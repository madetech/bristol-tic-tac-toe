
.PHONY: install
install:
	python -m venv venv && . venv/bin/activate && pip --quiet install --upgrade pip && pip install -r requirements.txt

.PHONY: activate
activate: 
	. venv/bin/activate

.PHONY: test
test:
	pytest
	
