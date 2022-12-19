kreklsk=int(input("Ievadiet kreklu daudzumu: "))
kreklzim=int(input("Ievadiet printa tipu (teksts - 1, zime - 2, foto - 3): "))
if kreklzim==1:
  printcena = 5
elif kreklzim==2:
  printcena = 7
elif kreklzim==3:
  printcena = 20
else:
  printcena = 0
  print("Nav tada printa, neiespējams veikt pasūtījumu ")
pascena=kreklsk*printcena
if pascena<50 and kreklzim>0 and kreklzim<4:
  pascena=pascena+15
  print("par piegādi papildus jāmaksā 15 EUR")
print("Pasutijuma cena =", pascena, "euro") 
if pascena>50 or pascena==50:
  pascena=pascena
  print("bezmaksas piegāde")
if pascena>100:
   print("Jums pienākas 5% atlaide! pasutijuma cena:", pascena/100*95,"euro")