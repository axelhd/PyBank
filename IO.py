import psycopg2

con = psycopg2.connect(
    host="",
    database="",
    user="",
    password="")

balance = int(input("Balance for account: "))
holder = input("Account to update: ")
password_prompt = input("Password for changing balances: ")
password = "your_password"

cur = con.cursor()
if password_prompt == password:
    query1 = """UPDATE account SET balance = {} WHERE holder = '{}';""".format(balance, holder)
    cur.execute(query1)
    con.commit()

cur.close()
con.close()
