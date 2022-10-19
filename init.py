import psycopg2

con = psycopg2.connect(
    host="",
    database="",
    user="",
    password="")

cur = con.cursor()

query1 =  """CREATE TABLE account (id SERIAL PRIMARY KEY, holder VARCHAR(100), password TEXT, balance NUMERIC(10));"""
query2 = """create table transaction(id SERIAL PRIMARY KEY, from_id INT, to_id INT, amount numeric(10, 2), CONSTRAINT from_user FOREIGN KEY(from_id) REFERENCES account(id), CONSTRAINT for_user FOREIGN KEY(to_id) REFERENCES account(id));"""

cur.execute(query1)
con.commit()
cur.execute(query2)
con.commit()

cur.close()
con.close()
