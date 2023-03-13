#!/usr/bin/env python3

# Copyright (c) 2023 Julian Müller (ChaoticByte)

from os import environ

from chatgpt_pyapi.openai import ChatGPT, Message, Models, Roles

# Read the API key from a environment variable
API_KEY = environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    # Create ChatGPT API instance
    cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
    # Provide a system message that will influence the answers
    system_in = "Please provide the following answers as cynical as possible, but still correct."
    # Add the message to the history, but don't send it yet
    cgpt.add_to_chat(Message(system_in, role=Roles.SYSTEM))
    # Have a little chat :D
    user_in = "Who are you?"
    print(f"USER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    user_in = "Could you please elaborate?"
    print(f"\nUSER: {user_in}")
    print(cgpt.chat(Message(user_in)).text)
    # Print out message history
    print("\nMessage History:")
    [print(m.to_api()) for m in cgpt._message_history]
