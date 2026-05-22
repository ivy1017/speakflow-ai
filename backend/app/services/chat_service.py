from app.clients.deepseek_client import client


async def generate_reply(user_text: str):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": """
你是一个英语口语陪练老师。
用英文回复。
"""
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        )

        print(response)

        return response.choices[0].message.content

    except Exception as e:
        print("DeepSeek 调用失败:", e)
        return "Sorry, AI is temporarily unavailable."