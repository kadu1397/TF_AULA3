import psycopg2
from psycopg2 import sql
import json

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="northwind",
            user="testeTf",
            password="faat",
            host="localhost",
            port="2000"
        )
        print("Connection to database established successfully")
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None
    
def get_alunos():
    connection = connect_to_db()
    if connection is None:
        return json.dumps({"error": "Failed to connect to the database"})

    try:
        cursor = connection.cursor()
        query = sql.SQL("SELECT alunos_id, alunos_name, alunos_idade,  FROM alunos")
        cursor.execute(query)
        rows = cursor.fetchall()
        alunos = []
        for row in rows:
            alunos.append({
                "alunos_id": row[0],
                "alunos_name": row[1],
                "alunos_id": row[2],
                
            })
        return json.dumps(alunos)
    except Exception as error:
        print(f"Error fetching data: {error}")
        return json.dumps({"error": "Failed to fetch data"})
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    print(get_alunos())