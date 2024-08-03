class MainClan:
     
     def __init__(self):
         self.klany = []

     def pridatKlan(self, klan):
        if isinstance(klan, Clan):
            self.klany.append(klan)
        else:
            raise ValueError("chyba MainClan")
        
     def zobrazitKlany(self):
         for klan in self.klany:
             print(klan)





class Clan:
    
    def __init__(self, nazev_klanu, pocet_vojaku, specialni_zbrane, jidlo, voda, munice):
        self.nazev_klanu = nazev_klanu
        self.pocet_vojaku = pocet_vojaku
        self.specialni_zbrane = specialni_zbrane
        self.jidlo = jidlo
        self.voda = voda
        self.munice = munice
        # 1 vojak = 1.8 jidla a 5.5 vody a  munice podle zbrani co pouzivaji ale nebudu to brat do detailu


class EasyClans(Clan):
    pass



class NormalClans(Clan):
    pass



class HardClans(Clan):
    pass




class ExpertClans(Clan):
    pass




class InsaneClans(Clan):
    pass
