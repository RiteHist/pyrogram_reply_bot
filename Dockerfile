FROM python:3.11.13-alpine
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]