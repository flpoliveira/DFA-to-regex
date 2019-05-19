import json
states = []


def main():
    inputData = readInput('input_2.json')
    # print(getAllTransitionsWithAListOfResults(
    # inputData['accepting'], inputData))
    recursiveNewStateChecker(inputData, inputData['accepting'])
    print("<<", states, ">>")


def recursiveNewStateChecker(inputData, state):
    if(state not in states):
        states.append(state)
        response = getAllTransitionsWithAListOfResults(
            state, inputData)
        for x in response:
            recursiveNewStateChecker(inputData, x)

    return


def readInput(path):
    file = open(path, 'r')
    jsonData = json.loads(file.read())
    return jsonData


def getAllTransitionsWithAListOfResults(listOfResults, inputData):
    response = []
    for y in inputData['alphabet']:
        aux = []
        for x in inputData['transitions']:
            if(x['to'] in listOfResults and x['letter'] == y):
                aux.append(x['from'])
                print(">>", aux)
        response.append(aux)
    return response


if __name__ == "__main__":
    main()
