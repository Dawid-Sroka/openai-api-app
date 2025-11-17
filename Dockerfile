FROM python:3.10

RUN pip install uv

WORKDIR /app

COPY . /app/

RUN uv sync --frozen --no-dev

ENV OPENAI_API_KEY placeholder_openai_api_key

CMD ["uv", "run", "fastapi", "run", "/app/src/main.py"]
