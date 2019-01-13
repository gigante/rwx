.PHONY: install

export HOST=0.0.0.0
export PORT=8000

install:
	@pipenv install --skip-lock --dev

test:
	@pytest

run:
	@gunicorn -b $(HOST):$(PORT) api:app