
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
        self.text = text
        self.role = role

    @classmethod
    def from_api(cls, message_dict:str):
        '''Create a Message object from API format'''
        return cls(
            message_dict["content"],
            message_dict["role"])

    def to_api(self):
        '''Convert to API format'''
        return {"role": self.role, "content": self.text}


class ChatGPT:
    '''ChatGPT API'''

    API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

    def __init__(self, api_key: str, model: str = Models.GPT_35_TURBO):
        # Create string used in header
        self.auth = f"Bearer {api_key}"
        # This list will contain all prior messages
        self.message_history = []
        self.model = model

    def chat(self, message: Message) -> Message:
        # check if the message parameter is the correct type
        assert type(message) == Message, "message must be an instance of Message"
        self.message_history.append(message)
        # create api_input from message_history & encode it
        api_input = [m.to_api() for m in self.message_history]
        api_input_encoded = dumps(
            {"model": self.model, "messages": api_input},
            separators=(",", ":")).encode()
        # create a Request object with the right url, data, headers and http method
        request = http_request.Request(
            self.API_ENDPOINT,
            data=api_input_encoded,
            headers={
                "Authorization": self.auth,
                "Content-Type": "application/json"
            },
            method="POST")
        # send the request with r as the response
        with http_request.urlopen(request) as r:
            # read response and parse json
            api_output = loads(r.read())
            api_output_answer = api_output["choices"][0]["message"]
            # remove leading and trailing newlines
            api_output_answer["content"] = api_output_answer["content"].strip("\n")
            # convert to Message object
            response_message = Message.from_api(api_output_answer)
            self.message_history.append(response_message)
            return response_message

    def clear_message_history(self):
        self.message_history = []
