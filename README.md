# RabbitMQ producer/consumer example

Requires Docker and Docker Compose to be installed.

```bash
// Build the containers in detached mode
$ docker-compose up -d

// Start the consumer container
$ docker-compose run app example consumer

// In another terminal run the producer
$ docker-compose run app example producer

// To simply enter the container run the following
$ docker-compose run app

// Now in container
root@c82061d93b6c:/usr/src/app#

// Access application via command line
root@c82061d93b6c:/usr/src/app example -h
```
