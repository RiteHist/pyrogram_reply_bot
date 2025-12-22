FROM python:3.11.13-alpine AS base
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.13-alpine
COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base /usr/local/bin /usr/local/bin
COPY . .
CMD ["python", "main.py"]