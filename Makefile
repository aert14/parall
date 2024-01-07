init:
	python -m pip install poetry
	poetry install --no-root

test:
	poetry run pytest -sv homework/tests
test_task_%:
	poetry run pytest -sv homework/tests/test_task_$*.py