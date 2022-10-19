import psycopg2
from tkinter import *

Text = "Please log in"

logged_in = False

root = Tk()
root.geometry('200x400')

con = psycopg2.connect(
    host="",
    database="",
    user="",
    password="")

cur = con.cursor()


def register():
    holder = entry1.get()
    password = entry2.get()

    cur.execute(
        'INSERT INTO account (holder, password, balance) VALUES ({0}, {1}, 0);'.format("'" + holder + "'",
                                                                           "'" + password + "'"))
    con.commit()


    con.commit()
    print("Done")


def login():
    holder = entry3.get()
    password = entry4.get()

    cur.execute('SELECT COUNT(id) FROM account WHERE holder = {0} AND password = {1};'.format("'" + holder + "'",
                                                                                              "'" + password + "'"))
    row = cur.fetchall()

    if row == [(1,)]:
        print("logged in")
        print(row)
        succes = "Succesfully logged in."
        label.config(text=succes)
        global logged_in
        logged_in = True
        get_balance(holder)
    else:
        print("Incorrect credentials!")
        print(row)
        succes = "Incorrect credentials!"
        label.config(text=succes)


def send_money():
    if logged_in:
        holder = entry3.get()
        amount = entry5.get()
        to = entry6.get()
        from_ = entry3.get()
        query = """
            INSERT INTO transaction (from_id, to_id, amount) VALUES( (SELECT id FROM account WHERE holder = '{}') , (SELECT id FROM account WHERE holder = '{}'), {});
            """.format(from_, to, amount)
        query3 = """UPDATE account SET balance = (SELECT balance FROM account WHERE holder = '{}') + {} WHERE holder = '{}';""".format(to, amount, to)
        query4 = """UPDATE account SET balance = (SELECT balance FROM account WHERE holder = '{}') - {} WHERE holder = '{}';""".format(holder, amount, holder)

        print(query)
        print(query3)
        cur.execute(query)
        cur.execute(query3)
        cur.execute(query4)
        con.commit()
        get_balance(holder)


entry1 = Entry(root, width=20)
entry1.pack()

entry2 = Entry(root, width=20)
entry2.pack()

Button(root, text="Register", command=register).pack()

entry3 = Entry(root, width=20)
entry3.pack()

entry4 = Entry(root, width=20)
entry4.pack()

Button(root, text="Login", command=login).pack()

label = Label(root, text=Text)
label.pack()

balance = 0





sp = Label(root, text="").pack()
amount_lb = Label(root, text="Amount").pack()
entry5 = Entry(root, width=20)
entry5.pack()
to_label = Label(root, text="To").pack()
entry6 = Entry(root, width=20)
entry6.pack()

send_button = Button(text="Send", command=send_money)

send_button.pack()
# bal = Label(text="Balance").pack()
bal = Label(text=balance)
bal.pack()
def get_balance(holder):
    global balance
    query = "SELECT balance FROM account WHERE holder = '{}';".format(holder)
    cur.execute(query)
    balance = cur.fetchall()
    print(balance)
    bal.config(text=balance)
root.mainloop()

cur.execute('SELECT * FROM account')

rows = cur.fetchall()

for r in rows:
    print(f"id: {r[0]} holder: {r[1]} password: {r[2]}")

cur.close()
con.close()
