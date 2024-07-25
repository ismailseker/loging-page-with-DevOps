import mysql.connector

# MySQL veritabanı bağlantısı için gerekli bilgiler
config = {
    'user': 'root',
    'password': 'CSGO123abcDf.',
    'host': 'localhost',  # MySQL Workbench ile aynı makinede çalışıyorsanız 'localhost'
    'database': 'flaskData',
    'raise_on_warnings': True
}

try:
    # Bağlantıyı kur
    cnx = mysql.connector.connect(**config)

    # Bir cursor oluştur
    cursor = cnx.cursor()

    # Bir sorgu çalıştır
    query = "SELECT id, username, email, created_at FROM users"
    cursor.execute(query)

    # Sonuçları al ve yazdır
    for (id, username, email, created_at) in cursor:
        print(f"ID: {id}, Username: {username}, Email: {email}, Created At: {created_at}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Bağlantıyı kapat
    cursor.close()
    cnx.close()
