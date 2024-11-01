def carre(n):
    fd = open("D:/Documents/Matières/Informatique 3/TP n°7/Images/exo3.pgm", "w")
    fd.write("P2\n" + str(n) + " " + str(n) + "\n" + str(n*2 - 1))
    for lig in range(1, n + 1):
        fd.write("\n")
        for col in range(n):
            fd.write(str(lig + col) + " ")
    fd.close()
carre(int(input()))
