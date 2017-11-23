DK=docker
DC=docker-compose

# Command to get all containers
CONTS=$(shell $(DK) ps -a -q)

# Builds images
build:
	./check-log-dir.sh
	$(DC) pull
	$(DC) build --force-rm

# Start the containers
up:
	$(DC) up -d

# Stops all docker compose related containers
down:
	$(DC) down

# Invokes ps command on docker-compose
ps:
	$(DC) ps

# Invokes ps command on docker
dps:
	$(DK) ps

# Lists all images
img:
	$(DK) images

# Build consumer container
con:
	$(DC) build consumer

# Logs for consumer container
logscon:
	$(DC) logs consumer

# Shows application logging for consumer container
flogcon:
	cat ./logs/consumer.log | grep root.

# Logs for producer container
logsprod:
	$(DC) logs producer

# Shows application logging for producer container
flogprod:
	cat ./logs/producer.log | grep root.

# Logs for RabbitMQ
logsra:
	$(DC) logs rabbit

# Build producer container
prod:
	$(DC) build producer

# Run producer container
rprod:
	$(DC) run producer

# Build CLI container
cl:
	$(DC) build cli

# Removes all images
rmi:
	$(DK) rmi -f $(shell $(DK) images -q)

# Stops all containers
stop:
	$(DK) stop $(CONTS)

# Removes all containers (forces running to stop)
rm:
	$(DK) rm -f $(CONTS)

# Removes containers and all images
clean: rm rmi
