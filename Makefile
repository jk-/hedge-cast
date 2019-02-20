.PHONY: init assets

init:
	pip install pip-tools
	pip-sync requirements.txt

assets:
	rm -rf ./app/static
	mkdir -p ./app/static
	cp -fr ./app/assets/images ./app/static
	cp -fr ./app/assets/downloads ./app/static/downloads

test:
	pip install -qr requirements.txt
	pip install -qr requirements-test.txt
	pytest --codestyle -p no:warnings -vv --ignore=migrations
	rm -rf .pytest_cache
	find . -name '*.pyc' -delete

migrate:
	flask db migrate
	flask db upgrade
