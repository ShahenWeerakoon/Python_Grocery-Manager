from sql_connection import get_sql_connection
import mysql.connector

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("""
    SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name
    FROM products
    INNER JOIN uom ON products.uom_id = uom.uom_id
    """)

    cursor.execute(query)
    response = []

    for products_id, name, uom_id, price_per_unit, uom_name in cursor:
        response.append(
            {
                'products_id': products_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    cursor.close()
    return response

def insert_new_product(connection, products):
    cursor = connection.cursor()
    query = ("INSERT INTO PRODUCTS "
             "(name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (products['product_name'], products['uom_id'], products['price_per_unit'])
    

    cursor.execute(query, data)
    connection.commit()
    

    return cursor.lastrowid

def delete_product(connection, products_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE products_id = %s")
    data = (products_id,)
    
    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    return products_id

if __name__ == '__main__':
    connection = get_sql_connection()

    
    deleted_product_id = delete_product(connection, 16)
    print(f"Deleted product ID: {deleted_product_id}")

    connection.close()
    
   
