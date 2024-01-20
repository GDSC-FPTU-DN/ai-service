import os
from openai import OpenAI
from .conversation_storage import get_conversation_storage, update_conversation_storage


BASE_ENHANCE_PROMPT = {
    "role": "system", "content": "You are a helpful assistant. You are helping a customer to solve a problem."}


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def send_message(prompt: str):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            BASE_ENHANCE_PROMPT,
            {"role": "user", "content": prompt}
        ]
    ).choices[0].message.content


def send_message_conversation(conversation_id: str, prompt: str):
    # Update conversation
    update_conversation_storage(conversation_id, "user", prompt)
    # Generate response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            BASE_ENHANCE_PROMPT,
            *get_conversation_storage(conversation_id),
            {"role": "user", "content": prompt}
        ]
    ).choices[0].message.content
    # Update conversation
    update_conversation_storage(conversation_id, "assistant", response)
    return response
