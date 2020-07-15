APP_NAME=freq_dist
HERE=$(shell pwd)
.PHONY: all

all: build run

build:
	docker build -t $(APP_NAME) .

run:
	docker run --rm --mount type=bind,source=$(HERE),target=/home/$(APP_NAME) $(APP_NAME)
