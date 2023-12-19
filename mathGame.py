try:
    # Importe les fonctions depuis le module 'myPythonFunctions'
    from myPythonFunctions import *

    # Demande le nom de l'utilisateur
    userName = input("Donnez votre nom : ")

    # Obtient les points de l'utilisateur
    userScore = int(getUserPoint(userName))

    # Vérifie si l'utilisateur est nouveau
    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False

    userChoice = 0

    # Boucle principale du jeu
    while userChoice != -1:
        # Incrémente les points de l'utilisateur avec le résultat de la question
        userScore += generateQuestion()

        # Demande à l'utilisateur s'il veut jouer à nouveau
        while True:
            user_input = input("Voulez-vous jouer encore une fois [y/n]?: ").lower()
            if user_input == 'y':
                break
            elif user_input == 'n':
                # Quitte la boucle et affiche un message de remerciement
                print("Merci d'avoir joué au jeu BODMAS, à la prochaine fois! ")
                userChoice = -1
                break
            else:
                print("Veuillez saisir 'y' pour continuer ou 'n' pour quitter")

    # Met à jour les points de l'utilisateur dans le fichier
    updateUserPoints(newUser, userName, userScore)

except:
    # Gère les erreurs potentielles et affiche un message en cas d'échec
    print("Une erreur s'est produite et le programme se terminera.")
