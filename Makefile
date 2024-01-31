help:
	@echo "Cereal Shop Makefile help"
	@echo "--------------------------"
	@echo "  make install        - Install dependencies"
	@echo "  make setup-data     - Set up data on database"
	@echo "  make run            - Run the application"
	@echo "  make test           - Run tests"
	@echo "  make docker-build   - Build application Docker image"
	@echo "  make docker-run     - Run application using Docker on port 8000"
	@echo "  make docker-clean   - Stop and remove Docker container and image"
	@echo "  make docker-up      - Build and run Docker container"
	@echo "  make docker-restart - Stop, remove, rebuild, and run Docker container"
	@echo "  make docker-test    - Run tests inside the Docker container"

install:
	pip install -r src/config/requirements.txt

setup-data:
	python -m src.config.scripts.setup_data

run: setup-data
	uvicorn src.main:app --port 8000

test: setup-data
	pytest

docker-build:
	docker build -t cereal-shop .

docker-run:
	docker run --name cereal-shop -p 8000:8000 cereal-shop 

docker-clean:
	docker stop cereal-shop
	docker rm cereal-shop
	docker rmi cereal-shop

docker-up: docker-build docker-run

docker-restart: docker-clean docker-up

docker-test:
	docker exec -it cereal-shop pytest