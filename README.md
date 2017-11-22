# RabbitMQ producer/consumer example

Requires Docker and Docker Compose to be installed.

```bash
// Build the containers in detached mode
$ docker-compose up -d

// Check that containers are up and running
$ docker ps

// Start the consumer container
$ docker-compose run consumer

// In another terminal run the producer
$ docker-compose run producer

// Now in container
root@c82061d93b6c:/usr/src/app#

// To startup and enter an instance of the consumer container
$ docker-compose run consumer bash

// Now in container
root@c82061d93b6c:/usr/src/app#

// Access application via command line
root@c82061d93b6c:/usr/src/app example -h

// Shutdown all containers
$ docker-compose down
```
