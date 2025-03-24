# CWE - IoT Weaknesses - PoC

Repositorio de Prueba de Concepto (PoC) del proyecto **Internet de las Cosas, lo que conocemos y no acerca de las vulnerabilidades y riesgos más comunes en estos sistemas**

## Herramientas
* WireShark
* Docker
* Python

## Estructura
.
├── Mitigations
│   ├── CWE-22
│   │   ├── configs
│   │   │   └── sensor.conf
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── app.py
│   ├── CWE-287
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   └── server.js
│   ├── CWE-311
│   │   ├── client
│   │   │   ├── Dockerfile
│   │   │   ├── client.py
│   │   │   └── ssl.crt
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── server.py
│   │   │   ├── ssl.crt
│   │   │   ├── ssl.csr
│   │   │   └── ssl.key
│   │   ├── README.md
│   │   ├── docker-compose.yml
│   │   ├── image-1.png
│   │   ├── image-2.png
│   │   ├── image.png
│   │   └── san.cnf
│   ├── CWE-319
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── cert.pem
│   │   │   ├── key.pem
│   │   │   └── server.py
│   │   ├── README.md
│   │   ├── cert.pem
│   │   ├── client.py
│   │   ├── docker-compose.yml
│   │   ├── image-1.png
│   │   ├── image-2.png
│   │   ├── image-3.png
│   │   ├── image-4.png
│   │   ├── image-5.png
│   │   ├── image-6.png
│   │   └── image.png
│   ├── CWE-522
│   │   ├── app
│   │   │   ├── __pycache__
│   │   │   │   └── config.cpython-311.pyc
│   │   │   ├── config.py
│   │   │   ├── requirements.txt
│   │   │   └── server.py
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── docker-compose.yml
│   ├── CWE-787
│   │   ├── client
│   │   │   └── Dockerfile
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   └── server.c
│   │   ├── README.md
│   │   └── docker-compose.yml
│   ├── CWE-798
│   │   ├── iot-device
│   │   │   ├── Dockerfile
│   │   │   ├── device.py
│   │   │   └── requirements.txt
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── app.py
│   │   │   └── requirements.txt
│   │   ├── README.md
│   │   └── docker-compose.yml
│   └── CWE-862
│       ├── attacker
│       │   ├── Dockerfile
│       │   └── attacker.py
│       ├── server
│       │   ├── Dockerfile
│       │   └── server.py
│       ├── README.md
│       ├── docker-compose.yml
│       ├── image-1.png
│       ├── image.png
│       └── requirements.txt
├── Weaknesses
│   ├── CWE-22
│   │   ├── configs
│   │   │   └── sensor.conf
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── app.py
│   ├── CWE-287
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   └── server.js
│   ├── CWE-311
│   │   ├── client
│   │   │   ├── Dockerfile
│   │   │   └── client.py
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   └── server.py
│   │   ├── README.md
│   │   ├── docker-compose.yml
│   │   ├── image-1.png
│   │   ├── image-2.png
│   │   └── image.png
│   ├── CWE-319
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── cert.pem
│   │   │   ├── key.pem
│   │   │   ├── secure_server.py
│   │   │   └── server.py
│   │   ├── README.md
│   │   ├── cert.pem
│   │   ├── client.py
│   │   ├── docker-compose.yml
│   │   ├── image-1.png
│   │   ├── image-2.png
│   │   ├── image-3.png
│   │   ├── image.png
│   │   └── secure_client.py
│   ├── CWE-522
│   │   ├── app
│   │   │   ├── config.py
│   │   │   ├── requirements.txt
│   │   │   └── server.py
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── docker-compose.yml
│   ├── CWE-787
│   │   ├── client
│   │   │   └── Dockerfile
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── secure_server.c
│   │   │   └── server.c
│   │   ├── README.md
│   │   └── docker-compose.yml
│   ├── CWE-798
│   │   ├── iot-device
│   │   │   ├── Dockerfile
│   │   │   ├── device.py
│   │   │   └── requirements.txt
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── app.py
│   │   │   └── requirements.txt
│   │   ├── README.md
│   │   └── docker-compose.yml
│   └── CWE-862
│       ├── attacker
│       │   ├── Dockerfile
│       │   └── attacker.py
│       ├── server
│       │   ├── Dockerfile
│       │   └── server.py
│       ├── README.md
│       ├── docker-compose.yml
│       ├── image-1.png
│       └── image.png
├── README.md
└── directories.md

41 directories, 129 files
