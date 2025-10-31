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
* then run this in your terminal:
```bash
setx OPENROUTER_API_KEY "sk-or-v1-your_api_key_here"
```
* ⚠️ Close and reopen your Command Prompt after running `setx`.
To verify:
```bash
echo %OPENROUTER_API_KEY%
```
* If it shows your key (partially hidden), you're good.

* since you repoen your terminal so before entering run command activate `venv` again
```bash
python -m venv venv
venv\Scripts\activate
```

## 🚨 Fix ULID (if any error occurs)
If you face this error: `AttributeError: module 'ulid' has no attribute 'new'`

Run these commands:
```bash
pip uninstall -y ulid ulid-py ulid3
pip install ulid-py
```
Optionally, upgrade pip to avoid compatibility issues:
```bash
python -m pip install --upgrade pip
```

## 5️⃣ Run the agent:
```bash
python main.py
```
Now you can chat directly with the ROMA Research Agent, 
Type your questions and it will respond intelligently using the ROMA framework.

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
ulid-py==1.1.0
python-dotenv
sentient-agent-framework
arxiv
pydantic
```

## 🧠 Notes
* If you cloned ROMA manually before, you can safely delete the ROMA/ folder — this project now installs it as a dependency.
* All responses are streamed to your console asynchronously.
* Works perfectly on Windows, macOS, or Linux.

## 👨‍💻 Author
 **Developed with ❤️ by [prithboy](https://x.com/Prith_boy) for [sentient](https://x.com/SentientAGI)**
