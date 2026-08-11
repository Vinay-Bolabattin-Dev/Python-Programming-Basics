import sqlite3

db_name="contruction_inverntory.db"

with sqlite3.connect(db_name) as conn :
    cursor= conn.cursor()
    cursor.execute("SELECT item_name, quantity FROM materials WHERE id =1 ")
    item , original_qty=cursor.fetchone()
    print(f" BEFORE TRANSECTION : {item} has quantity ={original_qty}")

print("="*50)


try:
    with sqlite3.connect(db_name)as conn:
        cursor=conn.cursor()

        print("2 Attemting to update quantity to 999....")
        cursor.execute("UPDATE materials SET quantity = 999 WHERE id=1")

        print("Intenstional Error occurring: Dividing by Zero !! ")
        crash= 10/0

except Exception as e:
    print(f" Caught expecated error : {e}")
    print("Context Manger Automatically Triggered ROLLBACK ! ")


print("-"*50)

with sqlite3.connect(db_name) as conn :
    cursor = conn.cursor()
    cursor.execute("SELECT item_name, quantity FROM materials WHERE id = 1")
    item, final_qty = cursor.fetchone()
    print(f"3. AFTER CRASH & ROLLBACK: {item} has quantity = {final_qty}")

if final_qty == original_qty:
    print("\n✅ SUCCESS: Rollback worked! Database remained completely uncorrupted!")