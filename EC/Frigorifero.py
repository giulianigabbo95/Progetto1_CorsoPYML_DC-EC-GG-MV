##from gg import Elettrodomestico
import Elettrodomestico from GG.Elettrodomestico


class Frigorifero(Elettrodomestico):
    
    def __init__(self, litri, ha_freezer):
        super().__init__()
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):
        costo = 35
        if self.litri > 300:
            costo += 25
        if self.ha_freezer:
            costo += 15
        return costo
    
