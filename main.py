import json
import sys
states = []
formatedStates = []
regexOutput = ""


def main():
    inputData = getFileName()
    print(getAllTransitionsWithAListOfResults(
        inputData['accepting'], inputData))
    recursiveNewStateChecker(inputData, inputData['accepting'])
    print("<<", states, ">>")
    for i in reversed(states):
        for j in formatedStates:
            if(i == j[0] and len(j[2]) != 0):
                print("<<", "(", "|".join(j[0]), ") =",
                      "(", "|".join(j[2]), ")", j[1], ">>")
    algebraicRemovalMethod(inputData)
    # print(regexOutput)


def algebraicRemovalMethod(inputData):
    global regexOutput
    for i in reversed(states):
        for j in formatedStates:
            if(i == j[0] and len(j[2]) != 0):
                # print(j[0], " = ", j[2], j[1])
                if(len(regexOutput) != 0 and regexOutput[-1] in inputData['alphabet']):
                    regexOutput += "+"
                regexOutput += j[1]
        # print(">>>>", inputData['initial'] in i, inputData['initial'], i)
        if(inputData['initial'] in i):
            regexOutput = "("+regexOutput+")*"
        # print(">>>", regexOutput)
    return


def recursiveNewStateChecker(inputData, state):
    if(state not in states and len(state) != 0):
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
        response.append(aux)
        # print("[", listOfResults, y, "]", " >>",  aux)
        formatedStates.append([listOfResults, y, aux])

    return response


def getFileName():
    try:
        filePath = sys.argv[1]
        if(filePath[-5:] != ".json"):
            raise ValueError("Formato de arquivo incorreto !!!")
        inputData = readInput(filePath)
        return inputData
    except IndexError:
        raise ValueError("Nome de arquivo não informado !!!")
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado !!!")


if __name__ == "__main__":
    main()
