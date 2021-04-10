bootstrap:
	poetry --version || curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	poetry install

test:
	poetry run test

lint:
	poetry run lint

package:
	poetry build
	poetry export -f requirements.txt --output requirements.txt

clean:
	find  . -type d -name __pycache__ -print | xargs rm -rf
	find  . -type d -name .pytest_cache -print | xargs rm -rf
	rm -rf dist htmlcov .mypy_cache


#export SONAR_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXX
qualitygate:
	docker run --rm --user="$(shell id -u):$(shell id -g)" -e SONAR_HOST_URL="https://sonarcloud.io/" -e SONAR_LOGIN="${SONAR_TOKEN}" -v "$(shell pwd):/usr/src" sonarsource/sonar-scanner-cli -Dproject.settings=.sonarcloud.properties