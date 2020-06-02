.PHONY: app

app:
	python3 MorseCoder.py

ui:
	pyuic5 MorseCoder.ui -o UI.py

