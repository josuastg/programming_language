
def division(firstNum, secondNum):
    try:
        result = int(firstNum/ secondNum)
        print(result)
    except:
        print("Pembagian tidak bisa dibagi 0")


division(10,5)