from definice_class import *
start_vojaci = 20
start_jidlo = 50 # kg ale jeste bych to zmenil
start_voda = 50 # v litrech
start_munice = 200 # naboju 
# 1 vojak = 1.8 jidla a 5.5 vody
nazev_hracova_klanu = input("Zadej jmeno sveho klanu")
hracuvKlan = Clan(nazev_hracova_klanu, 20, "zadne", 100, 100, 200 )
hlavni_Klan = MainClan()

hlavni_Klan.pridatKlan(hracuvKlan)