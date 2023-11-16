def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words = {}
    for line in file:
        word1, word2 = line.split("-")
        words[word1] = word2
    return words

