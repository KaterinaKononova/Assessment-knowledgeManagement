# history[цена акций, цена акций, количество, количество, балансовая стоимость, активы, обязательства, рын.каитализация]
import sys
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import pandas as pd


def assess(history):
    keys = list(history.keys())  # для подбора ключей

    companySize0 = 1                              # 1 - small, 2 - big
    companySize1 = 1
    if float(history.get(keys[len(keys) - 2])[13]) > 100 and float(history.get(keys[len(keys) - 2])[16]) > 800:     # 16 index  - marga, 15 - PO
        companySize0 = 2
    if float(history.get(keys[len(keys) - 1])[13]) > 100 and float(history.get(keys[len(keys) - 1])[16]) > 800:
        companySize1 = 2

    companyDev0 = float(history.get(keys[len(keys) - 2])[14]) / float(history.get(keys[len(keys) - 2])[13])
    companyDev1 = float(history.get(keys[len(keys) - 1])[14]) / float(history.get(keys[len(keys) - 1])[13])
    if history.get(keys[len(keys) - 2])[12] == "1":
        companyDev0 = companyDev0+0.3
    if history.get(keys[len(keys) - 1])[12] == "1":
        companyDev1 = companyDev1+0.3

    poQualityName0 = history.get(keys[len(keys) - 2])[15]
    poQualityName1 = history.get(keys[len(keys) - 1])[15]

    wb = load_workbook('ПО.xlsx')
    print(wb.get_sheet_names())
    sheet = wb.get_sheet_by_name('Лист1')
    df = pd.DataFrame(sheet.values)
    names = df[0]
    compSize = df[1]
    counter = 0
    poQuality0 = 0
    poQuality1 = 0
    for name in range(len(names)-1):
        counter = counter+1
        # прошлый год
        if names[name] == poQualityName0:
            poQuality0 = poQuality0+0.5
            if companySize0 <= compSize[counter]:
                poQuality0 = poQuality0+0.5
            else:
                poQuality0 = poQuality0+0
        #текущий год
        if names[name] == poQualityName1:
            poQuality1 = poQuality1+0.5
            if companySize1 <= compSize[counter]:
                poQuality1 = poQuality1+0.5
            else:
                poQuality1 = poQuality1+0

    intellectualCost1 = countIntellectualCost(history, keys[len(keys) - 2])
    intellectualCost2 = countIntellectualCost(history, keys[len(keys) - 1])

    # ценка эффективности считается относительно базового и текущего года
    dev = (companyDev1 - companyDev0) / companyDev0
    po = (poQuality1-poQuality0)/poQuality0
    assess = ((intellectualCost2 - intellectualCost1) / intellectualCost1 + dev + po)/3*100
    print("assess of effectiveness ", assess, "%")


def countTobin(history, key):
    # считаем q - индекс Тобина
    marketValue1 = float(history.get(key)[0]) * float(history.get(key)[2]) + float(history.get(key)[1]) * float(history.get(key)[3])
    q1 = marketValue1 / (float(history.get(key)[5]) * 1000 - float(history.get(key)[6]) * 1000)
    return q1


def countIntellectualCost(history, key):
    intellectualCost = float(history.get(key)[7]) * 1000 - (float(history.get(key)[2]) + float(history.get(key)[3]))
    return intellectualCost


def makeGraphs(history):
    data = makeDataForDiagGraph(history)

    x = list(history.keys())

    fig, ax = plt.subplots(3, 2)
    ax = ax.flatten()
    # цены акций
    ax[0].bar(x, data[0])
    ax[0].bar(x, data[1])
    ax[0].set_title("Prices of shares(rub)")
    ax[0].set_facecolor('seashell')

    # количество тренингов
    ax[1].bar(x, data[2])
    ax[1].set_title("Amount of trainings in the company")
    print(data[2])

    # использование базы
    ax[2].bar(x, data[3])
    ax[2].set_title("Base use")

    # индекс Тобина
    ax[3].bar(x, data[4])
    ax[3].set_title("Tobin Index")

    # стоимость интеллектуального капитала

    ax[4].bar(x, data[5])
    ax[4].set_title("Intellectual cost")

    # персонал обученный/нет
    ax[5].bar(x, data[0])
    ax[5].bar(x, data[1])
    ax[5].set_title("Staff (mln)")

    fig.set_figheight(10)
    fig.set_figwidth(15)
    plt.show()


def makeDiagram(history):
    data = makeDataForDiagGraph(history)
    print("Diagram", data)


def makeDataForDiagGraph(history):
    keys = list(history.keys())
    if len(keys) <= 1:
        print("More data needed")
        sys.exit()

    pricePremium = []
    priceOrdinary = []
    education = []
    baseUse = []
    tobinIndex = []
    intellectCost = []
    educatedStaff = []
    staff = []

    for i in range(len(keys)):
        priceOrdinary.append(float(history.get(keys[i])[0]))
        pricePremium.append(float(history.get(keys[i])[1]))
        education.append(float(history.get(keys[i])[11]))
        baseUse.append(float(history.get(keys[i])[9]))
        tobinIndex.append(float(countTobin(history, keys[i])))
        intellectCost.append(float(countIntellectualCost(history, keys[i])))
        educatedStaff.append(float(history.get(keys[i])[14]))
        staff.append(float(history.get(keys[i])[13]))

    data = [priceOrdinary, pricePremium, education, baseUse, tobinIndex, intellectCost, educatedStaff, staff]
    return data


def showAnalysis(history):
    keys = list(history.keys())  # для подбора ключей
    if len(keys) >= 1:
        key = keys.pop((len(keys) - 1))
    else:
        print("No data")
        sys.exit()

    print(key)

    print("Индекс Тобина ", countTobin(history, key))
    print("Стоимость интеллектуального капитала ", countIntellectualCost(history, key), "млн.руб.")
    print(
        "% сотрудников прошедших внутренне обучение ", float(history.get(key)[14]) / float(history.get(key)[13]) * 100, "%")
    print("% сотрудников пользующихся базой знаний компании ", float(history.get(key)[9]) / float(history.get(key)[13]) * 100, "%")
    print("В компании на текущий момент есть ")
    if history.get(key)[8] == "1":
        print("База знаний")

    if history.get(key)[10] == "1":
        print("Внутренние тренинги")

    if history.get(key)[12] == "1":
        print("Наставники")
