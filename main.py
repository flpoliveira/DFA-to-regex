import json


def main():
    inputData = readInput('input.json')
    print(inputData)


def readInput(path):
    file = open(path, 'r')
    jsonData = json.loads(file.read())
    return jsonData


if __name__ == "__main__":
    main()
