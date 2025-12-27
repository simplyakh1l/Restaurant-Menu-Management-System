from db_config import get_connection

def insert_record():
    con = get_connection()
    cur = con.cursor()
    fid = int(input("Enter Food ID: "))
    fname = input("Enter Food Name: ")
    price = int(input("Enter Price: "))
    rating = float(input("Enter Rating: "))
    dor = input("Enter Date (YYYY-MM-DD): ")
    cur.execute(
        "INSERT INTO menu VALUES (%s,%s,%s,%s,%s)",
        (fid, fname, price, rating, dor)
    )
    con.commit()
    con.close()

def display_records():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM menu")
    for row in cur.fetchall():
        print(row)
    con.close()

def delete_record():
    con = get_connection()
    cur = con.cursor()
    fid = int(input("Enter Food ID to delete: "))
    cur.execute("DELETE FROM menu WHERE fid=%s", (fid,))
    con.commit()
    con.close()

while True:
    print("""
1. Add Record
2. Delete Record
3. Display Records
4. Exit
""")
    ch = int(input("Enter choice: "))
    if ch == 1:
        insert_record()
    elif ch == 2:
        delete_record()
    elif ch == 3:
        display_records()
    else:
        break
