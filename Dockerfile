FROM python:3.10

WORKDIR /bewise_ai_text

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]