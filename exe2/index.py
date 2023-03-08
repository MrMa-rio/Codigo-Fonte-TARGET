arrayNumber = [0, 1]
numberInput = int(input("Digite um numero: "))

while numberInput >= arrayNumber[arrayNumber.__len__() - 1]:
    number = arrayNumber[arrayNumber.__len__() - 1] + arrayNumber[arrayNumber.__len__() - 2]
    arrayNumber.append(number)

if numberInput in arrayNumber:
    print("O numero informado existe na sequencia de Fibo.")

else:
    print("Infelizmente o numero não foi encotrado na sequencia de Fibo.")

print(arrayNumber)
