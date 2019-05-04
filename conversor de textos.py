textSpeakDictionary = {
    "rs" : "risos" ,
    "tbm" : "tambem",
    "vc" : "voce",
    "pq" : "porque"
}

#obtem a frase para traduçao
sentence = input("insira a frase para traduzir:").lower()

#divida a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translateSentence = ""

#passa por cada palavra da lista
for word in wordsToTranslate:

#adiciona a palavra traduzidacaso ela exista no dicionario
    if word in textSpeakDictionary:

        translateSentence += textSpeakDictionary[word] + ""

#mantem a palavra original caso nao exista traduçao
    else:

        translateSentence += word + ""

#imprime a frase traduzida
print("==>")
print(translateSentence)
def displaymenu():
    print("trdtr de express")
    print("=" * 13)
    print("menu:")
    print(" c = converter uma frase")
    print(" p = imprimir dicionario")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")


#---------------------------------------------------------------------------


def convertSetence():
    sentence = input (" insira uma frase para traduzir:").lower()
    translatedSentence = ""

    #advinhe a frase em uma lista de palavras
    listOfWords = sentence.split()

    for word in listOfWords:
        #direciona a palavra original caso nao exiata traduçao
        translatedsentence += textSpeakDictionary[word] + ""
        #mantem a palavra original caso nao exista traduçao
        #else:
        translatedSentence += Word+ " "

        #imprime a frase traduzida
        print("==>")
        print(translatecentence)

#------------------------------------------------------------
def addDirectioinaryItem():
    txtToAdd = input("insira a expressao a ser adicionada ao dicionario: ")

    #adiciona a nova traduçao ao dicionario
    textSpeakDictionary[txtToAdd] = meaning

#=====================
def deleteDictionaryItem():
    txtToDelete = input("insira a expressao a ser removida ao dicionario: ")
    #remove a traduçao do dicionario

#---------------------------------------
#o programa principal comessa aqui
#---------------------------------------


textSpeakDictionary = {
    "rs" : "risos",
    "tbm" : "tambem",
    "vc"  : "voce",
    "pq" : "porque"

    }


running = True

displaymenu()


#remove ate que o usuario digite 'q' para sair
while running == True:

    menuChoice = input(">_").lower()

#'c' para converter
    if menuChoice == 'c':
        convertSetence()

#'p' para imprimir
    elif menuChoice == 'p':
        print(textSpeakDictionary)

#'a' para adicionar
    elif menuChoice == 'a':
        addDirectioinaryItem()

#d para remover
    elif menuChoice == 'd':
        deleteDictionaryItem()

#q para sair
    elif menuChoice =='q':
        running = False

    else:
        print("escolha invalida")
                 
