

class Plant():
    def __init__(self, name = "", price = "Rp 0", statusTumbuh = 0, jumlahAir = 0, jumlahPupuk = 0, 
    jumlahTanaman = 0):
        self.name = name
        self.price = price
        self.statusTumbuh = statusTumbuh
        self.jumlahAir = jumlahAir
        self.jumlahPupuk = jumlahPupuk
        self.jumlahTanaman = jumlahTanaman

    def beriAir(self):
        self.jumlahAir+=1
        self.cekKondisiTumbuh()
    
    def beriPupuk(self):
        self.jumlahPupuk+=1
        self.cekKondisiTumbuh()
    
    def cekKondisiTumbuh(self):
        if self.jumlahAir >= 3 and self.jumlahPupuk >= 1:
            self.tumbuh()

    def tumbuh(self):
        if self.statusTumbuh < 4:
            self.jumlahAir-= 3
            self.jumlahPupuk-= 1
            self.statusTumbuh+=1

    def getStatusTumbuhText(self):
        self.statusTumbuh = int(self.statusTumbuh) 
        if self.statusTumbuh == 0:
            return "Benih"
        elif self.statusTumbuh == 1:
            return "Tunas"
        elif self.statusTumbuh == 2:
            return "Tanaman Kecil"
        elif self.statusTumbuh == 3:
            return "Tanaman Dewasa"
        elif self.statusTumbuh == 4:
            return "Berbunga"
        else:
            return "General"

    def getStatusTumbuh(self):
        return self.statusTumbuh
    
    def reducePlant(self, amount):
        self.jumlahTanaman -=amount
    
    def displayPlant(self):
        print("\n")
        print("Status Tanaman : {}".format(self.getStatusTumbuhText()))
        print("Nama Tanaman : {}".format(self.name))
        print("Harga Tanaman : {}".format(self.price))
        print("Jumlah Tanaman {}: {}".format(self.name, self.jumlahTanaman))
    

        
class Garden():
    def __init__(self, 
    SIZE = 10, 
    nTanaman = 0, 
    mGardenName = "", 
    pArrList = Plant([]), 
    hasilPanen = 0):
        self.SIZE = SIZE
        self.nTanaman = nTanaman
        self.mGardenName = mGardenName
        self.pArrList = pArrList
        self.hasilPanen = hasilPanen
    
    def Garden(self):
        self("UGarden")
    
    def addPlant(self, p):
        if(self.nTanaman < self.SIZE):
            self.pArrList.append(p)
            self.nTanaman+=1
            return True
        else:
            return False

    def harvestPlant(self):
        tmpN = 0
        i = 0
        while self.pArrList != [] and i < len(self.pArrList):
            if self.pArrList[i].getStatusTumbuh() == 4:
                self.pArrList.remove(self.pArrList[i])
                self.nTanaman -= 1
                tmpN += 1
                i = 0
            else:
                i+=1
        self.hasilPanen = self.hasilPanen + (tmpN * 100)
        return tmpN
    
    def beriAir(self):
        print(self.pArrList)
        for item in self.pArrList:
            item.beriAir()
        
    def beriPupuk(self):
        for item in self.pArrList:
            item.beriPupuk()
    

    def displayPlant(self):
        print("\n")
        print("----- {} -----".format(self.mGardenName))
        print("There are {} plant(s) in the garden".format(self.nTanaman))
        print("Your harvest point: {}".format(self.hasilPanen))
        for index in range(0, len(self.pArrList)):
            self.pArrList[index].displayPlant()

    def getHasilPanen(self):
        return self.hasilPanen

class Store:
    def __init__(self, name = "", jumlahTaman = 0, listGarden = Garden([])):
        self.name = name
        self.listGarden = listGarden
        self.jumlahTaman = jumlahTaman
    
    def addGardenToStore(self, p):
        self.listGarden.append(p)
        self.jumlahTaman+=1
    
    def removeGardenFromStore(self, nameGarden):
        for idx in range (0, len(self.listGarden)):
            if nameGarden == self.listGarden[idx].mGardenName:
                self.listGarden.remove(self.listGarden[idx])
                self.jumlahTaman-=1
                print("Berhasil Menghapus {}".format(nameGarden))
                return self.displayGarden()
            else:
                print("Nama taman tidak ditemukan atau sudah terhapus.")



    def displayGarden(self):
        if(self.jumlahTaman > 0):
            print("Nama Toko : {}".format(self.name))
            print("Jumlah {} taman beserta detail tanamannya : ".format(self.jumlahTaman))
            for index in range(0, len(self.listGarden)):
                self.listGarden[index].displayPlant()
        else:
            print("Tidak ada taman yang tersedia di toko.")

class Person:
    def __init__(self, name):
        self.name = name
    
    def buyPlant(self, store = Store(), category = "", plantName = 0, amount = 0):
        for idx in range(0, len(store.listGarden)):
            if category == store.listGarden[idx].mGardenName:
                for secondIdx in range(0, len(store.listGarden[idx].pArrList)):
                    if plantName == store.listGarden[idx].pArrList[secondIdx].name and store.listGarden[idx].pArrList[secondIdx].jumlahTanaman > amount:
                        store.listGarden[idx].pArrList[secondIdx].reducePlant(amount)
                        self.displayName()
                        print("Berhasil membeli {} buah {}".format(amount, plantName))
                        return store.displayGarden()
                    return print("Tanaman/Sayuran tidak tersedia.")
            
            return print("Kategori Tanaman/Sayuran tidak tersedia.")

    
    
    def displayName(self):
        print("Nama Pembeli : {}".format(self.name))



plants = []
plants.append(Plant("Anggrek", "Rp 100.000", 4, 1, 1, 5))
plants.append(Plant("Mawar", "Rp 150.000", 4, 2, 3, 5))
plants.append(Plant("Melati", "Rp 20.000", 4, 2, 1, 5))
garden = Garden(10, len(plants), "Taman Bunga", plants)
vegetablePlants = []
vegetablePlants.append(Plant("Sawi", "Rp 10.000", 3, 1, 1, 5))
vegetablePlants.append(Plant("Bayam", "Rp 15.000", 3, 2, 3, 5))
secondGarden = Garden(10, len(vegetablePlants), "Taman Sayuran", vegetablePlants)
myStore = Store("Toko Bunga dan Sayuran", 0, [])
myStore.addGardenToStore(garden)
myStore.addGardenToStore(secondGarden)
myStore.displayGarden()

myStore.removeGardenFromStore("Taman Bunga")


person = Person("Josua")
person.buyPlant(myStore, "Taman Sayuran", "Sawi", 6)






