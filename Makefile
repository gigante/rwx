.PHONY: install test run

export HOST=0.0.0.0
export PORT=8000

install:
	@pipenv install --skip-lock --dev

test:
	@pytest --cov-report xml --cov=./

run:
	@gunicorn -b $(HOST):$(PORT) api:app
