
# 💬 Agentic AI FAQ Bot for Banking Domain

An intelligent banking assistant built using Agentic AI principles, designed to answer user queries across 9 banking scenarios via natural, multi-turn conversations. This chatbot is strictly limited to English and banking-related queries, ensuring domain safety and relevance. Powered by [Ollama](https://ollama.com) with the lightweight Qwen 0.5B model and deployed via Streamlit.

---

## 🚀 Demo

👉 [Run Locally](#-local-setup) | 🏦 Supports: Loan Enquiry, KYC Update, EMI Schedule, and more.

---

## 📌 Features

- 🧠 **Agentic AI Logic** – Multi-turn conversations based on user input and scenario understanding.
- 🏦 **Banking-Only Mode** – Rejects non-banking topics and non-English queries with polite fallback.
- 📄 **9 Scenario Modules** – Includes Loan Enquiry, Account Balance, Credit Card Status, Transaction Dispute, etc.
- ⚙️ **Qwen 0.5B + Ollama** – Lightweight LLM used for efficient response generation.
- 🌐 **Streamlit UI** – Simple and interactive web interface with MVC architecture.
- 🔐 **Input Validation** – Ensures only appropriate domain and language-specific interactions.

---

## 💼 Banking Scenarios Supported

1. Loan Enquiry  
2. Loan Retrieval  
3. Account Balance Check  
4. Credit Card Application/Status  
5. Transaction Dispute  
6. Interest Rate Information  
7. Loan Pre-Approval Check  
8. EMI Schedule/Breakdown  
9. KYC Status Update

Each scenario has a unique hardcoded response format (with emojis) and is dynamically filled based on user inputs.

---

## 👩‍💻 My Contributions

- Designed structured prompt templates for 9 banking scenarios.
- Built agentic multi-turn flow with validation and fallback logic.
- Developed full Streamlit UI using MVC separation.
- Integrated Ollama’s Qwen 0.5B for local LLM support.
- Enforced domain and language restrictions with system prompt + code checks.

---

## 🛠️ Local Setup

### 1. Prerequisites

- Python 3.10+
- Ollama (for local LLM inference): [Install Ollama](https://ollama.com)
- Streamlit

### 2. Installation

```bash
# Clone the repo
git clone https://github.com/your-username/agentic-ai-banking-faq-bot.git
cd agentic-ai-banking-faq-bot

# Set up environment
pip install -r requirements.txt

# Pull the Qwen 0.5B model
ollama pull qwen:0.5b

# Run the Streamlit app
streamlit run unified_chatbot.py
````

---



## ⚠️ Constraints

* ❌ No responses to non-English queries
* ❌ No support for entertainment, politics, sports, or unrelated topics
* ✅ Only banking-related, FAQ-style, professional conversations

---

## 📸 Screenshots
<img width="959" height="877" alt="Screenshot 2025-07-29 092959" src="https://github.com/user-attachments/assets/f0033ae7-e39b-42c5-b083-74b191d1e335" />



## 📝 License

MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgements

* [Ollama](https://ollama.com) – For lightweight on-device LLM deployment.
* [Streamlit](https://streamlit.io) – For building fast, interactive apps.
* [Qwen 0.5B](https://github.com/QwenLM) – LLM used for conversation understanding.

---


