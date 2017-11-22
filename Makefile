DK=docker
DC=docker-compose


build:
	$(DC) build

run:
	$(DC) up -d

down:
	$(DC) down

ps:
	$(DC) ps

dps:
	$(DK) ps

img:
	$(DK) images

clean:
	$(DK) stop $(shell $(DK) ps -a -q) && $(DK) rm $(shell $(DK) ps -a -q)
	$(DK) rmi -f $(shell $(DK) images -q)


