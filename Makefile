run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py search_index --rebuild

up:
	docker-compose.exe -f ./docker-compose.dev.yaml up -d

down:
	docker-compose -f ./docker-compose.dev.yaml down