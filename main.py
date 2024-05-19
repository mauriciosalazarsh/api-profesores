from fastapi import FastAPI
from schemas import Professor
import mysql.connector

app = FastAPI()

db_config = {
    "host": "100.27.52.36",
    "port": 8005,
    "user": "root",
    "password": "utec",
    "database": "api_profesores"
}

@app.post("/profesores")
def add_professor(professor: Professor):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO profesores (nombre, apellido, título, especialidad) VALUES (%s, %s, %s, %s)"
    val = (professor.nombre, professor.apellido, professor.título, professor.especialidad)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Professor added successfully"}

@app.get("/profesores")
def get_professors():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesores")
    professors = cursor.fetchall()
    conn.close()
    return {"professors": professors}

@app.get("/profesores/{id}")
def get_professor(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesores WHERE id = %s", (id,))
    professor = cursor.fetchone()
    conn.close()
    return {"professor": professor}

@app.put("/profesores/{id}")
def update_professor(id: int, professor: Professor):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "UPDATE profesores SET nombre=%s, apellido=%s, título=%s, especialidad=%s WHERE id=%s"
    val = (professor.nombre, professor.apellido, professor.título, professor.especialidad, id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Professor updated successfully"}

@app.delete("/profesores/{id}")
def delete_professor(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profesores WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return {"message": "Professor deleted successfully"}
