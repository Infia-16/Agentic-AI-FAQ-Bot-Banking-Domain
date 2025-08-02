import streamlit as st
import subprocess
import re
from langdetect import detect, LangDetectException  # pip install langdetect
from fuzzywuzzy import fuzz  #  fuzzy matching for greeting detection

# === Config ===
OLLAMA_PATH = r"C:/Users/paul/AppData/Local/Programs/Ollama/ollama.exe"
MODEL_NAME = "qwen"

# === Scenario Definitions ===
scenario_fields = {
    "Loan Enquiry": ["user_name", "loan_type"],
    "Loan Pre-Approval": ["user_name", "monthly_income", "employment_type", "loan_type"],
    "Account Balance Check": ["user_name", "authenticated", "account_type"],
    "KYC Status Update": ["user_name", "customer_id", "dob"],
    "EMI Schedule/Breakup": ["user_name", "loan_amount", "interest_rate", "loan_tenure"],
    "Interest Rate Info": ["user_name", "loan_type"],
    "Credit Card Status": ["user_name", "card_type"],
    "Transaction Dispute": ["user_name", "transaction_id", "reason"],
    "Loan Retrieval": ["user_name", "loan_id"]
}

# === System Prompt ===
def build_system_prompt():
    guidelines = "\n".join(
        f"{scenario}:\n" + "\n".join(f"  - {field} (str)" for field in fields)
        for scenario, fields in scenario_fields.items()
    )
    return f"""
You are a smart and friendly **English-only** banking assistant. Your job is to respond ONLY to banking-related queries and always in English.

 If the user input is in any other language like Hindi, French, Tamil etc., reply:
"I’m sorry, I can only understand and respond in English. Please ask in English."

 If the user asks anything unrelated to banking (like celebrities, sports, movies, tech etc.), you must respond:
"I can only assist with banking-related topics like loans, EMI, KYC, account status, credit cards, and transactions."

 If user says "Hi this is [Name]", greet them normally.

 Your job is to understand the user intent (e.g., KYC update, loan enquiry, balance check) and ask for required info step by step using these guidelines:

{guidelines}

 Never mention scenario names directly to the user. Ask follow-up questions to collect missing fields conversationally.

 Strictly reject any queries that are NOT about banking.
""".strip()

# === Query LLM (Qwen via Ollama) ===
def query_llm(system_prompt, history):
    user_message = history[-1][1] if history else ""
    prompt = f"{system_prompt}\n\nUser: {user_message}\nAssistant:"
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", MODEL_NAME],
            input=prompt.encode("utf-8"),
            capture_output=True,
            timeout=60
        )
        return result.stdout.decode("utf-8").strip() or " I couldn’t generate a response. Please try again."
    except Exception as e:
        return f" An error occurred while querying the model: {e}"

# === Language Detection (Improved) ===
def is_non_english_input(text):
    try:
        # Allow words that contain letters and/or digits (e.g., "Loan123", "456")
        cleaned = " ".join(re.findall(r"[A-Za-z0-9]{2,}", text))
        if len(cleaned.split()) < 2:
            return False
        lang = detect(cleaned)
        return lang != "en"
    except LangDetectException:
        return False

# === Fuzzy Greeting Detection ===
def fuzzy_greeting_match(text, threshold=85):
    known_greetings = [
        "hello", "hi", "hey", "greetings",
        "good morning", "good evening", "good afternoon",
        "how are you", "how was your day"
    ]
    for greet in known_greetings:
        if fuzz.partial_ratio(greet.lower(), text.lower()) >= threshold:
            return True
    return False

# === Named Greeting Extraction (more flexible)
def extract_named_greeting(user_input):
    match = re.search(r"\b(this is|i am|i'm)\s+([A-Za-z]+)", user_input.lower())
    if match:
        return match.group(2).capitalize()
    return None

# === Streamlit UI ===
st.set_page_config("Banking Assistant 💬", layout="wide")
st.title("🤖 Banking Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

# Display chat history
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

# User Input
user_input = st.chat_input("Ask your banking question...")

# Handle Input
if user_input:
    st.session_state.chat.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    name = extract_named_greeting(user_input)

    #  First handle greetings
    if name:
        response = f" Hello {name}! How can I assist you with your banking needs today?"
    elif fuzzy_greeting_match(user_input):
        response = " Hello! How can I assist you today?"

    #  Then handle language
    elif is_non_english_input(user_input):
        response = " I'm sorry, I can only understand and respond in English. Please rephrase your message in English."

    #  Otherwise, send to LLM
    else:
        with st.spinner("Thinking..."):
            system_prompt = build_system_prompt()
            response = query_llm(system_prompt, st.session_state.chat)

    st.session_state.chat.append(("assistant", response))
    st.chat_message("assistant").markdown(response)
