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

countPPN();