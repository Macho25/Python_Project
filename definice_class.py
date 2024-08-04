class Clan:
    
    def __init__(self, nazev_klanu, pocet_vojaku, specialni_zbrane, jidlo=0, voda=0, munice=0):
        self.nazev_klanu = nazev_klanu
        self.pocet_vojaku = pocet_vojaku
        self.specialni_zbrane = specialni_zbrane
        self.jidlo = jidlo
        self.voda = voda
        self.munice = munice
        self.status_klanu = True

    def __str__(self):
        return f"\nKLan {self.nazev_klanu}"
    
    def __repr__(self):
        return f"Klan: {self.nazev_klanu}\nvojaci: {self.pocet_vojaku}\nzbrane: {self.specialni_zbrane}\njidlo: {self.jidlo}\nvoda: {self.voda}\nmunice: {self.munice}"

# f"Clan(nazev_klanu: '{self.nazev_klanu}'vojaci: '{self.pocet_vojaku}'zbrane: '{self.specialni_zbrane}'jidlo: '{self.jidlo}'voda: '{self.voda}'munice: '{self.munice}')"
    

    def zasobyJidla():
        pass
        
        
        
        
        
        # 1 vojak = 1.8 jidla a 5.5 vody a  munice podle zbrani co pouzivaji ale nebudu to brat do detailu
class MainClan:
     
     def __init__(self):
         self.klany = []
         self.status_klanu = True

     def pridatKlan(self, klan):
        if isinstance(klan, Clan):
            self.klany.append(klan)
        else:
            raise ValueError("chyba MainClan")
        
     def zobrazitKlany(self):
         for klan in self.klany:
             print(f"- {klan}")
    
     def utok(self, nepritel, **kwargs):
        pass
    

     def pridelJidel(self):
         pass






class EasyClans(Clan):
    # Drakthar = 'Drakthar'
    # Volkarim = 'Volkarim'
    # Grimthor = 'Grimthor'
    # Zantril = 'Zantril'
    # Ravendark = 'Ravendark'
    pass



class NormalClans(Clan):
    # Falthorn = 'Falthorn'
    # Gorath = 'Gorath'
    # Vexarim = 'Vexarim'
    # Tarkhul = 'Tarkhul'
    # Brimvald = 'Brimvald'
    pass



class HardClans(Clan):
    # Korveth = 'Korveth'
    # Myrkal = 'Myrkal'
    # Thragorn = 'Thragorn'
    # Xandor = 'Xandor'
    # Kharzul = 'Kharzul'
    pass




class ExpertClans(Clan):
    # Zarath = 'Zarath'
    # Vorthak = 'Vorthak'
    # Draelith = 'Draelith'
    # Maraxus = 'Maraxus'
    # Nalthor = 'Nalthor'
    pass




class InsaneClans(Clan):
    pass







