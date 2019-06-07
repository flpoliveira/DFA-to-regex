import json
import sys
import re
states = []
formatedStates = []
regexOutput = ""
equacoes = []
estados = []

def main():
	inputData = getFileName()
	print(getAllTransitionsWithAListOfResults(inputData['accepting'], inputData))
	recursiveNewStateChecker(inputData, inputData['accepting'])
#    print("<<", states, ">>")
    #for i in reversed(states):
    #    for j in formatedStates:
            #if(i == j[0] and len(j[2]) != 0):
                #print("<<", "(", "|".join(j[0]), ") =",
                #     "(", "|".join(j[2]), ")", j[1], ">>")
    #simplificar(inputData)
	for i in reversed(states):
		for j in formatedStates:
			if(i == j[0] and len(j[2]) != 0):
				lista = []
				aux = "|".join(j[0])
				lista.append(aux)
				aux2 = "<"+"|".join(j[2])+">"+str(j[1])
				lista.append(aux2)
				equacoes.append(lista)
	for i in equacoes:
		c = 0
		estados.append(i[0])
		for j in equacoes:
			if(i[0] == j[0]):
				c += 1
				if(i[1] != j[1]):
					i[1] = i[1]+'+'+j[1]
					equacoes.remove(j)
				elif(c > 1):
					equacoes.remove(j)
	for i in equacoes:
		for j in i[0].split('|'):
			if(j == inputData['initial']):
				i[1] = i[1]+'+$'
				break

	for i in equacoes:
		print("Antes -------")
		print(i[0]+"="+i[1])
		for j in estados:
			#if(len(re.findall("<["+j+"]*>",i[1])) > 1):
			aux1 = []
			aux2 = []
			for x in i[1].split("+"):
				aux = x.replace("<"+j+">", '')
				y = x.replace(aux, '')
				if('<'+j+'>' == y):
					aux1.append(aux)
				else:
					aux2.append(x)
			if(len(aux1) > 1):
				i[1] = '<'+j+'>('+'+'.join(aux1)+')'+'+'+'+'.join(aux2)
		print("Depois -----")
		print(i[0]+"="+i[1])
		print("------------")
	for i in equacoes:
		print(i[0]+'='+i[1])



        # print(i[0] +" = "+ i[1])

    #algebraicRemovalMethod(inputData)
    # print(regexOutput)





def arden(inputData, estado):
    for i in reversed(states):
        for j in formatedStates:
            if(i == j[0] and len(j[2]) != 0):
                if(j[0] == estado[0] and (estado[1] != j[1] or estado[2] != j[2])):
                    print("Nao deu")


def algebraicRemovalMethod(inputData):
    global regexOutput
    for i in reversed(states):
        for j in formatedStates:
            if(i == j[0] and len(j[2]) != 0):
                print(j[0], " = ", j[2], j[1])
                if(j[0] == j[2] or j[0] == j[1]):
                    print("auto referencia")
                    arden(inputData, j)
            #    if(len(regexOutput) != 0 and regexOutput[-1] in inputData['alphabet']):
                #    regexOutput += "+"
                #regexOutput += j[1]
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
        print("[", listOfResults, y, "]", " >>",  aux)
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
