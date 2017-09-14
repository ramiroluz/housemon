.PHONY: test py.test run

test: 
	python -m unittest discover -p 'test*' -v

py.test:
	py.test --verbose --color=yes test*

run:
	python app.py
