from datetime import datetime

def countAge(yearOfBirth):
    currentYear = datetime.today().year
    result = currentYear - yearOfBirth
    print("Tahun lahir saya : {} \nUmur saya sekarang : {} tahun".format(yearOfBirth, result))

countAge(2000)

def countPPN(goodsPrice):
    ppn = int(goodsPrice * 0.1)
    result = int(goodsPrice + ppn)
    print("PPN yang dipungut : {} \nTotal pembelian setelah kena pajak : {}".format(ppn, result));

countPPN(15000);
