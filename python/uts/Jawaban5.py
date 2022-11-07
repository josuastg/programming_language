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