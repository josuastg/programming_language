class Plant():
    def __init__(self, statusTumbuh = 0, jumlahAir = 0, jumlahPupuk = 0):
        self.statusTumbuh = statusTumbuh
        self.jumlahAir = jumlahAir
        self.jumlahPupuk = jumlahPupuk

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
    
    def displayPlant(self):
        print(self.getStatusTumbuhText())
        print("Jumlah Air : {}".format(self.jumlahAir))
        print("Jumlah Pupuk : {}".format(self.jumlahPupuk))
    
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

class Garden:
    def __init__(self, SIZE = 10, nTanaman = 0, 
    mGardenName = "", pArrList = Plant([]), 
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
        tmpN = 0;
        i = 0;
        while self.pArrList != [] and i < len(self.pArrList):
            if self.pArrList[i].getStatusTumbuh() == 4:
                self.pArrList.remove(self.pArrList[i])
                self.nTanaman -= 1
                tmpN += 1
                i = 0
            else:
                i+=1;
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
        print("----- {} -----".format(self.mGardenName))
        print("There are {} plant(s) in the garden".format(self.nTanaman))
        print("Your harvest point: {}".format(self.hasilPanen))
        for index in range(0, len(self.pArrList)):
            self.pArrList[index].displayPlant()

    def getHasilPanen(self):
        return self.hasilPanen

# plant.beriAir()
# plant.beriPupuk()
# plant.cekKondisiTumbuh()
# plant.displayPlant()

plant = Plant(2, 1, 1)
plants = []
plants.append(Plant(1,2,3))
plants.append(Plant(3,2,1))
garden = Garden(10, len(plants), "Taman Eden", plants)
garden.addPlant(plant)
garden.beriAir()
garden.beriPupuk()
garden.harvestPlant()
garden.displayPlant()







