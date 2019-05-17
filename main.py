import json


def main():
    inputData = readInput('input.json')


def readInput(path):
    file = open(path, 'r')
    jsonData = json.loads(file.read())
    return jsonData


def getAllTransitionsWithAListOfResults(listOfResults, transitions):
    response = []
    for x in transitions:
        if(x['to'] in listOfResults):
            response.append(x)
    return response


if __name__ == "__main__":
    main()
