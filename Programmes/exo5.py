def inverted(largeur):
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/chat.pgm", "r")
    useless = fd.readline()
    nbCol, nbLig = fd.readline().split()
    debutLig, debutCol = int(nbLig)//2 - largeur//2, int(nbCol)//2 - largeur//2
    finLig, finCol = debutLig + largeur, debutCol + largeur
    blanc = int(fd.readline())
    tableau = [list(map(int, fd.readline().split())) for _ in range(int(nbLig))]
    fd.close()
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/chatX.pgm", "w")
    fd.write("P2\n" + nbCol + " " + nbLig + "\n" + str(blanc))
    for ligne in range(int(nbLig)):
        fd.write("\n")
        for colonne in range(int(nbCol)):
            color = tableau[ligne][colonne]
            if debutLig <= ligne <= finLig or debutCol <= colonne <= finCol: fd.write(str(2*(blanc - color)//3 + color) + " ")
            else: fd.write(str(color) + " ")
    fd.close()
inverted(int(input("Largeur de la croix :")))
