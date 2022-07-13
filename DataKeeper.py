import ComparativeAnalysis
import DocParser
from tabulate import tabulate

from User import User


class DataKeeper:

    def __init__(self):
        self.history = {}

    def showHistory(self):
        data = list(self.history.values())
        keys = list(self.history.keys())
        for i in range(len(data)):
            data[i].insert(0, keys[i])

        print(tabulate(data,
                       headers=['КОЛИЧЕСТВО ОБЫЧНЫХ АКЦИЙ', 'КОЛИЧЕСТВО ПРИВИЛЕГИРОВАННЫХ АКЦИЙ', 'ЦЕНА ОБЫЧНЫХ АКЦИЙ',
                                'ЦЕНА ПРИВИЛЕГИРОВАННЫХ АКЦИЙ', 'БАЛАНСОВАЯ СТОИМОСТЬ',
                                'ВСЕГО АКТИВОВ', 'ВСЕГО ОБЯЗАТЕЛЬСТВ', 'РЫНГОЧНАЯ КАПИТАЛИЗАЦИЯ',
                                'БАЗА ЗНАНИЙ', 'КОЛИЧЕСТВО ПОЛЬЗОВАТЕЛЕЙ БАЗЫ', 'ТРЕНИНГИ',
                                'КОЛИЧЕСТВО ТРЕНИНГОВ', 'НАСТАВНИКИ',
                                'КОЛИЧЕСТВО СОТРУНИКОВ', 'КОЛИЧЕСТВО СОТРУНИКОВ ПРОШЕДШИХ ОБУЧЕНИЕ', 'ПО', 'ДОХОД КОМПАНИИ'],
                       tablefmt="grid"))
        for i in range(len(data)):
            data[i].pop(i)

    def getMap(self):
        return self.history

    def fillMap(self, file):
        # считываем по строкам и отправляем в словарь
        file = open(file, "r")
        lineCounter = 0

        # считываем строку

        line = file.readline()
        oneWord = line.split(" ")
        key = oneWord[0]
        oneWord = oneWord[1:]

        for item in oneWord:
            lineCounter = lineCounter + 1
            if "1" in item or "2" in item or "3" in item or "4" in item or "5" in item or "6" in item or "7" in item or "8" in item or "9" in item or "0" in item or item =="ПО":
                d = str(item)
                if item == "ПО":
                    d = oneWord[lineCounter]

                if key in self.history.keys():
                    data = self.history.get(key)
                    data.append(d)
                    self.history.update({key: data})
                else:
                    data = []
                    data.append(d)
                    self.history.update({key: data})

            file.close
        return self.history


newUser = User('Kate', '816856')
newUser.log()
myData = DataKeeper()
operation = "0"
method = "0"

print("Choose the data entering method:")
print("1. Input document")
print("2. Enter data")
method = int(input())
if method == 1:
    print("Input name of the file: ")
    name = DocParser.nameInput()
    dataFile = DocParser.convertData(DocParser.readDoc(name))

    myData.fillMap(dataFile)
elif method == 2:
    file1 = open("C:\\Users\\ПК\\Desktop\\Диплом\\SelfWriter.txt", "w+")
    print("Input year of analysis")
    text = input()
    file1.write(text+" ")
    print("Input the price of ordinary shares")
    text = input()
    file1.write(text+" ")
    print("Input the price of preferred shares")
    text = input()
    file1.write(text+" ")
    print("Input the amount of ordinary shares")
    text = input()
    file1.write(text + " ")
    print("Input the amount of preferred shares")
    text = input()
    file1.write(text + " ")
    print("Input the balance value of the company")
    text = input()
    file1.write(text + " ")
    print("Input the company assets")
    text = input()
    file1.write(text + " ")
    print("Input the company obligations")
    text = input()
    file1.write(text + " ")
    print("Input the market capitalization")
    text = input()
    file1.write(text + " ")
    print("if your company has base of knowledge input 1, otherwise input 0")
    text = input()
    file1.write(text + " ")

    print("input the number of knowledge base views")
    text = input()
    file1.write(text + " ")
    print("if your company has the system of trainings input 1, otherwise input 0")
    text = input()
    file1.write(text+" ")

    print("input the number of trainings")
    text = input()
    file1.write(text+" ")
    print("if your company has the mentoring system input 1, otherwise input 0")
    text = input()
    file1.write(text + " ")
    print("input the number of employees")
    text = input()
    file1.write(text + " ")
    print("input the number of educated employees in the company")
    text = input()
    file1.write(text + " ")
    print("input the name of the program id used in the company for knowledge management")
    text = input()
    file1.write(text + " ")
    print("input the income of the company in thousands of rubles")
    text = input()
    file1.write(text + " ")
    file1.close()

    myData.fillMap("C:\\Users\\ПК\\Desktop\\Диплом\\SelfWriter.txt")
