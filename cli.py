#!/usr/bin/env python3

# Copyright (c) 2023 Julian Müller (ChaoticByte)

from os import environ
from sys import argv

if __name__ == "__main__":
    bing = False
    if len(argv) > 2:
        bing = argv[1] == "bing"
    if bing:
        from chatgpt_pyapi.bing import ChatGPT, Message, ConversationStyle
        # Read the path to the cookies file from a environment variable
        BING_COOKIES_FILE = environ["BING_COOKIES_FILE"]
        # Create ChatGPT API instance
        cgpt = ChatGPT(BING_COOKIES_FILE, ConversationStyle.balanced)
        user_input = " ".join(argv[2:])
    else:
        from chatgpt_pyapi.openai import ChatGPT, Message, Models
        # Read the API key from a environment variable
        API_KEY = environ["OPENAI_API_KEY"]
        # Create ChatGPT API instance
        cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
        user_input = " ".join(argv[1:])
    print(cgpt.chat(Message(user_input)).text)
