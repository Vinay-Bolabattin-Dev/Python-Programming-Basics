import sqlite3

DB_NAME = "contruction_inverntory.db"

def get_all_materials():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, item_name, category, quantity, unit_cost FROM materials")
        return cursor.fetchall()


def add_materials(item_name, category, quantity, unit_cost):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO materials (item_name, category, quantity, unit_cost)
            VALUES (?, ?, ?, ?)
        """, (item_name, category, quantity, unit_cost))
        return True 


def Update_stock(item_id, new_quantity):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE materials
            SET quantity = ?
            WHERE id = ?
        """, (new_quantity, item_id))
        return cursor.rowcount > 0


def delete_material(item_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM materials WHERE id = ?", (item_id,))
        return cursor.rowcount > 0


if __name__ == "__main__":
    print("---- 1. Testing add_materials() ----")
    add_materials("Safety Helmets", "Safety", 50, 250)
    print("Added 'Safety Helmets'")

    print('\n---- 2. Testing get_all_materials() ----')
    materials = get_all_materials()
    for item in materials:
        print(item)

    print("\n---- 3. Testing update_stock() ----")
    if Update_stock(1, 150):
        print("Stock updated successfully for ID 1")

    print('\n---- 4. Testing delete_material() ----')
    for m in get_all_materials():
        if m[1] == "Safety Helmets":  # Fixed: removed trailing space
            if delete_material(m[0]):
                print(f"Deleted 'Safety Helmets' (ID {m[0]}) successfully!")