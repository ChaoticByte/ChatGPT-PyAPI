# ChatGPT-PyAPI

A minimalistic Python Library for OpenAI's ChatGPT and Bing's Chatbot

## Supported APIs

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

This requires the [EdgeGPT](https://github.com/acheong08/EdgeGPT) library to be installed, and your Cookies to be exported to a json file. See [EdgeGPT's README](https://github.com/acheong08/EdgeGPT#readme) for more infos.

## Examples

For examples, take a look at `examples.py`.

## CLI

Using the official API via ChatGPT:
```
OPENAI_API_KEY="..." ./cli.py Hello
```

Using Bing's Chatbot:
```
BING_COOKIES_FILE="~/cookies.json" ./cli.py bing Hello
```
