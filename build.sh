#!/bin/bash
        
sudo apt install python3
sudo apt install -y python3-pip
pip install uvicorn
pip install grpcio
pip install grpcio-tools
pip3 install glob2
pip install fastapi
pip install pika

export PATH="/home/ubuntu/.local/bin:$PATH"
yes Y | sudo apt-get install rabbitmq-server

sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo service nginx start
python3 ./service-grpc/grpc_server.py /home/ubuntu/djtoroe-st0263/service-grpc/config.json &
python3 ./service-mom/rpc_server.py /home/ubuntu/djtoroe-st0263/service-mom/config.json &
cd gateway
python3 -m uvicorn api_gateway:app &
