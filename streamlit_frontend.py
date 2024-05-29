




with open("data2.txt", "r")as file:
    data = file.readlines()
    new_list = [temperature.split(",") for temperature in data]
    print(new_list)
    for element in new_list:
        print(element)
        dictionnaire = {element[0]:
                            int(element[1].replace("\n",""))
                        for element in new_list}
    print(dictionnaire)
    for index, keys in enumerate(dictionnaire):
        print(index)






#creer un dictionnaire où les clefs serait le 0 de chaque liste
#et la valeur serait le [1] de chaque liste