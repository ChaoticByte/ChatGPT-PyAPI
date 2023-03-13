#!/usr/bin/env python3

# Copyright (c) 2023 Julian Müller (ChaoticByte)

from os import environ
from sys import argv

example_system_message = "Please provide the following answers as cynical as possible, but still correct."
example_questions = [
    "Who are you?",
    "Could you please elaborate?"
]

if __name__ == "__main__":
    bing = False
    if len(argv) > 1:
        bing = argv[1] == "bing"
    if bing:
        from chatgpt_pyapi.bing import ChatGPT, Message, ConversationStyle
        # Read the path to the cookies file from a environment variable
        BING_COOKIES_FILE = environ["BING_COOKIES_FILE"]
        # Create ChatGPT API instance (with creative answers)
        cgpt = ChatGPT(BING_COOKIES_FILE, ConversationStyle.creative)
        cgpt.chat(Message(example_system_message))
    else:
        from chatgpt_pyapi.openai import ChatGPT, Message, Models, Roles
        # Read the API key from a environment variable
        API_KEY = environ["OPENAI_API_KEY"]
        # Create ChatGPT API instance
        cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
        # Provide a system message that will influence the answers
        sys_msg = Message(example_system_message, role=Roles.SYSTEM)
        # Add the message to the history, but don't send it yet
        cgpt.add_to_chat(sys_msg)
    # Have a little chat :D
    for q in example_questions:
        print(f"\nUSER: {q}")
        print(cgpt.chat(Message(q)).text)
    # Print out message history
    print("\nMessage History:")
    [print(str(m)) for m in cgpt._message_history]
