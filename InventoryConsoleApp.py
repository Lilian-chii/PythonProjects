import mysql.connector as mysql
db =mysql.connect (
    host = "localhost",
    user = "root",
    passwd = "3520lil.",
    database = "inventory_management_application")

cursor = db.cursor()

def item_add(product_name, product_description, quantity_in_stock, unit_price, date_added, status ):
    query = "INSERT INTO products2 (product_name, product_description, quantity_in_stock, unit_price, date_added, status) VALUES (%s, %s, %s, %s,%s,%s)"
    values = (product_name, product_description, quantity_in_stock, unit_price, date_added, status)
    cursor.execute(query, values)
    db.commit()
    return cursor.rowcount, "record inserted"


def item_list():
    querry = "SELECT * FROM products2"
    cursor.execute(querry)
    records = cursor.fetchall()
    for record in records:
        print(record)
    return record

def item_remove(product_id):
    query = "DELETE FROM products2 WHERE product_id = " + product_id 
    cursor.execute(query)
    db.commit
    print(f"item record with id {product_id} removed")
    return query


#product_id=(input("Enter the unique id of the product you want to remove: "))
#item_remove(product_id)

#query = "SELECT * FROM products2"
#cursor.execute(query)

#records2 = cursor.fetchall()

#for record in records2:
#print(record)

def compute_asset_value():
    query = "SELECT product_id, product_name, quantity_in_stock*unit_price AS total_assets_value FROM products2 "
    cursor.execute(query)
    db.commit
    records3 = cursor.fetchall()
    for record in records3:
        print(record)
    return query










# Console Layout


application_launcher_options = {
    "1": "item add",
    "2": "item remove",
    "3": "item list",
    "4": "item list export",
    "5": "item checkout",
    "6": "item check in",
    "7": "item view",
    "8": "item search",
    "9": "compute asset value",
    "10": "exit"
    }

def application_commands():
    print ("""Application Commands
    """)
    application_launcher_items = application_launcher_options.items()      
    for item in application_launcher_items:
        print (item)

print("""Inventory Management Application

""")

def log_in():
    count = 0
    while count <3:
        count = count + 1   
        password = input("ENTER PASSWORD TO CONTINUE: ")
        print ("""               
        """)
        if password == "3520lil.":
            application_commands()
            break
        else: 
            print("Incorrect Password")
    else:
        print("You have been denied access to the application") 
                
    

log_in()


def navigation_panel():
    while True: 
        print ("""
             """)
        try:
            option1 = int(input("Enter a command >: "))
            if option1 == 1:
                print("""
                Add a new item
                Enter product details
                """)
                product_name = input("product_name: ")
                product_description = input("product_description: ")
                quantity_in_stock = input("quantity_in_stock: ")
                unit_price = input("unit_price: ")
                date_added = input("date_added: ")
                status = input("status: ")
                print(item_add (product_name, product_description, quantity_in_stock, unit_price, date_added, status ))
            elif option1 == 2:
                print("Remove an item from the inventory")
                product_id=(input("Enter the unique id of the product you want to remove: "))
                item_remove(product_id)
            elif option1 == 3:
                print("Shop Inventory")
                print(item_list())
            elif option1 == 4:
                print("item_list_export")
            elif option1 == 5:
                print("item checkout")
            elif option1 == 6:
                print("item checkin")
            elif option1 == 7:
                print("item view")
            elif option1 == 8:
                print("item search")
            elif option1 == 9:
                print("Total Asset Value")
                compute_asset_value()
            elif option1 == 10:
                break
            else:
                option1 = input("please enter a valid option: ")
        except ValueError:
            print("please enter a valid option")

navigation_panel()







    

