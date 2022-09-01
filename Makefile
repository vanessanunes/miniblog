
run:
	uvicorn app.main:app --port 3813 --reload

run-docker:
	sudo docker-compose up -d

migrate:
	alembic upgradehead
