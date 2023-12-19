from random import randint
import os


# Obtient les points d'un utilisateur depuis le fichier 'userScores.txt'
def getUserPoint(username):
    with open('userScores.txt', 'r') as file:
        for line in file:
            user_data = line.split(', ')
            if user_data[0] == username:
                return int(user_data[1])
    return -1


# Met à jour les points d'un utilisateur dans le fichier 'userScores.txt'
def updateUserPoints(newUser, userName, score):
    if newUser:
        # Ajoute un nouvel utilisateur et ses points au fichier
        with open('userScores.txt', 'a') as file:
            file.write(f"{userName}, {score}\n")
    else:
        # Met à jour les points d'un utilisateur existant dans le fichier
        with open('userScores.tmp', 'w') as temp_file:
            with open('userScores.txt', 'r') as file:
                for line in file:
                    user, score = line.split(', ')
                    if user == userName:
                        temp_file.write(f"{userName}, {score}\n")
                    else:
                        temp_file.write(line)
                file.close()
                temp_file.close()

                # Remplace le fichier original par la version mise à jour
                os.remove('userScores.txt')
                os.rename('userScores.tmp', 'userScores.txt')


# Obtient une liste d'opérandes aléatoires
def getOperandList():
    operandList = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        operandList[i] = randint(0, 9)
    return operandList


# Obtient une liste d'opérateurs aléatoires
def getOperatorList():
    operatorList = ["", "", "", ""]
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"}
    for i in range(0, 4):
        while True:
            # Évite l'utilisation consécutive de l'opérateur '**'
            operator_key = randint(1, 4)
            if operatorList[i - 1] != '**' or operatorDict[operator_key] != '**':
                break
        operatorList[i] = operatorDict[operator_key]
    return operatorList


# Obtient une question mathématique sous forme de chaîne de caractères
def getQuestionString():
    operandList = getOperandList()
    operatorList = getOperatorList()
    # Combinaison d'opérandes et d'opérateurs
    interleaved_list = [f"{operand}{operator}" for operand, operator in zip(operandList, operatorList)] + [
        str(operandList[-1])]
    questionString = ''.join(interleaved_list)
    return questionString


# Évalue le résultat d'une expression mathématique
def evaluationResultat(questionString):
    return eval(questionString)


# Génère une question mathématique et demande la réponse à l'utilisateur
def generateQuestion():
    questionString = getQuestionString()
    resultat = evaluationResultat(questionString)
    questionString = questionString.replace("**", "^")

    # Affiche la question à l'utilisateur
    print(f"Voici l'expression à résoudre : {questionString} = ? ")
    while True:
        try:
            # Demande à l'utilisateur de fournir sa réponse
            reponse = int(input("Votre réponse : "))
            break
        except:
            print("Veuillez saisir un entier")

    # Vérifie si la réponse de l'utilisateur est correcte
    if reponse == resultat:
        print("Félicitations, vous avez bien résolu l'expression :) ! ")
        return 1
    else:
        print(f"Dommage, vous n'avez pas bien répondu :( voici la bonne réponse : {resultat}")
        return 0