else:
    print("try again")
    exit(-1)


while operation != "4":
    print("Choose the operation:")
    print("1. Show assess")
    print("2. Show analysis")
    print("3. Show history")
    print("4. Enter more data")
    print("5. Exit")

    operation = int(input())

    if operation == 1:
        if len(myData.getMap().keys()) > 1:
            ComparativeAnalysis.assess(myData.getMap())
        else:
            print("Enter data, load the document")

    elif operation == 2:
        if len(myData.getMap().keys()) > 0:
            ComparativeAnalysis.showAnalysis(myData.getMap())
            ComparativeAnalysis.makeGraphs(myData.getMap())
        else:
            print("Enter data, load the document")

    elif operation == 3:
        myData.showHistory()
    elif operation == 4:
        print("Choose the data entering method:")
        print("1. Input document")
        print("2. Enter data")
        method = int(input())
        if method == 1:
            print("Input name of the file: ")
            name = DocParser.nameInput()
            dataFile = DocParser.convertData(DocParser.readDoc(name))

            myData.fillMap(dataFile)
        elif method == 2:
            file1 = open("C:\\Users\\ПК\\Desktop\\Диплом\\SelfWriter.txt", "w+")
            print("Input year of analysis")
            text = input()
            file1.write(text + " ")
            print("Input the price of ordinary shares")
            text = input()
            file1.write(text + " ")
            print("Input the price of preferred shares")
            text = input()
            file1.write(text + " ")
            print("Input the amount of ordinary shares")
            text = input()
            file1.write(text + " ")
            print("Input the amount of preferred shares")
            text = input()
            file1.write(text + " ")
            print("Input the balance value of the company")
            text = input()
            file1.write(text + " ")
            print("Input the company assets")
            text = input()
            file1.write(text + " ")
            print("Input the company obligations")
            text = input()
            file1.write(text + " ")
            print("Input the market capitalization")
            text = input()
            file1.write(text + " ")
            print("if your company has base of knowledge input 1, otherwise input 0")
            text = input()
            file1.write(text + " ")

            print("input the number of knowledge base views")
            text = input()
            file1.write(text + " ")
            print("if your company has the system of trainings input 1, otherwise input 0")
            text = input()
            file1.write(text + " ")

            print("input the number of trainings")
            text = input()
            file1.write(text + " ")
            print("if your company has the mentoring system input 1, otherwise input 0")
            text = input()
            file1.write(text + " ")
            print("input the number of employees")
            text = input()
            file1.write(text + " ")
            print("input the number of educated employees in the company")
            text = input()
            file1.write(text + " ")
            print("input the name of the program id used in the company for knowledge management")
            text = input()
            file1.write(text + " ")
            print("input the income of the company in thousands of rubles")
            text = input()
            file1.write(text + " ")
            file1.close()

            myData.fillMap("C:\\Users\\ПК\\Desktop\\Диплом\\SelfWriter.txt")
        else:
            print("try again")
            exit(-1)

    elif operation == 5:
        exit(-1)
    else:
        print("The input is not correct. Try again.")

