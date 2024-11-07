const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./database/shopping.db', (err) => {
    if (err) {
        console.error('Error connecting to SQLite:', err);
        return;
    }
    console.log('Connected to the SQLite database');
});

db.run(`
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        Preço REAL NOT NULL,
        description TEXT,
        imageURL TEXT
    );
`);

module.exports = db;
