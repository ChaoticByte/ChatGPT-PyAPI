# Copyright (c) 2023 Julian Müller (ChaoticByte)

from json import dumps, loads
from urllib import request as http_request


class Models:
    '''This class holds available models'''
    GPT_35_TURBO = "gpt-3.5-turbo"
    GPT_35_TURBO_0301 = "gpt-3.5-turbo-0301"


class Roles:
    '''This class holds available roles to be used in Messages'''
    ASSISTANT = "assistant"
    SYSTEM = "system"
    USER = "user"


class Message:
    '''Message type. Supports roles.'''

    def __init__(self, text: str, role: str = Roles.USER):
        assert type(text) == str
        assert type(role) == str
        self.text = text
        self.role = role

    @classmethod
    def from_api(cls, api_msg: dict):
        '''Create a Message object from API format'''
        assert type(api_msg) == dict
        msg = api_msg["choices"][0]["message"]
        msg["content"] = msg["content"].strip("\n")
        return cls(
            msg["content"],
            msg["role"])

    def to_api(self):
        '''Convert to API format'''
        return {"role": self.role, "content": self.text}

    def __str__(self):
        return f"Role: {self.role}, Text: {self.text}"


class ChatGPT:
    '''ChatGPT API'''

    API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

    def __init__(self, api_key: str, model: str = Models.GPT_35_TURBO):
        assert type(api_key) == str
        assert type(model) == str
        # Create string used in header
        self.auth = f"Bearer {api_key}"
        # This list will contain all prior messages
        self._message_history = []
        self.model = model

    def chat(self, message: Message) -> Message:
        '''Add a message to the message history & send it to ChatGPT. Returns the answer as a Message instance.'''
        self.add_to_chat(message)
        # Create api_input from message_history & encode it
        api_input = [m.to_api() for m in self._message_history]
        api_input_encoded = dumps(
            {"model": self.model, "messages": api_input},
            separators=(",", ":")).encode()
        # Create a Request object with the right url, data, headers and http method
        request = http_request.Request(
            self.API_ENDPOINT,
            data=api_input_encoded,
            headers={
                "Authorization": self.auth,
                "Content-Type": "application/json"
            },
            method="POST")
        # Send the request with r as the response
        with http_request.urlopen(request) as r:
            # Read response and parse json
            api_output = loads(r.read())
            # Convert to Message object
            response_message = Message.from_api(api_output)
            self._message_history.append(response_message)
            return response_message

    def add_to_chat(self, message: Message) -> Message:
        '''Add a message to the message history without sending it to ChatGPT'''
        # Check if the message parameter is the correct type
        assert type(message) == Message, "message must be an instance of Message"
        self._message_history.append(message)

    def clear_message_history(self):
        self._message_history = []
