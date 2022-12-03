import sys;
class Plant:
    def __init__(self, age = 0, growStatus =""):
        self.age = age
        self.growStatus = growStatus

    def displayListGrowStatus(self):
        print("\nStatus Tanaman")
        list = ["Benih", "Tunas", "Tanaman Kecil", "Tanaman Dewasa", "Berbunga"]    
        for item in range(0, len(list)):
            print("{}. {}".format(item + 1, list[item].capitalize()))
        choice = int(input('Masukkan nomor pilihan status tanaman \t: ')) - 1
        
        if choice <= 0 or choice > (len(list)-1):
            print("berhasil exit" if choice == len(list)-1 else "Pilihan tidak tersedia") 
            sys.exit() 
        else: 
            self.getGrowStatus(choice);
   
    def getGrowStatus(self, growStatus):

        if growStatus == 0:
            self.growStatus = "Benih"
        elif growStatus == 1:
            self.growStatus ="Tunas"
        elif growStatus == 2:
            self.growStatus = "Tanaman Kecil"
        elif growStatus == 3:
            self.growStatus = "Tanaman Dewasa"
        elif growStatus == 4:
            self.growStatus = "Berbunga"
        else:
            self.growStatus = "General"

    def displayPlant(self):
         print("Status Tumbuhan : {}\nUmur Tumbuhan \t: {} Tahun".format(self.growStatus, self.age));

class Anggrek(Plant):
    def __init__(self, age = 0, growStatus= "", color= "", name= ""):

        self.color = color
        self.name = name
        Plant.__init__(self, age, growStatus)
    
    def setAnggrek(self):
        name = input("\nMasukkan nama anggrek \t : ")
        color = input("Masukkan warna anggrek \t : ")
        age = input("Masukkan umur anggrek \t : ")
        self.name = name
        self.color = color
        self.age = age

    def displayAnggrek(self):
        print("\nINFORMASI ANGGREK")
        print("Nama Anggrek \t: {}\nWarna Anggrek \t: {}".format( self.name, self.color))
        self.displayPlant()

class Mawar(Plant):
    def __init__(self, age = 0, growStatus = "", color = "", name = "", isThorny= ""):

        self.color = color
        self.name = name
        self.isThorny = isThorny

        Plant.__init__(self, age, growStatus)
    
    def setMawar(self):
        name = input("\nMasukkan nama mawar \t : ")
        color = input("Masukkan warna mawar \t : ")
        age = input("Masukkan umur mawar \t : ")
        isThorny = input("Apakah batang berduri ? (Yes/No) \t : ")
        self.name = name
        self.color = color
        self.age = age
        self.isThorny = "Berduri" if isThorny == "Yes" else "Tidak Berduri"

    def displayMawar(self):
        print("\nINFORMASI MAWAR")
        print("Nama Mawar \t: {}\nWarna Mawar \t: {}\nBatang \t\t: {}".format( self.name, self.color, self.isThorny))
        self.displayPlant();

class Melati(Plant):
    def __init__(self, age = 0, growStatus = "", color = "", name = "", source= ""):

        self.color = color
        self.name = name
        self.source = source

        Plant.__init__(self, age, growStatus)
    
    def setMelati(self):
        name = input("\nMasukkan nama melati \t : ")
        color = input("Masukkan warna melati \t : ")
        age = input("Masukkan umur melati \t : ")
        source = input("Asal Melati \t : ")
        self.name = name
        self.color = color
        self.age = age
        self.source = source

    def displayMelati(self):
        print("\nINFORMASI MELATI")
        print("Nama Melati \t: {}\nWarna Melati \t: {}\nAsal Melati \t: {}".format( self.name, self.color, self.source))
        self.displayPlant();
        
    
anggrek = Anggrek()
anggrek.displayListGrowStatus();
anggrek.setAnggrek()
anggrek.displayAnggrek();

mawar = Mawar()
mawar.displayListGrowStatus()
mawar.setMawar()
mawar.displayMawar()

melati = Melati()
melati.displayListGrowStatus()
melati.setMelati()
melati.displayMelati()
