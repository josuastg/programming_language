class Jam:

    def __init__(self, jam = 0, menit = 0, detik = 0):
        self.jam = jam
        self.menit = menit
        self.detik = detik

    def tambahJam(self, jam):
        if(type(self.jam) is str):
            self.jam = int(self.jam)
        self.jam += jam
        if(self.jam >= 0 and self.jam < 24):
            if(self.jam < 10):
              self.jam = "0"+ str(self.jam)
            else:
                self.jam = self.jam 
        else:
            self.jam = 0
            print("Invalid Hours !!")
        

    def tambahMenit(self, menit):
        if(type(self.menit) is str):
            self.menit = int(self.menit)
        self.menit += menit
        if(self.menit >= 0 and self.menit < 60):
            if(self.menit == 0 or self.menit < 10):
              self.menit = "0"+ str(self.menit)
            else:
                self.menit = self.menit 
        else:
            self.menit = 0
            print("Invalid Minutes !!")
     
    def tambahDetik(self, detik):
        if(type(self.detik) is str):
            self.detik = int(self.detik)
        self.detik +=detik
        if(self.detik >= 0 and self.detik < 60):
            if(self.detik < 10):
              self.detik = "0"+ str(self.detik)
            else:
              self.detik = self.detik 
        else:
            self.detik = 0
            print("Invalid Seconds !!")
            

    def displayJam(self):
        print("\n")
        print("{}:{}:{} (jam:menit:detik)"
        .format(
        "00" if self.jam == 0 else self.jam, 
        "00" if self.menit == 0 else self.menit, 
        "00" if self.detik == 0 else self.detik
        ))
        print("\n")


jam = Jam()
jam.tambahJam(12)
jam.tambahJam(10)
jam.tambahMenit(20)
jam.tambahMenit(10)
jam.tambahDetik(10)
jam.tambahDetik(5)
jam.displayJam()







