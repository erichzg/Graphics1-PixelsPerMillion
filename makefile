all: validPpm.py
	python validPpm.py
run: all
	display image.ppm
