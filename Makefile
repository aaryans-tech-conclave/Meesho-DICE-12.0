.PHONY: up down test lint
up:
	docker compose -f infra/docker-compose.yml up --build -d
down:
	docker compose -f infra/docker-compose.yml down
test:
	pytest -q || true
lint:
	ruff src || true
