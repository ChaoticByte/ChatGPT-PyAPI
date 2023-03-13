# Copyright (c) 2023 Julian Müller (ChaoticByte)

import asyncio

from json import dumps, loads

from EdgeGPT import Chatbot as _Chatbot
from EdgeGPT import ConversationStyle


class _Roles:
    ASSISTANT = "assistant"
    USER = "user"

class Message:
    '''Message type'''

    def __init__(self, text: str, _role:str=_Roles.USER):
        assert type(text) == str
        assert type(_role) == str
        self.text = text
        self.role = _role

    @classmethod
    def from_api(cls, api_msg: dict):
        '''Create a Message object from API format'''
        assert type(api_msg) == dict
        text = api_msg["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"].strip("\n")
        return cls(
            text,
            _role=_Roles.ASSISTANT)

    def to_api(self):
        '''Convert to API format'''
        return self.text
    
    def __str__(self):
        return f"Role: {self.role}, Text: {self.text}"


class ChatGPT:
    '''ChatGPT API'''

    def __init__(self, cookies_file_path:str, conversation_style=ConversationStyle.precise):
        self.bot = _Chatbot(cookiePath=cookies_file_path)
        self.conversation_style = conversation_style
        self._message_history = []
        self._event_loop = asyncio.get_event_loop()

    def __del__(self):
        self._event_loop.run_until_complete(
            self.bot.close())

    def chat(self, message: Message) -> Message:
        '''Add a message to the message history & send it to Bings Chatbot. Returns the answer as a Message instance.'''
        self._message_history.append(message)
        # Ask the bot
        api_output = self._event_loop.run_until_complete(
            self.bot.ask(message.to_api(), conversation_style=self.conversation_style))
        response_message = Message.from_api(api_output)
        self._message_history.append(response_message)
        return response_message

    def clear_message_history(self):
        self._message_history = []
