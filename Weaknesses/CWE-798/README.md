		
# CWE-798: Use of Hard-coded Credentials

## Descripción
El producto contiene credenciales hard codeadas, como contraseña y claves criptográficas.

## Pasos de ejecución 

Construye los servicios ejecutando
```bash
// Construcción del servicio
docker-compose up --build
```
Una vez los servicios arranquen, revisa como el cliente estará enviando solicitudes cada 5s al servidor.

Revisa como si un atacante logra acceder o descargar el firmware de la aplicación, podrá simular peticiones del propio dispositivo, gracias a la obtención de las credenciales hardcodeadas. 