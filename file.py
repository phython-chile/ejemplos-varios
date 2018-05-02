
f=open("ejemplo.csv","w")
f.write("rut,nombre \n")


print "Iniciando"
for i in range(1, 21000):
    print i
    f.write(str(i) + ",24063999-6,FALCONSOLUTIONS\n")

f.close()
print "Terminado"