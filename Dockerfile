FROM python:3.9-bullseye

# Install postgres driver
RUN apt update && apt -y install libpq-dev

WORKDIR /srv

COPY *.py requirements.txt ./
COPY data/ ./data/
COPY src/ ./src/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "etl_chup_prostate.py"]