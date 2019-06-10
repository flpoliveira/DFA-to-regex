import json
import sys
import re
states = []
formatedStates = []
regexOutput = ""
equacoes = []
estados = set()
#vetor = []
log = []

def main():
	inputData = getFileName()
	#print(getAllTransitionsWithAListOfResults(inputData['accepting'], inputData))
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
				#print("<<", "(", "|".join(j[0]), ") =",
                     #"(", "|".join(j[2]), ")", j[1], ">>")
				lista = []
				aux = "|".join(j[0])
				lista.append(aux)
				aux2 = "<"+"|".join(j[2])+">"+str(j[1])
				lista.append(aux2)
				equacoes.append(lista)
	for i in equacoes:
		c = 0
		estados.add(i[0])
		for j in equacoes:
			if(i[0] == j[0]):
				c += 1
				if(i[1] != j[1]):
					i[1] = i[1]+'+'+j[1]
					equacoes.remove(j)
				elif(c > 1):
					equacoes.remove(j)
		aa = set()
		for x in i[1].split('+'):
			aa.add(x)
		i[1] = '+'.join(aa)

	for i in equacoes:
		for j in i[0].split('|'):
			if(j == inputData['initial']):
				i[1] = i[1]+'+$'
				break
	log.append('Apos aplicar o algoritmo, obtivemos as seguintes equacoes')
	log.append('---------------------------------------------------------')
	for i in equacoes:
		log.append(printEquacao(i))
	log.append('---------------------------------------------------------')
	pai = []
	funcao(i, pai)
	log.append('Logo, a ER para este AFD fica:')
	log.append(i[1].replace('&', '+'))
	for x in log:
		print(x)

	#substituir(equacoes[1], equacoes[6])
	#arden(equacoes[6])
	#for i in equacoes:
		#printEquacao(i)
		##print(equacaoReferenciada(i))


        # print(i[0] +" = "+ i[1])

    #algebraicRemovalMethod(inputData)
    # print(regexOutput)

def simplificar():

		for i in equacoes:
			#print("Antes -------")
			#print(i[0]+"="+i[1])
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
					log.append('Simplificando a equacao ' + printEquacao(i))
					i[1] = ''
					if(len(aux2) > 0):
						i[1] = '+'.join(aux2)+'+'
					i[1] = i[1]+'<'+j+'>('+'&'.join(aux1)+')'
					log.append('Obtemos ' + printEquacao(i))
			#print("Depois -----")
			#print(i[0]+"="+i[1])
			#print("------------")

def printEquacao(equacao):
	return '<'+equacao[0]+'>'+'='+equacao[1].replace('&', '+')

def arden(equacao):
	simplificar()
	#print(equacao[0]+'='+equacao[1])
	aux = ''
	aux1 = ''
	aux2 = []
	for x in equacao[1].split('+'):
		aux = x.replace("<"+equacao[0]+">", '')
		y = x.replace(aux, '')
		#print(aux)
		if('<'+equacao[0]+'>' == y):
			aux1 = aux
		else:
			aux2.append(x)
	if(aux1 != ''):
		log.append('Aplicando Arden a equacao '+ printEquacao(equacao))
		if ( len(aux1) == 1 ) or (aux1.startswith('(') and aux1.endswith(')')):
			aux1 = aux1+'*'
		else:
			aux1 = '('+aux1+')*'
		saida = ''
		for x in aux2:
			if(x == '$'):
				saida = saida + aux1 + '+'
			else:
				saida = saida + x + aux1 + '+'
		equacao[1] = saida[:-1]
		log.append('Obtemos '+ printEquacao(equacao))

def funcao(equacao, pai):
	#vetor.append(equacao[0])
	#print(vetor)
	pai.append(equacao[0])
	#print(pai)
	for i in equacaoReferenciada(equacao):
		if(i[0] not in pai):
			funcao(i, pai)
			substituir(i, equacao)

	arden(equacao)
	pai.pop()

def substituir(equacao2, equacao1):
	log.append('Substituindo <' + equacao2[0] + '> em <' + equacao1[0]+'>')
	log.append(printEquacao(equacao2))
	log.append(printEquacao(equacao1))
	listaSemEquacao2 = []
	comEquacao2 = ''
	for x in equacao1[1].split('+'):
		aux = x.replace('<'+equacao2[0]+'>', '')
		y = x.replace(aux, '')
		if(y == '<'+equacao2[0]+'>'):
			comEquacao2 = aux
		else:
			listaSemEquacao2.append(x)
	saida = ''
	if(len(comEquacao2) != 0):
		for x in equacao2[1].split('+'):
			if x == '$':
				saida = saida + comEquacao2 + '+'
			else:
				saida = saida + x + comEquacao2 + '+'
		for i in listaSemEquacao2:
			saida = saida + i+'+'
		equacao1[1] = saida[:-1]
		log.append(printEquacao(equacao1))
	else:
		log.remove('Substituindo <' + equacao2[0] + '> em <' + equacao1[0]+'>')
		log.remove(printEquacao(equacao2))
		log.remove(printEquacao(equacao1))


def equacaoReferenciada(equacao):
	retorno = []
	for i in equacao[1].split('+'):
		for j in estados:
			aux = i.replace('<'+j+'>', '')
			y = i.replace(aux, '')
			if(y == '<'+j+'>'):
				for x in equacoes:
					if(x[0] == j):
						retorno.append(x)
						break
	return retorno


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
        #print("[", listOfResults, y, "]", " >>",  aux)
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
