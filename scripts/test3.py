import json
import sys
import os
from openai import OpenAI

def ask_gpt(prompt):
    client = OpenAI(
        api_key=os.environ.get("sk-svcacct-Ars-9ySzqRWHtJQJ6dNXQSW5hXcjawI-QXTscZUyw5fAmdT3BlbkFJHv8w9_xAhC78olSbhZ9xePGghSktBGCZez8FWC_wy3lDEA"),
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-0125",
    )

    result = {
        "id": response.id,
        "object": response.object,
        "created": response.created,
        "model": response.model,
        "choices": [{
            "message": choice.message.content,
            "finish_reason": choice.finish_reason,
            "index": choice.index
        } for choice in response.choices]
    }

    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        result = ask_gpt(user_input)
        print(json.dumps(result))
