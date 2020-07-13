FROM python:3.5 as base

WORKDIR /src

COPY requirements.txt ./requirements.txt

RUN pip install --user -r ./requirements.txt

COPY endpoint.py .

COPY app ./app

FROM python:3.5-slim-buster

WORKDIR /src

COPY --from=base /src /src

COPY --from=base /root/.local /root/.local

CMD python ./endpoint.py
