.PHONY: install test run

export HOST=0.0.0.0
export PORT=8000

install:
	@pip install pipenv
	@pipenv install --skip-lock --dev

test:
	@pipenv run pytest --cov-report xml --cov=./

run:
	@pipenv run gunicorn -b $(HOST):$(PORT) api:app --workers=3

deploy:
	@docker build --build-arg PORT=$(PORT) -t rwximg .
	@docker run -d -p $(PORT):$(PORT) --name rwx rwximg
