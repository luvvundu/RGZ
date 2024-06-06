import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="rgz_vikcha",
    user="vika",
    password="postgres"
)

with conn.cursor() as cur:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id SERIAL PRIMARY KEY,"
        "chat_id BIGINT NOT NULL,"
        "name VARCHAR(50) NOT NULL)"
    )

    cur.execute(
        "CREATE TABLE IF NOT EXISTS operations ("
        "id SERIAL PRIMARY KEY,"
        "date DATE NOT NULL,"
        "sum NUMERIC(10, 2) NOT NULL,"
        "chat_id BIGINT NOT NULL,"
        "type_operation VARCHAR(50) NOT NULL,"
        "comment TEXT)"
    )
    conn.commit()
