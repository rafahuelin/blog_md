up:
	docker-compose up

down:
	docker-compose down

downup:
	docker-compose down
	docker-compose up

build:
	docker-compose build --force-rm --no-cache && docker-compose up --detach && docker-compose logs -f