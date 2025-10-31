# 🧩 ROMA Research Agent

A local AI research assistant powered by [ROMA](https://github.com/sentient-agi/ROMA) and the Sentient Agent Framework.  
Built to search, analyze, and respond to your research queries locally.

---

## 🚀 Features
- Uses the ROMA framework for local AI orchestration  
- Fetches research papers from Arxiv  
- Chat-like local interface  
- 100% local run (no frontend needed)

---

## 🧰 Requirements
- Python 3.10+
- Internet connection
- OpenRouter API key

---

## 🛠️ Installation

## 1️⃣ Clone the repo:
```bash
git clone https://github.com/prithboy/roma-research-agent.git
cd roma-research-agent
```

## 2️⃣ Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## 4️⃣ Copy `.env.example → .env` and add your OpenRouter API key:
* get your openrouter api key from [OpenRouter](https://openrouter.ai/)
```bash
OPENROUTER_API_KEY=your_key_here
```

## 5️⃣ Run the agent:
```bash
python main.py
```

## 👾 Example Usage
```bash
🤖 ROMA Research Agent started!
💡 Type 'exit' or 'quit' to stop.

🔍 You: Explain quantum entanglement in simple terms
```

## 👨‍💻 Author
 **Developed with ❤️ by [prithboy](https://x.com/Prith_boy) for [sentient](https://x.com/SentientAGI)**
