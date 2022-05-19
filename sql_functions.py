import psycopg2 as pg2

def connect_db():
    conn = pg2.connect(host = 'localhost',
                       database = 'scuba_team',
                       user = 'postgres',
                       password = 'postgres')

    return conn

def create_db(sql):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def query_db(sql):
    """Retorna as consultas (queries) no banco de dados."""

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registry = [reg for reg in recset]

    conn.close()

    return registry

def insert_db(sql):
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except (Exception, pg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
        cur.close()
        return 1
    
    cur.close()
