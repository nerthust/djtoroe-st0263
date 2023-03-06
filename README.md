# Materia: ST0263 Tópicos especiales en telemática 

# Estudiante: Danilo de Jesus Toro Echeverri - djtoroe@eafit.edu.co

# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Reto 2 - Procesos comunicantes por API REST, RPC y MOM

# 1. breve descripción de la actividad

El sistema ofrece dos micro-servicios a una API Gateway sirviendo como proxy en frente de los dos servicios. Los micro-servicios hacen uso de dos diferentes middleware, uno de ellos es GRPC y otro MOM usando RabbitMQ. Los servicios ofrecidos son listar todos los archivos existentes o listar los archivos que coincidan con un patron suministrado.

## 1.1. Requerimeintos

- Implementar un micro-servicio en GRPC.
- Implementar un micro-servicio con RabbitMQ queues.
- La API Gateway implementa un REST API en Json.
- Todos los nodos cargan la configuracion desde un archivo Json.
- Proveer el mismo servicio de listar archivos o buscar archivos con un patron dado.
- Los tres servicios soportan concurrencia.

Todos los requerimientos en el laboratorio fueron desarrollados.

# 2. Arquitectura.

El sistema va intercambiando entre Modo GRPC y Modo MOM. 

Cuando se encuentra en modo GRPC  va directamente a la API Gateway, que genera el formato binario proto-buffer específico para hacer la solicutud al servidor GRPC. Este mensaje proto-buffer se envía al microservicio que deserializa el mensaje y procesa la solicitud. Una vez el servidor genera la respuesta, se la envia a la API Gateway que a su vez deserializa la respuesta.

Cuando se encuentra en modo MOM la petición se envía a una cola de peticiones de RabbitMQ co un id unico generado. El servidor MOM esta constantemente revisando el estado de la cola, para encontrar nuevas peticiones. Una vez procesada, el servidor MOM serializa la respuesta y la envía a la cola de respuestas. El cliente MOM compara el id de la respuesta para confirmar que coincida con un id de peticion antes realizada. Si ambos ids coinciden, significa que el mensaje corresponde a la respuesta para la petición inicial.

# 3. Ambiente de desarrollo
# 3.1 Dir Tree
![alt text](https://github.com/nerthust/djtoroe-st0263/blob/main/assets/screen.png)
# 3.2 Lenguaje de programacion
EL lenguaje usado fue Python 3.10.

Las librerias usadas son:
```
uvicorn==0.20.0
grpcio-tools==1.51.3
grpcio==1.51.3
pika==1.3.1
```
# 3.3 Configuracion de servidores

## API Gateway
`api_gateway.py`
```
{
"host": "localhost",
"port": 50051
}
```
## Servidor GRPC
`grpc_server.py`
```
{
  "port": 50051,
  "max_workers": 10,
  "dir_path": "absolute/path/to/assets/dir"
 }
```
## Servidor MOM
`rpc_server.py`

```
{
  "host" = "localhost"
  "dir_path": "absolute/path/to/assets/dir"
 }
```

# 4. Ejecucion
En el repositorio se encuentra el archivo `build.sh` el cual se encarga de:
Instalar las depedencias necesarias para el trabajo.

![alt text](https://github.com/nerthust/djtoroe-st0263/blob/main/assets/libraries.png)

En otra seccion, inicializa cada uno de los servicios.
![alt text](https://github.com/nerthust/djtoroe-st0263/blob/main/assets/screen.png)


Para ejecutar el trabajo se usa el siguiente comando:

```
./build.sh
```


# 5. referencias:
- https://www.rabbitmq.com/tutorials/tutorial-six-python.html
- https://www.uvicorn.org/
- https://grpc.io/docs/languages/python/basics/
