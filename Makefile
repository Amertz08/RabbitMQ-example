DK=docker
DC=docker-compose


build:
	$(DC) pull
	$(DC) build --force-rm

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

logs:
	$(DC) logs consumer

prod:
	$(DC) run producer

rmi:
	$(DK) rmi -f $(shell $(DK) images -q)

clean:
	$(DK) stop $(shell $(DK) ps -a -q) && $(DK) rm $(shell $(DK) ps -a -q)
	$(DK) rmi -f $(shell $(DK) images -q)


