# REST API application for completing generative AI tasks using OpenAI API, written in Python

## Installation

Install uv:
```
pip install uv
```
Clone the repo, cd to it and to create the venv and download the dependencies run:
```
uv venv
uv sync
```
If you've never used uv before: don't be suspicious if this takes one second - uv is super fast!

## How to run
You will need your OpenAI API key. For the day this readme version was commited, you need to create an account on OpenAI Platform and you do need to put a minimal amount of money (it was 5$ I believe) to be able to generate api keys. You cannot get one without paying anything (I tried and couldn't). For details please refer to OpanAI pages.

Once you have your api key, export it as an environment variable:
```
export OPENAI_API_KEY=<your_openai_api_key>
```
Now you should be able to run the app:
```
uv run fastapi run src/main.py 
```
The app by default runs on port 8000.

## Run the Docker container
You can run the app inside the Docker container. First from the root of this repo build the image:
```
docker build -t <tag_your_image> .
```
To run it and be able to access the app from outside, use port publishing:
```
docker run -it --rm -p choose_your_host_port:8000 <your_image>
```