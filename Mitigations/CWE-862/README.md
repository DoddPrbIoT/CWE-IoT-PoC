# CWE-862 – Missing authorization 

## Descripción
El producto no realiza una comprobación de autorización cuando un actor intenta acceder a un recurso o realizar una acción.

## Pasos de ejecución 

Construye los servicios ejecutando
```bash
// Construcción del servicio
docker-compose up --build
```

En este caso para que el atacante logre una ejecución remota de los servicios, es necesario que se haya autenticado con credenciales válidas. 

```python
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad credentials"}), 401
```
Esto le otorgará un token de autorización que le permitirá realizar consultas.

```python
@app.route('/api/device/on', methods=['POST'])
@jwt_required()
def turn_on_device():
    device_status["on"] = True
    return jsonify({"message": "Device turned ON!"}), 200
```

**Petición de token**
```
curl -X POST "http://localhost:5000/api/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "admin"}'

```

**Petición activación de dispositivos**
```
curl -X POST "http://localhost:5000/api/device/on" \
     -H "Authorization: Bearer ACCESS_TOKEN"

```