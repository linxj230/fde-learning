from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # 读取 .env 里的 Key，避免硬编码

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",  # DeepSeek 兼容 OpenAI 协议
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个直接、不说废话的技术顾问。"},
        {"role": "user", "content": "用一句话解释什么是 Forward Deployed Engineer，并举例说明它和普通后端工程师的区别。"},
    ],
    temperature=0.7,
)

print(resp.choices[0].message.content)
