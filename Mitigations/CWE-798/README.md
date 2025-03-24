		
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

En este caso, si el atacante da con el código fuente, no podrá hacer mucho ya que las credenciales están almacenadas en el entorno de ejecución y no propiamente en el código.