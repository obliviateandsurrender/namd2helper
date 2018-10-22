name1 = "metafile"
f1 = open(name1, "w")

for i in range(4, 31, 2):
    name2 = "nacl_us_" + str(i) + ".colvars.traj"
    f1.write(str(name2))
    f1.write(" ")
    f1.write(str(i))
    f1.write(" ")
    f1.write(str(3.0))
    f1.write("\n")

f1.close()
