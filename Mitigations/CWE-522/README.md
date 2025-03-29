# CWE-522 Insufficiently Protected Credentials
## Descripción
El producto transmite o almacenas credenciales de autenticación, pero utiliza un método inseguro que es susceptible a una intercepción y o recuperación.
![alt text](../../Weaknesses/CWE-522/image.png)

## Pasos de ejecución
La aplicación de ejemplo se puede ejecutar de la siguiente manera:

```bash
docker-compose up --build
```
Iniciada la aplicación se desplegaran un contenedor exponiendo una aplicación web por el puerto 5000.
Utilize su navegador para acceder a `http://localhost:5000/get-credentials`


En esta versión, las claves de aplicación no están en un archivo dentro del proyecto, sino que más bien hacen parte del entorno de ejecución.
```yaml
# Base image
FROM python:3.9

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

ENV API_USERNAME=admin
ENV API_PASSWORD=admin


EXPOSE 5000

CMD ["python", "server.py"]
```