import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data = json.load(data_file)
    for key in data.keys():
        if field == key:
            sequential_data = data[field]
            return sequential_data
    return None


def linear_search(sekvence, cislo):
    pozice = []
    slovnik = {"position": pozice, "count": 0}
    for i in range(len(sekvence)):
        if sekvence[i] == cislo:
            pozice.append(i)
            slovnik["count"] = slovnik["count"] + 1
    return slovnik


def pattern_search(sekvence, vzor = ""):
    pozice = set()
    delka = len(sekvence)
    delka_vzoru = len(vzor)
    for i in range(delka - delka_vzoru + 1):
        if sekvence[i:i+delka_vzoru] == vzor:
            pozice.add(i)
    return pozice


def main():
    """sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential data: ", sequential_data)
    slovnik = linear_search(sequential_data, 0)
    print(slovnik)"""
    sekvence = read_data("sequential.json", "dna_sequence")
    print(sekvence)
    pozice = pattern_search(sekvence, "ATG")
    print(pozice)
    return


if __name__ == '__main__':
    main()
