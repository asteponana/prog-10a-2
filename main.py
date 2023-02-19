##3.uzd
# alga = int(input("Uzrakstiet Jusu algu :"))
# klientsk = int(input("Uzrakstiet apkalpoto klientu skaitu:")) 
# if klientsk >= 5:
#   algafinal = alga + alga/100*25
#   algabonus = alga/100*25
#   print("Jusu finala alga:", algafinal)
# if klientsk >= 5:
#   print("Bonuss ir", algabonus, "euro")
# if klientsk < 5:
#     print("Bonusa nav :(, Jusu alga ir - ", alga, "euro") 
##5.uzd
# day = int(input("Uzrakstiet dienas kārtas numuru :"))
# if day > 365 or day < 0:
#   print("Neeksistē")
# if day > 0 and day <= 31:
#   print("Janvaris", day, "skaitlis")
# if day > 31 and day <= 59:
#   print("Februāris", day-31, "skaitlis")
# if day > 59 and day <= 90:
#   print("Marts", day-59, "skaitlis")
# if day > 90 and day <= 120:
#   print("Aprīlis",day-90, "skaitlis")
# if day > 120 and day <= 151:
#   print("Maijs",day-120, "skaitlis")
# if day > 151 and day <= 181:
#   print("Jūnijs",day-151, "skaitlis")
# if day > 181 and day <= 212:
#   print("Jūlijs",day-181, "skaitlis")
# if day > 212 and day <= 243:
#   print("Augusts",day-212, "skaitlis")
# if day > 243 and day <= 273:
#   print("Septembris",day-243, "skaitlis")
# if day > 273 and day <= 304:
#   print("Oktobtis",day-273, "skaitlis")
# if day > 304 and day <= 334:
#   print("Novembris",day-304, "skaitlis")
# if day > 334 and day <= 365:
#   print("Decembris",day-334, "skaitlis") 
##6.uzd
# stur1 = int(input("1. sturis:"))
# stur2 = int(input("2. sturis:"))
# stur3 = int(input("3. sturis:"))
# if stur1+stur2+stur3 > 180 or stur1+stur2+stur3 <= 0 or stur1+stur2+stur3 < 180:
#   print("Neeksitē?")
# if stur1 == 90 and stur1+stur2+stur3 == 180 or stur2 == 90  and stur1+stur2+stur3 == 180 or stur3 == 90 and stur1+stur2+stur3 == 180 :
#   print("Taisnleņķa trissturis")
# if stur1 > 90 and stur1+stur2+stur3 == 180 or stur2 > 90 and stur1+stur2+stur3 == 180 or stur3 > 90 and stur1+stur2+stur3 == 180:
#   print("Platleņķa trissturis")
#   print("vienadmalu trissturis") 
##8.uzd
# skaitlis = int(input("Jusu skaitlis - (_)! "))
# if stur1==stur2==stur3 and stur1+stur2+stur3 == 180:
#   print("vienadmalu trissturis") 
##8.uzd
# skaitlis = int(input("Jusu skaitlis - (_)! "))
# factorial = 1
# while skaitlis > 1:
#     factorial *= skaitlis
#     skaitlis -= 1
# print(factorial)