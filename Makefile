.PHONY: help build run-rabbitmq run-master stop-master run-slave stop-slave clean push

.DEFAULT: help
help:
	@echo "make build"
	@echo "		Building with docker-compose has been started."
	@echo "make run-rabbitmq"
	@echo "		Rabbitmq message broker has been started."
	@echo "make stop-rabbitmq"
	@echo "		Rabbitmq message broker has been stopped."
	@echo "make run-master"
	@echo "		Master container has been started."
	@echo "make stop-master"
	@echo "		Master container has been stopped."
	@echo "make run-slave"
	@echo "		Slave container has been started."
	@echo "make stop run-slave"
	@echo "		Slave container has been stopped."
	@echo "make clean"
	@echo "		Cleans project-related files."
	@echo "make push"
	@echo "		Pushes to github repository."

build:
	@echo "Builds images with docker-compose tool"
	docker-compose build

run-rabbitmq:
	@echo "Starts rabbitmq message-broker tool"
	docker-compose up -d rabbitmq

stop-rabbitmq:
	@echo "Stops & Removes rabbitmq message-broker container"
	docker-compose stop rabbitmq && docker-compose rm -f rabbitmq

run-master:
	@echo "Starts master container in interactive mode"
	docker-compose run master /bin/sh

stop-master:
	@echo "Stops & Removes master container"
	docker-compose stop master && docker-compose rm -f master

run-slave:
	@echo "Starts slave container"
	docker-compose up -d $$slave

stop-slave:
	@echo "Stops & Removes slave continer"
	docker-compose stop $(slave) && docker-compose rm -f $(slave)

clean:
	@echo "Cleans project related files."

push:
	@echo "Moves the changes to github repository"
	git push git@github.com:celikelozdinc/ThesisWork.git
