FROM python:3.11-slim
WORKDIR /app
COPY infra/requirements.txt /app/
RUN pip install -r requirements.txt
COPY src /app/src
CMD ["uvicorn", "src.services.risk_scoring_api.app:app", "--host", "0.0.0.0", "--port", "8080"]
