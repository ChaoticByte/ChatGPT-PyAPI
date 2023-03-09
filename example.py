#!/usr/bin/env python3

# Copyright (c) 2023 Julian Müller (ChaoticByte)

from os import environ

from chatgpt_pyapi import ChatGPT
from chatgpt_pyapi import Message
from chatgpt_pyapi import Models
from chatgpt_pyapi import Roles


API_KEY = environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
    system_in = "Please provide the following answers as cynical as possible, but still correct."
    cgpt.add_to_chat(Message(system_in, role=Roles.SYSTEM))
    user_in = "Who are you?"
    print(f"USER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    user_in = "Could you please elaborate?"
    print(f"\nUSER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    print("\nMessage History:")
    [print(m.to_api()) for m in cgpt._message_history]
