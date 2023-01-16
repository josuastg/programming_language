import mysql.connector

mydb = mysql.connector.connect(
  host="172.17.3.187", #based on your ip (localhost)
  port=13306,
  user="root",
  password="p455w0rd",
  database = "vehicle"
)

db = mydb.cursor()

def insertCar():
    print("=== MASUKKAN DATA MOBIL ===")
    name = input("Masukkan Merk Mobil Anda \t: ")
    color = input("Masukkan Warna Mobil Anda \t: ")
    try:
        sql = "INSERT INTO car (name,color) VALUES (%s, %s)"
        value = (name, color)
        db.execute(sql, value)
        mydb.commit()
        print(db.rowcount, "BERHASIL INSERT")
    except:
        print("TIDAK BERHASIL INSERT")

def showCar():
    print("LIST MOBIL")
    db.execute("SELECT * from car")
    res = db.fetchall()

    if res:
        for car in res:
            print(car)
    else:
        print("Data tidak tersedia")

def chooseMenu():
    print("Masukkan angka 1 atau 2 untuk menjalankan menu dibawah ini : ")
    print("1. Masukkan Data Mobil")
    print("2. Lihat Data Mobil")
    menu = int(input("Masukkan angka \t: "))
    if menu == 1:
        insertCar()
    elif menu == 2:
        showCar()
    else:
        print("Menu tidak tersedia atau salah memasukkan pilihan")

chooseMenu()
