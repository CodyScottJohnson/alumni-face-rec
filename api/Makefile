python-grpc:
	python -m grpc_tools.protoc -I. --proto_path=proto/v1 --python_out=./pkg/v1/python --grpc_python_out=./pkg/v1/python face_rec.proto
go-grpc:
	protoc --proto_path=proto/v1 --go_out=plugins=grpc:pkg/go/v1 face_rec.proto