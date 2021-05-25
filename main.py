##########################
# Début de mon programme #
##########################
import random

nombre = []
reponse = []
nom_joueur = ""
nb_fautes = 0
nb_calc_ok = False
nb_calculs = 0


# intégration du nom du joueur
def player_name():
    nom_joueur = input("Pour commencer, entre ton nom : ")
    print("Bonjour " + nom_joueur + " nous allons faire un peu de calcul...")
    print("L'exercice du jour est d'ajouter 101 à une liste de nombres")
    print('Tu peux quitter à tout moment en tapant la lettre "q" puis la touche entrée')
    return


def joueur_pret():
    nb_calc_ok = False
    while not nb_calc_ok == True:
        nb_calculs_str = input("Combien de calculs veux-tu effectuer ? : ")
        try:
            int(nb_calculs_str)
        except:
            print("Ce n'est pas un nombre")
        else:
            global nb_calculs
            nb_calculs = int(nb_calculs_str)
            if nb_calculs < 5:
                print("Ca ne fait pas beaucoup tout ça...\nSi on partait sur au moins 5, ça te va ?")
            elif nb_calculs > 15:
                print("Ca va faire un peu beaucoup tout ça\nChoisis un nombre plus petit (<ou=15)")
            else:
                nb_calc_ok = True
                # print(nb_calculs)
    global pret
    pret = ""
    while not pret == "oui":
        pret = input("Tu te sens prêt(e) pour faire " + str(nb_calculs) + " calculs ? : ")
        if pret == "oui" or pret == "Oui":
            pret = "oui"
            print("OK, c'est parti\n")
        elif pret == "q":
            quit()
        else:
            print("Euh... Je ne m'étais pas préparé à ça \nC'est embêtant... \nJe te repose la question")
    return


def generate_list():
    # print(nb_calculs)
    for i in range(0, nb_calculs):
        a = str((random.randint(1000, 2000)))
        nombre.append(a)
    # print(nombre)


def exercice_maths():
    h = 0
    while not h == nb_calculs:
        # print(h)
        # print(nombre[h])
        # print(int(nombre[h]) + 101)
        reponse = input("Entre le résultat de l'opération " + (nombre[h]) + " + 101 : ")
        if reponse == "q":
            return
        try:
            int(reponse)
        except:
            print("Ce n'est pas un nombre")
        else:
            if int(reponse) != int(nombre[h]) + 101:
                print("Perdu")
                global nb_fautes
                nb_fautes = nb_fautes + 1
                if nb_fautes > 1:
                    print("Tu as fait " + str(nb_fautes) + " fautes")
                else:
                    print("Tu as fait " + str(nb_fautes) + " faute")
            else:
                print("Bravo, c'est la bonne réponse")
                h += 1
    return


def __main__():
    player_name()
    joueur_pret()
    generate_list()
    # print(nombre)
    exercice_maths()
    print("C'est maintenant terminé \nTu as fais " + str(nb_fautes) + " fautes")
    quit()
    print("Bonne journée")


def quit():
    quitter_ok = False
    while quitter_ok == False:
        quitter = input("Veux tu vraiment quitter (q) ou recommencer (r) ? ")
        if quitter == "q":
            return
        elif quitter == "r":
            __main__()


__main__()
