

class Instrument:
    def __init__(self, name, stimmung):
        self.name = name
        self.stimmung = stimmung
        self.ist_gestimmt = False

    def stimmen(self):
        self.ist_gestimmt = True
        return f"{self.name} ({self.stimmung}) wurde gestimmt."

    def status(self):
        if self.ist_gestimmt:
            return f"{self.name} ist gestimmt."
        else:
            return f"{self.name} ist nicht gestimmt."



a = Instrument("Trompete", "Bb")
b = Instrument("Gitarre", "C")

print(a.status())
print(a.stimmen())
print(a.status())

print(b.status())
print(b.stimmen())
print(b.status())