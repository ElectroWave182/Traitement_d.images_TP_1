def inverted():
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/chat.pgm", "r")
    useless = fd.readline()
    nbCol, nbLig = fd.readline().split()
    blanc = int(fd.readline())
    tableau = [list(map(int, fd.readline().split())) for _ in range(int(nbLig))]
    fd.close()
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/tahc.pgm", "w")
    fd.write("P2\n" + nbCol + " " + nbLig + "\n" + str(blanc))
    for ligne in tableau:
        fd.write("\n")
        for color in ligne:
            fd.write(str(blanc - color) + " ")
    fd.close()
inverted()
