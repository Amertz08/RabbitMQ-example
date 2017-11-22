# RabbitMQ producer/consumer example

Requires Docker and Docker Compose to be installed.

## Makefile

This is probably the easiest way to run if not familiar with Docker & Docker Compose CLI

[Makefile](Makefile)

## Using Docker & Docker Compose commands

These are some of the underlying Docker & Docker Compose commands

```bash
// Build the containers in detached mode
$ docker-compose up -d

// Check that consumer and RabbitMQ containers are up and running
$ docker ps

// Run the producer function from outside the container
$ docker-compose run producer example producer

// Or enter producer container and run from inside it
$ docker-compose run producer

// Now in container
root@c82061d93b6c:/usr/src/app# example producer

// Check consumer logs
$ docker-compose logs consumer

// To startup and enter an instance of the consumer container
$ docker-compose run consumer bash

// Now in container
root@c82061d93b6c:/usr/src/app#

// Access application via command line
root@c82061d93b6c:/usr/src/app example -h

// Shutdown all containers
$ docker-compose down
```
