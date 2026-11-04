from typing import List, Optional
class CD:
    def __init__(self, titolo: str, autore: str, brani: List[Brano]):
        self.titolo = titolo
        self. autore = autore
        self.brani = brani

        
    @property
    def durata_totale(self) -> int:
        durata_totale = 0
        for brano in self.brani:
            durata_totale += brano.durata
        return durata_totale
    
    def aggiungi_brano(self, brano: Brano) -> None:
        self.brani.append(brano)
    def __str__(self) -> str:
        brani = [str(brano) for brano in self.brani] 
        return f"CD: {self.titolo} di {self.autore}\n- " + "\n- ".join(descrizione)
    
    