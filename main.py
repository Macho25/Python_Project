from definice_class import *
from Database_klanu import *
start_vojaci = 20
start_jidlo = 50 # kg ale jeste bych to zmenil
start_voda = 50 # v litrech
start_munice = 200 # naboju 
# 1 vojak = 1.8 jidla a 5.5 vody

nazev_hracova_klanu = input("Zadej jmeno sveho klanu: ")
hracuvKlan = Clan(nazev_hracova_klanu, 20, "zadne", 100, 100, 200 )
hlavni_Klan = MainClan()

hlavni_Klan.pridatKlan(hracuvKlan)  

# Drakthar = EasyClans("Drakthar", 5, "zadne", 20, 20, 50)
# hlavni_Klan.pridatKlan(Drakthar)
# hlavni_Klan.zobrazitKlany()
# print(repr(hracuvKlan))
# print(repr(Drakthar))

# Hlavni Menu

print("Vitej ve hre")
print("jak se hraje:\n'zasoby' zjistis kolik ma tvuj klan aktualne mnozstvi zasob")
print("'utok nazev_klanu' timto prikazem zautocis na klan v tve oblasti")
print("'pridel' prejdes do modu kde zacnes pridelovat svym klanum jidlo a vodu podle jejich potreby")
hracova_volba = input("> ")
match hracova_volba:

    case "zasoby":
        pass
    
    case "utok":
        pass

    case "pridel":
        pass



