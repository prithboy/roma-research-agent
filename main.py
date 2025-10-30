import os
import sys
import ulid
import asyncio
import aiohttp

# 🧩 Patch: make ULID compatible with Pydantic 2.x
from pydantic import BaseModel
BaseModel.model_config = {"arbitrary_types_allowed": True}

# ✅ Import ROMA framework
from sentient_agent_framework.interface.agent import AbstractAgent
from sentient_agent_framework.interface.request import Query
from sentient_agent_framework.interface.response_handler import ResponseHandler


# 🧠 OpenRouter helper function
async def get_openrouter_response(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model": os.getenv("OPENROUTER_MODEL", "meta-llama/llama-4-maverick:free"),
        "messages": [{"role": "user", "content": prompt}],
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as resp:
            if resp.status != 200:
                error = await resp.text()
                return f"⚠️ Error from OpenRouter ({resp.status}): {error}"
            result = await resp.json()
            return result["choices"][0]["message"]["content"]


# ✅ Dummy Session
class DummySession:
    def __init__(self, session_id="local-test"):
        self.session_id = session_id


# ✅ ROMA Research Agent
class ROMAResearchAgent(AbstractAgent):
    async def assist(self, session: DummySession, query: Query, response_handler: ResponseHandler):
        print(f"\n🧠 ROMA Agent Active")
        print(f"📥 Received query: {query.prompt}")

        # 🔗 Fetch response from OpenRouter
        ai_response = await get_openrouter_response(query.prompt)
        await response_handler.send_text(ai_response)


# ✅ Console Response Handler
class ConsoleResponseHandler(ResponseHandler):
    async def send_text(self, text: str):
        print(f"💬 {text}")


# ✅ Main App
async def main():
    agent = ROMAResearchAgent(name="ROMA Research Agent")
    session = DummySession()
    handler = ConsoleResponseHandler()

    print("🤖 ROMA Research Agent started! Type your queries below.")
    print("💡 Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("🔍 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        query = Query(
            id=ulid.new(),
            prompt=user_input,
            input=user_input,
        )

        await agent.assist(session, query, handler)


if __name__ == "__main__":
    asyncio.run(main())
