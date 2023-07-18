* `pip3 install grpcio`
* `pip3 install grpcio-tools`
* `python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. reporting.proto`
* `python3 reporting_server.py`
* `python3 reporting_client.py 17 45 40.0409 −29 00 28.118`
