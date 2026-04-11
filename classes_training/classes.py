# Einführung in Classes

class Gitarre:
    def __init__(self, marke, saitenanzahl):
        self.marke = marke
        self.saitenanzahl = saitenanzahl

    def beschreibung(self):
        return f"{self.marke} mit {self.saitenanzahl} Saiten"

meine_gitarre = Gitarre("Fender", 6)
print(meine_gitarre.beschreibung())  # → Fender mit 6 Saiten






"""
__init__ – der Konstruktor: wird automatisch beim Erstellen einer Instanz aufgerufen
self – Referenz auf die aktuelle Instanz (entspricht this in anderen Sprachen)
Attribut – eine Variable, die zu einer Instanz gehört (self.marke)
Methode – eine Funktion innerhalb einer Klasse 
"""