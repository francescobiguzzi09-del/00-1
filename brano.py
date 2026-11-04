class Brano:
    def __init__(self, titolo: str, autore: str, durata: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    @property
    def titolo(self) -> str:
        return self._titolo
    
    @titolo.setter
    def titolo(self, valore: str) -> None:
        if not valore:
            raise ValueError("errore titolo")
        self._titolo = valore
    
    @property
    def autore(self) -> str:
        return self._autore
    
    @autore.setter
    def autore(self, valore: str) -> None:
        if not valore:
            raise ValueError("errore titolo")
        self._autore = valore
    
    @property
    def durata(self) -> int:
        return self._durata
    
    @durata.setter
    def durata(self, valore: int) -> None:
        if  valore <= 0:
            raise ValueError("errore titolo")
        self._durata = valore
    
    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} - {self.durata} s"
    def short_song(self) -> bool:
        if self.durata < 120:
            return True
        return False
    
