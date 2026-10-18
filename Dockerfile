FROM python:3.10-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        wget \
        bash \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip wheel && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "flask --app app run -h 0.0.0.0 -p ${PORT:-8000} & exec python -m devgagan"]
