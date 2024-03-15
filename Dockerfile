FROM python:3.12-alpine

ENV PORT=8000

WORKDIR /usr/src/app

COPY requirements.txt .

# Install alpine base dependencies 
# then upgrade an install pip requirements 
# finally cleanup everything to keep the image small
# profit!
RUN apk add build-base && \
    apk add gcc musl-dev python3-dev libffi-dev openssl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \ 
    apk del build-base && \ 
    apk del gcc musl-dev python3-dev libffi-dev openssl-dev && \
    rm -rf /var/cache/apk/*

COPY ./src /src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

