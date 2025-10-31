# 🤖 ROMA Research Agent

A simple **local AI research assistant** built using [ROMA](https://github.com/sentient-agi/ROMA) and [sentient-agent-framework](https://pypi.org/project/sentient-agent-framework/).  
It runs locally in your terminal and answers queries in real time using OpenRouter-powered models.

---

## 🚀 Features

- Built on **ROMA** (Research Oriented Multi-Agent) framework  
- Runs **fully locally** in terminal  
- Simple, clean async Python code  
- Uses **OpenRouter API** for intelligent responses  
- Easy to clone, run, and modify


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
```
Activate it:
* Windows
```bash
venv\Scripts\activate
```
* Mac/Linux
```bash
source venv/bin/activate
```

## 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## 4️⃣ Create .env file
* Create a new file named .env in the project root and add your OpenRouter key: [OpenRouter](https://openrouter.ai/)
```bash
OPENROUTER_API_KEY=your_key_here
```

## 5️⃣ Run the agent:
```bash
python main.py
```

## 👾 Example
```bash
🤖 ROMA Research Agent started! Type your queries below.
💡 Type 'exit' or 'quit' to stop.

🔍 You: what is bitcoin?
💬 Bitcoin is a decentralized digital currency that allows peer-to-peer transactions...
```

## 📦 Requirements
* Your requirements.txt should include:
```bash
httpx
aiohttp
ulid-py
python-dotenv
sentient-agent-framework
arxiv
```

## 🧠 Notes
* If you cloned ROMA manually before, you can safely delete the ROMA/ folder — this project now installs it as a dependency.
* All responses are streamed to your console asynchronously.
* Works perfectly on Windows, macOS, or Linux.

## 👨‍💻 Author
 **Developed with ❤️ by [prithboy](https://x.com/Prith_boy) for [sentient](https://x.com/SentientAGI)**
