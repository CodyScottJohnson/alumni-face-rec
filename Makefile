dev-build:
	docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml build

dev:
	cp api/pkg/python/* python/face-rec/grpc
	docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml up 
prod-build:
	docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml build

prod:
	docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml up 
test:
	./python-tests.sh
proto:
	cp api/pkg/python/* python/face-rec/grpc
