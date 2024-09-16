# chatgpt_query.py

import sys
import openai

# Substitua YOUR_API_KEY pela sua chave da API do OpenAI
openai.api_key = "sk-svcacct-Ars-9ySzqRWHtJQJ6dNXQSW5hXcjawI-QXTscZUyw5fAmdT3BlbkFJHv8w9_xAhC78olSbhZ9xePGghSktBGCZez8FWC_wy3lDEA"

def query_chatgpt(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-0125",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        result = query_chatgpt(user_input)
        print(result)
