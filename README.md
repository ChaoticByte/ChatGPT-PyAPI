# ChatGPT-PyAPI

A minimalistic Python API for OpenAI's ChatGPT and Bing's Chatbot

## Supported APIs

- Official ChatGPT API by OpenAI
- Unofficial API for Bing Chatbot (required `EdgeGPT` to be installed)

### Official ChatGPT API by OpenAI

You need an API key for the official ChatGPT API.

### Unofficial API for Bing Chatbot

This requires your Cookies to be exported to a json file. See [EdgeGPT's README](https://github.com/acheong08/EdgeGPT) for more infos.

## CLI

Using the official API via ChatGPT:
```
OPENAI_API_KEY="..." ./cli.py Hello
```

Using Bing's Chatbot:
```
BING_COOKIES_FILE="~/cookies.json" ./cli.py bing Hello
```
