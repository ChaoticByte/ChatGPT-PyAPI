#!/usr/bin/env python3

from os import environ

from chatgpt_pyapi import ChatGPT
from chatgpt_pyapi import Models
from chatgpt_pyapi import Message


API_KEY = environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
    user_in = "Who are you?"
    print(f"USER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    user_in = "Could you please elaborate?"
    print(f"\nUSER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    print("\nMessage History:")
    [print(m.to_api()) for m in cgpt.message_history]
