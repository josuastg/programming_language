print('=== Masukkan Identitas dan Nilai Anda ===')
name = input('Masukkan Nama anda : ')
nim = input('Masukkan NIM anda : ')
gender = input('Masukkan Gender anda (ex: Pria/Wanita) : ')
valueInputDate = input('Masukkan Tanggal Input Nilai (ex: YYYY-MM-DD) : ')
course = input('Masukkan Mata Kuliah anda : ')
presence = input('Masukkan Jumlah Kehadiran anda (ex: 0 s/d 14) : ')
homework = input('Masukkan Nilai Tugas anda (ex: 0 s/d 100) : ')
middleTest = input('Masukkan Nilai UTS anda (ex: 0 s/d 100) : ')
finalTest = input('Masukkan Nilai UAS anda (ex : 0 s/d 100): ')


def countPercentageValue(presences, homework, middleTest, finalTest):
    resultPresence = (int(presences) / 14) / 0.1
    resultHomework = int(homework) * 0.25
    resultMiddleTest = int(middleTest) * 0.30
    resultFinalTest = int(finalTest) * 0.35
    finalResult = round(resultPresence + resultHomework + resultMiddleTest + resultFinalTest)
    if(finalResult <= 49):
        grade = "E"
    elif (finalResult > 49 and finalResult < 60):
        grade = "D"
    elif(finalResult > 59 and finalResult < 64):
        grade = "C"
    elif(finalResult > 63.9 and finalResult < 68):
        grade= "C+"
    elif(finalResult > 67.9 and finalResult < 71):
        grade = "B-"
    elif(finalResult > 70.9 and finalResult < 74):
        grade = "B"
    elif(finalResult > 73.9 and finalResult < 77):
        grade = "B+"
    elif(finalResult >76.9 and finalResult < 80):
        grade = "A-"
    else:
        grade ="A"
    print("""GRADE: {}\n
NILAI AKHIR: {}\n 
Keterangan Lulus: {}""".format(grade, finalResult, "LULUS" if finalResult > 67.9 and finalResult <= 100 else "TIDAK LULUS"))  
print("\n")
print('=== Hasil Penilaian===')
print(
"""\nNama : {}\n
NIM : {}\n
Jenis Kelamin : {}\n
Tanggal Input Nilai : {}\n
Nama Mata Kuliah : {}\n
Absensi : Hadir {} Pertemuan\n
Tugas : {}\n
UTS : {}\n
UAS : {}
    """.format(name, nim, gender, valueInputDate, course, presence, homework, middleTest, finalTest))
print(countPercentageValue(presence, homework, middleTest, finalTest))
