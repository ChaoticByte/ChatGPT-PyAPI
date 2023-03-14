# ChatGPT-PyAPI

A minimalistic Python API for OpenAI's ChatGPT and Bing's Chatbot

## Supported APIs

- Official ChatGPT API by OpenAI
- Unofficial API for Bing Chatbot (requires [EdgeGPT](https://github.com/acheong08/EdgeGPT) to be installed)

### Official ChatGPT API by OpenAI

You need an API key for the official ChatGPT API.

The following models are supported:

    - GPT-4
    - GPT-4-0314
    - GPT-4-32k
    - GPT-4-32k-0314
    - GPT-3.5-Turbo
    - GPT-3.5-Turbo-0301

### Unofficial Bing Chatbot API

This requires your Cookies to be exported to a json file. See [EdgeGPT's README](https://github.com/acheong08/EdgeGPT#readme) for more infos.

## CLI

Using the official API via ChatGPT:
```
OPENAI_API_KEY="..." ./cli.py Hello
```

Using Bing's Chatbot:
```
BING_COOKIES_FILE="~/cookies.json" ./cli.py bing Hello
```
