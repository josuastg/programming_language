
# UTS PBO

### PARADIGMA PEMROGRAMAN
Merupakan dasar dari memahami bahasa pemrograman, mulai dari pola desain bahasa pemrograman, gaya, pendekatan sehingga dapat mengurangi kompleksitas dari sebuah program sehingga dapat menyelesaikan masalah-masalah yang ada.
Paradigma Pemrograman juga sebagai sudut pandang untuk mengelompokkan bahasa pemrograman berdasarkan kemampuannya.

### PEMROGRAMAN BERORIENTASI OBJEK
Pemrograman Berorientasi Objek merupakan salah satu paradigma bahasa pemrograman yang perlu dipahami, mulai dari menyelesaikan suatu masalah yang ada dengan berorientasi objek. 
Objek ini akan terdiri dari atribut dan fungsi-fungsi yang berkaitan. Kemudian Objek ini akan dibungkus kedalam suatu kelas.

### PROGRAM QUIZ
```python
print("================")
print("PROGRAM QUIZ")
print("================")

def inputProgramQuiz():
    name = input('masukkan nama \t: ')
    nim = input('masukkan nim \t: ')
    # print data
    print("======= RESULT =========")
    print('Nama \t: {} '.format(name))
    print('NIM \t: {} '.format(nim))

inputProgramQuiz()

```
### PERBEDAAN LOOPING DENGAN CONTINUE DAN BREAK
Jika looping menggunakan continue, ketika kondisi bernilai true maka akan dilewatkan atau tidak dieksekusi action dalam mencetak huruf tersebut kemudian lanjut lagi ke loopingan berikutnya
Sedangkan break ketika kondisi bernilai true maka akan menghentikan proses loopingnya dan hanya dapat mencetak huruf sebelum huruf h.


### PROGRAM MENGHITUNG PPN

```python
import sys;

def countPPN():
    name = input('NIM \t: ')
    nim = input('NAMA \t: ')
    list = ["capucino", "teh", "exit"]
    #looping variable list 
    for item in range(0, len(list)):
        print("{}. {}".format(item + 1, list[item].capitalize()));
    # variable choice sebagai indikator pemilihan menu
    choice = int(input('masukkan pilihan \t: ')) - 1
    # kondisi ketika yang dipilih tidak ada atau pilih exit maka akan memberhentikan program tetapi jika ada maka menampilkan pilihan 
    if choice <= 0 or choice >= (len(list)-1):
        print("berhasil exit" if choice == len(list)-1 else "Pilihan tidak tersedia") 
        sys.exit() 
    else: 
        print("memilih {}".format(list[choice].upper()))
    # Perhitungan PPN berdasarkan inputan harga minuman dari user 
    price = int(input('masukkan harga \t: ' ))
    ppn = int(price * 0.1)
    result = int(price + ppn)
    print(result);

countPPN()
```
### CLASS WAKTU BESERTA VALIDASI JAM, WAKTU, dan DETIK

```python
class Waktu:
    
    def __init__(self, jam = 0, menit = 0, detik = 0):
        self.jam = jam
        self.menit = menit
        self.detik = detik
    
    def validateJam(self, jam):
        if(jam >= 0 and jam < 24):
            if(jam < 10):
              self.jam = "0"+ str(jam)
            else:
                self.jam = jam
            return True     
        else:
            return False
        

    def validateMenit(self, menit):
        if(menit >= 0 and menit < 60):
            if(menit == 0 or menit < 10):
              self.menit = "0"+ str(menit)
            else:
                self.menit = menit 
            return True     
        else:
            return False
     
    def validateDetik(self, detik):
        if(detik >= 0 and detik < 60):
            if(detik < 10):
              self.detik = "0"+ str(detik)
            else:
              self.detik = detik 
            return True     
        else:
            return False

    def displayWaktu(self):
        jam = int(input('masukkan jam \t: '))
        menit = int(input('masukkan menit \t: '))
        detik = int(input('masukkan detik \t: '))
        if self.validateJam(jam) and self.validateMenit(menit) and self.validateDetik(detik):
            print("{} : {} : {}" .format(self.jam, self.menit, self.detik))
        else:
            print('salah memasukkan jam atau menit atau detik!!!')

waktu = Waktu()
waktu.displayWaktu()

```