const express = require('express');
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt');
const crypto = require('crypto');
const helmet = require('helmet');
const session = require('express-session');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// Simulated database 
const users = {
    admin: {
        username: 'admin',
        passwordHash: bcrypt.hashSync('admin', 10), // Hashed password
        role: 'admin'
    }
};

// Secure session configuration
app.use(session({
    secret: crypto.randomBytes(64).toString('hex'), 
    resave: false,
    saveUninitialized: false,
    cookie: {
        httpOnly: true,
        sameSite: 'Strict',
        maxAge: 1000 * 60 * 15
    }
}));

// Function to authenticate user
function authenticateUser(username, password) {
    const user = users[username];
    return user && bcrypt.compareSync(password, user.passwordHash);
}

// Authentication middleware
function requireAuth(req, res, next) {
    if (!req.session.user) {
        return res.status(401).send('Error: Authentication required');
    }
    next();
}

// Admin authorization middleware
function requireAdmin(req, res, next) {
    if (!req.session.user || req.session.role !== 'admin') {
        return res.status(403).send('Error: Access denied');
    }
    next();
}

// Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (!authenticateUser(username, password)) {
        return res.status(401).send('Error: Invalid credentials');
    }

    // Set session on the server
    req.session.user = username;
    req.session.role = users[username].role;
    res.send('Login successful');
});

// Logout route
app.post('/logout', (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.status(500).send('Error logging out');
        }
        res.send('Session successfully closed');
    });
});

// Protected route for admins only
app.get('/admin', requireAuth, requireAdmin, (req, res) => {
    res.send('Performing administrator tasks');
});

app.listen(3000, () => {
    console.log('Secure server running on port 3000');
});
