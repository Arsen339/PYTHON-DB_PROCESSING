import sqlite3 as sq

# Контекстный менеджер автоматически закроет базу, даже если произошла ошибка
with sq.connect("Saper.db") as con:
    cur = con.cursor()  # метод для выполнения запросов
    cur.execute("""CREATE TABLE IF NOT EXISTS users
    (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL,
    old INTEGER,
    score INTEGER)
    
    """)
    cur.execute("""
    INSERT INTO users VALUES 
    (NULL, "Николай", 1, 26, 2220)
    """)
