import pika
import json
import os
import glob
import pathlib
import sys

dir_path = ""

def list_files(dir_path, pattern="*", limit=None):
    files = list(map(lambda p: str(p), pathlib.Path(dir_path).glob("**/" + pattern)))
    if limit < 1:
        return str(json.loads(json.dumps(files)))
    else:
        return str(json.loads(json.dumps(files[:limit])))

def on_request(ch, method, props, body):
    msg = json.loads(body)
    serv = msg["service"]
    limit = int(msg["limit"])

    if limit == None:
        limit = 0
    else: 
        limit = int(limit)

    response: str
    if serv == "list":
        response = list_files(dir_path=dir_path, limit=limit)
    else:
        response = list_files(dir_path=dir_path, pattern=msg["file"], limit=limit)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main(argv):
    if len(argv) == 2:
        config_path = argv[1]
        config = json.load(open(config_path, 'r'))

        dir_path = config['dir_path']

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config['host']))
        
        channel = connection.channel()
        
        channel.queue_declare(queue='rpc_server_queue')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_server_queue', on_message_callback=on_request)
        
        print(" [x] Awaiting RPC requests")
        channel.start_consuming()

if __name__ == '__main__':
    main(sys.argv)
