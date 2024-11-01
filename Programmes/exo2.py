def carre(n):
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/exo2.pgm", "w")
    fd.write("P2\n" + str(n) + " " + str(n) + "\n255")
    for _ in range(n):
        fd.write("\n")
        for _ in range(n):
            fd.write("128 ")
    fd.close()
carre(int(input()))
