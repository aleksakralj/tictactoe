deps:
	pip install --no-cache-dir -r requirements.txt

test:
	python3 -m pytest tests/

run:
	python main.py