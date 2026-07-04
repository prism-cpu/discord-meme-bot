import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment")


def generate_blog(paragraph_topic: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that writes a short paragraph."
            },
            {
                "role": "user",
                "content": f"Write a paragraph about the following topic: {paragraph_topic}"
            }
        ],
        max_tokens=120,
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print(generate_blog("advantages of buying a nothing headset over random boat earphones"))