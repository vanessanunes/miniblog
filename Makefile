
run:
	uvicorn "app.main:app" --reload

run-docker:
	sudo docker-compose up
