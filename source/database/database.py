import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="natura-sale-base-datos-nature-sale.k.aivencloud.com",    
        user="avnadmin",      
        password="AVNS_0w9Ehs191pN4lT79WxM",
        database="defaultdb",
        port= "16992"
    )
