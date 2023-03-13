#!/usr/bin/env python3

# Copyright (c) 2023 Julian Müller (ChaoticByte)

from os import environ
from sys import argv

from chatgpt_pyapi.openai import ChatGPT, Message, Models

# Read the API key from a environment variable
API_KEY = environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    # Create ChatGPT API instance
    cgpt = ChatGPT(API_KEY, model=Models.GPT_35_TURBO_0301)
    user_input = " ".join(argv[1:])
    print(cgpt.chat(Message(user_input)).text)
