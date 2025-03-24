# CWE-287: Improper Authentication

## Descripción
La vulnerabilidad CWE-287 ocurre cuando una aplicación no verifica adecuadamente la identidad de un usuario antes de concederle acceso a recursos o funcionalidades protegidas. Esto puede llevar a accesos no autorizados y posibles ataques de escalación de privilegios.

Este ejemplo muestra un error en la autenticación dentro de una aplicación Express, donde solo se verifica la existencia del nombre de usuario sin comprobar la contraseña.

## Código de Ejemplo
El archivo `server.js` contiene el siguiente código:

```javascript
const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

function authenticateUser(username, password) {
    return username === 'admin' && password === 'password123';
}

function exitError(res, message) {
    res.status(401).send(message);
}

app.post('/login', (req, res) => {
    if (req.cookies.loggedin !== 'true') {
        const { username, password } = req.body;
        if (!authenticateUser(username, password)) {
            return exitError(res, 'Error: you need to log in first');
        } else {
            res.cookie('loggedin', 'true', { httpOnly: true });
            res.cookie('user', username, { httpOnly: true });
            res.send('Login successful');
        }
    } else {
        res.send('Already logged in');
    }
});

app.get('/admin', (req, res) => {
    if (req.cookies.user === 'Administrator') {
        res.send('Performing administrator tasks');
    } else {
        res.status(403).send('Access denied');
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

```

En el código de ejemplo, basta solo con pasar por cookies el parametro `user=Administrator` para entrar a tareas de administrador, o `loggedin=true` para simular una logueo en el sistema.