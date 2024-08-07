class Clan:
    
    def __init__(self, nazev_klanu: str, pocet_vojaku: int, specialni_zbrane: str, jidlo: int, voda: int, zije_klan:bool, is_ally: bool) -> None:
        self.nazev_klanu = nazev_klanu
        self.pocet_vojaku = pocet_vojaku
        self.specialni_zbrane = specialni_zbrane
        self.jidlo = jidlo
        self.voda = voda
        # self.munice = munice
        self.zije_klan = zije_klan
        self.is_ally = is_ally

    def __str__(self) -> str:
        return f"\nKLan {self.nazev_klanu}"
    
    def __repr__(self) -> str:
        return f"Klan: {self.nazev_klanu}\nvojaci: {self.pocet_vojaku}\nzbrane: {self.specialni_zbrane}\njidlo: {self.jidlo}\nvoda: {self.voda}\nzije_klan: {self.zije_klan}\nis_ally: {self.is_ally}"

# f"Clan(nazev_klanu: '{self.nazev_klanu}'vojaci: '{self.pocet_vojaku}'zbrane: '{self.specialni_zbrane}'jidlo: '{self.jidlo}'voda: '{self.voda}'munice: '{self.munice}')"
    

    def zasobyJidla():
        pass
        
        
        
        
        
        # 1 vojak = 1.8 jidla a 5.5 vody a  munice podle zbrani co pouzivaji ale nebudu to brat do detailu
class MainClan:
     
     def __init__(self) -> None:
         self.klany = []
         

     def pridatKlan(self, klan: str) -> None:
        if isinstance(klan, Clan):
            self.klany.append(klan)
        else:
            raise ValueError("chyba MainClan")
        
     def zobrazitKlany(self) -> None:
         for klan in self.klany:
             print(f"- {klan}")
    
     def utok(self, nepritel:str, **kwargs:list[str]):
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


# nebo 

class NepratelskeKlany(Clan):
    def __init__(self, obtiznost: str, nazev_klanu: str, pocet_vojaku: int, specialni_zbrane: str, jidlo: int, voda: int, zije_klan: bool, is_ally: bool) -> None:
        super().__init__(nazev_klanu, pocet_vojaku, specialni_zbrane, jidlo, voda, zije_klan, is_ally)
        self.obtiznost = obtiznost
        # tady by mohlo byt rovnou jestli jsou easy, normal, hard atd...
        # a podle nejakeho seznamu by se zjistilo kolik davaji poskozeni a kolik muzoy mit vojaku
        # napr easy = {  Drakthar: info   ,  Volkarim:info   }
        


