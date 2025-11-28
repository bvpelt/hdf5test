GEN=openapi-generator

generate:
	java -jar openapi-generator-cli.jar generate \
	  -i openapi/knmi.json \
	  -g python \
	  -o knmi_client

install:
	pip install -e knmi_client
	pip install -e .

run:
	python src/hdf5test/example.py

test:
	pytest

format:
	black .

run-example:
	python -m hdf5test.example

