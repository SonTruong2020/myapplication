FROM python:3.8-alpine3.12 as base

WORKDIR /src

COPY . .

RUN pip install --user -r ./requirements.txt

COPY endpoint.py .

COPY app ./app

# Was unable to find a smaller image to reduce size
FROM python:3.8-alpine3.12

WORKDIR /src

RUN apk update

RUN apk add git

COPY --from=base /src /src

COPY --from=base /root/.local /root/.local

CMD python ./endpoint.py
