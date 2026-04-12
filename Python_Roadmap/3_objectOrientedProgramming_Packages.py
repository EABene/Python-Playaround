# =============================================================================
# PYTHON — OOP & PACKAGE MANAGERS CHEAT SHEET
# =============================================================================


# =============================================================================
# PART 1: OBJECT ORIENTED PROGRAMMING
# =============================================================================


# -----------------------------------------------------------------------------
# 1. CLASSES
# -----------------------------------------------------------------------------

class Animal:
    # Klassenattribut — geteilt von allen Instanzen
    kingdom = "Animalia"

    def __init__(self, name: str, age: int):
        # Instanzattribute — individuell pro Objekt
        self.name = name
        self.age = age
        self._energy = 100       # _ = konventionell "intern" (soft private)
        self.__id = id(self)     # __ = Name Mangling (hard private)

    def __str__(self):
        """Für print() — lesbare Darstellung"""
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self):
        """Für Debugging — technische Darstellung"""
        return f"Animal({self.name!r}, {self.age!r})"

    def __len__(self):
        return self.age

    def __eq__(self, other):
        return isinstance(other, Animal) and self.name == other.name

# Instanz erstellen
a = Animal("Rex", 5)
print(a)             # Animal(name=Rex, age=5)
print(repr(a))       # Animal('Rex', 5)
print(len(a))        # 5
print(a.kingdom)     # Animalia (Klassenattribut)

# Wichtige Dunder-Methoden (Magic Methods)
# __init__     Konstruktor
# __str__      str(obj) / print(obj)
# __repr__     repr(obj) / Debugging
# __len__      len(obj)
# __eq__       obj1 == obj2
# __lt__       obj1 < obj2  (für sorting)
# __add__      obj1 + obj2
# __contains__ item in obj
# __call__     obj()  (Instanz aufrufbar machen)
# __enter__ / __exit__   Context Manager (with-Statement)


# -----------------------------------------------------------------------------
# 2. METHODS
# -----------------------------------------------------------------------------

class BankAccount:
    interest_rate = 0.03   # Klassenattribut

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance

    # Instance Method — hat Zugriff auf self
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Betrag muss positiv sein")
        self._balance += amount
        print(f"Einzahlung: €{amount:.2f} → Guthaben: €{self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Nicht genug Guthaben")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    # Class Method — hat Zugriff auf cls, nicht self
    # Typischer Use-Case: alternative Konstruktoren
    @classmethod
    def from_string(cls, data: str) -> "BankAccount":
        owner, balance = data.split(":")
        return cls(owner, float(balance))

    @classmethod
    def set_interest_rate(cls, rate: float) -> None:
        cls.interest_rate = rate

    # Static Method — kein Zugriff auf self oder cls
    # Nur logisch zur Klasse gehörig, aber unabhängig
    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    # Property — Zugriff wie Attribut, Logik wie Methode
    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Guthaben kann nicht negativ sein")
        self._balance = value

    def __str__(self):
        return f"BankAccount({self.owner}, €{self._balance:.2f})"


acc = BankAccount("Benedikt", 1000)
acc.deposit(500)
print(acc.balance)           # 1500.0 (via @property)
acc.balance = 2000           # via @balance.setter
print(BankAccount.validate_amount(-5))   # False (static)

acc2 = BankAccount.from_string("Anna:250.0")   # classmethod
print(acc2)


# -----------------------------------------------------------------------------
# 3. INHERITANCE
# -----------------------------------------------------------------------------

class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def start(self) -> str:
        return f"{self.make} {self.model} startet..."

    def info(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def __str__(self):
        return self.info()


class Car(Vehicle):
    def __init__(self, make, model, year, doors: int = 4):
        super().__init__(make, model, year)   # Elternklasse initialisieren
        self.doors = doors

    def start(self) -> str:                    # Override
        base = super().start()
        return f"{base} (Motor läuft)"

    def honk(self) -> str:
        return "Huup!"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kwh: float):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def start(self) -> str:                    # Override der Override
        return f"{self.make} {self.model} startet lautlos..."

    def charge_status(self) -> str:
        return f"Akku: {self.battery_kwh} kWh"


car = Car("Toyota", "Corolla", 2022)
ecar = ElectricCar("Tesla", "Model 3", 2024, 75.0)

print(car.start())         # Toyota Corolla startet... (Motor läuft)
print(ecar.start())        # Tesla Model 3 startet lautlos...
print(ecar.honk())         # Huup! (geerbt von Car)
print(ecar.info())         # 2024 Tesla Model 3 (geerbt von Vehicle)

# isinstance & issubclass
print(isinstance(ecar, ElectricCar))  # True
print(isinstance(ecar, Car))          # True  (Vererbungskette!)
print(isinstance(ecar, Vehicle))      # True
print(issubclass(ElectricCar, Car))   # True

# MRO — Method Resolution Order (Reihenfolge der Methodensuche)
print(ElectricCar.__mro__)
# (ElectricCar, Car, Vehicle, object)

# Mehrfachvererbung (Multiple Inheritance)
class Flyable:
    def fly(self):
        return "Fliegt!"

class Swimmable:
    def swim(self):
        return "Schwimmt!"

class Duck(Flyable, Swimmable, Animal):
    def __init__(self, name):
        Animal.__init__(self, name, age=1)

    def quack(self):
        return "Quack!"

donald = Duck("Donald")
print(donald.fly())    # Fliegt!
print(donald.swim())   # Schwimmt!
print(donald.quack())  # Quack!


# -----------------------------------------------------------------------------
# 4. ENCAPSULATION
# -----------------------------------------------------------------------------

# Encapsulation = Daten und Methoden bündeln, Zugriff kontrollieren

class Temperature:
    def __init__(self, celsius: float):
        self._celsius = None         # initialisieren
        self.celsius = celsius       # setter aufrufen

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError(f"Unterhalb des absoluten Nullpunkts: {value}")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5/9    # Validierung via celsius-setter

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    def __str__(self):
        return f"{self._celsius:.2f}°C / {self.fahrenheit:.2f}°F / {self.kelvin:.2f}K"


t = Temperature(100)
print(t)                  # 100.00°C / 212.00°F / 373.15K
t.fahrenheit = 32
print(t.celsius)          # 0.0
# t.celsius = -300        # ValueError!

# Konventionen für Sichtbarkeit:
# name       → public      (kein Schutz)
# _name      → protected   (Konvention: "nicht von außen nutzen")
# __name     → private     (Name Mangling: _ClassName__name)

class Secret:
    def __init__(self):
        self.public = "jeder"
        self._protected = "bitte nicht"
        self.__private = "wirklich nicht"

    def reveal(self):
        return self.__private    # intern kein Problem

s = Secret()
print(s.public)            # "jeder"
print(s._protected)        # geht, aber Konvention verletzt
# print(s.__private)       # AttributeError!
print(s._Secret__private)  # geht — Name Mangling, aber bitte nicht


# Dataclasses — moderner, weniger Boilerplate
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "P"
    tags: list = field(default_factory=list)   # mutable default!

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3.0, 4.0)
print(p)                       # Point(x=3.0, y=4.0, label='P', tags=[])
print(p.distance_to_origin())  # 5.0
# __init__, __repr__, __eq__ werden automatisch generiert!

@dataclass(frozen=True)   # immutable — wie namedtuple aber moderner
class ImmutablePoint:
    x: float
    y: float


# =============================================================================
# PART 2: PACKAGE MANAGERS
# =============================================================================

# -----------------------------------------------------------------------------
# KONZEPT: Was macht ein Package Manager?
# -----------------------------------------------------------------------------
#
# 1. Pakete installieren / deinstallieren / updaten
# 2. Abhängigkeiten auflösen (Dependencies)
# 3. Virtuelle Umgebungen verwalten (Isolation)
# 4. Reproduzierbare Builds sicherstellen (Lock Files)
#
# PyPI (Python Package Index) = das zentrale Repository für Python-Pakete
# → https://pypi.org — hier landen alle öffentlichen Pakete
# → alle Tools unten laden standardmäßig von PyPI


# -----------------------------------------------------------------------------
# PIP — der Standard (kommt mit Python)
# -----------------------------------------------------------------------------

# Installation
# pip install requests
# pip install requests==2.31.0       # spezifische Version
# pip install "requests>=2.28,<3"    # Versionsbereich
# pip install -r requirements.txt    # aus Datei installieren
# pip install -e .                   # editable install (eigenes Projekt)

# Verwaltung
# pip list                           # installierte Pakete
# pip show requests                  # Details zu einem Paket
# pip freeze > requirements.txt      # aktuellen Stand exportieren
# pip uninstall requests
# pip install --upgrade requests

# requirements.txt (manuell oder via pip freeze)
# requests==2.31.0
# flask>=3.0
# sqlalchemy

# Nachteil: kein Lock File, kein integriertes venv-Management


# -----------------------------------------------------------------------------
# VENV — virtuelle Umgebung (immer verwenden!)
# -----------------------------------------------------------------------------

# python -m venv .venv               # venv erstellen
# source .venv/bin/activate          # aktivieren (Mac/Linux)
# .venv\Scripts\activate             # aktivieren (Windows)
# deactivate                         # deaktivieren

# Warum?
# → Jedes Projekt hat eigene, isolierte Abhängigkeiten
# → Keine Konflikte zwischen Projekten
# → pip installiert dann nur in diese Umgebung


# -----------------------------------------------------------------------------
# UV — modernes, extrem schnelles Tool (empfohlen für neue Projekte)
# -----------------------------------------------------------------------------

# Geschrieben in Rust → 10-100x schneller als pip
# Ersetzt pip + venv + pip-tools in einem Tool
# Drop-in Replacement für pip-Befehle

# Installation
# curl -LsSf https://astral.sh/uv/install.sh | sh   (Mac/Linux)
# winget install --id=astral-sh.uv                   (Windows)

# Projekt starten
# uv init my_project                 # neues Projekt
# uv venv                            # venv erstellen
# uv add requests                    # Paket hinzufügen (wie pip install)
# uv remove requests
# uv sync                            # alle Dependencies installieren (aus uv.lock)
# uv run python script.py            # Skript in venv ausführen

# uv.lock — automatisch generierter Lock File
# → 100% reproduzierbare Umgebungen
# → in Git einchecken!

# pyproject.toml — moderne Projektkonfiguration
# [project]
# name = "my-project"
# version = "0.1.0"
# dependencies = ["requests>=2.31"]


# -----------------------------------------------------------------------------
# POETRY — bekanntes Dependency-Management + Packaging Tool
# -----------------------------------------------------------------------------

# Gut für: Bibliotheken die auf PyPI veröffentlicht werden sollen,
#           Projekte mit komplexen Abhängigkeitsbäumen

# Installation
# curl -sSL https://install.python-poetry.org | python3 -

# Workflow
# poetry new my_project              # neues Projekt
# poetry init                        # in bestehendem Verzeichnis
# poetry add requests                # Paket hinzufügen
# poetry add pytest --group dev      # nur für Entwicklung
# poetry remove requests
# poetry install                     # aus poetry.lock installieren
# poetry run python script.py
# poetry shell                       # venv aktivieren
# poetry update                      # Dependencies updaten
# poetry build                       # Paket bauen (.whl, .tar.gz)
# poetry publish                     # auf PyPI veröffentlichen

# pyproject.toml (Poetry-Format):
# [tool.poetry.dependencies]
# python = "^3.11"
# requests = "^2.31"
#
# [tool.poetry.group.dev.dependencies]
# pytest = "^8.0"


# -----------------------------------------------------------------------------
# PDM — modernes Tool, strikt PEP-konform
# -----------------------------------------------------------------------------

# Ähnlich wie Poetry, aber näher am offiziellen Python-Standard (PEP 517/518/621)
# Kein eigenes venv nötig — nutzt __pypackages__ (PEP 582, optional)

# pip install pdm
# pdm init
# pdm add requests
# pdm remove requests
# pdm install
# pdm run python script.py
# pdm update


# -----------------------------------------------------------------------------
# CONDA — für Data Science / Scientific Computing
# -----------------------------------------------------------------------------

# Nicht nur Python-Pakete — auch C/C++ Bibliotheken, CUDA, etc.
# Eigenes Paket-Ökosystem (conda-forge, defaults)
# Schwergewichtig, aber unverzichtbar für ML/Data Science

# conda create -n myenv python=3.11
# conda activate myenv
# conda install numpy pandas scikit-learn
# conda install -c conda-forge package_name  # aus community channel
# conda deactivate
# conda env export > environment.yml
# conda env create -f environment.yml

# Miniconda = minimale Installation (empfohlen)
# Anaconda  = Miniconda + viele vorinstallierte Data Science Pakete


# -----------------------------------------------------------------------------
# ZUSAMMENFASSUNG: Welches Tool wann?
# -----------------------------------------------------------------------------
#
# ┌─────────────┬──────────────────────────────────────────────────────┐
# │ Tool        │ Wann verwenden                                       │
# ├─────────────┼──────────────────────────────────────────────────────┤
# │ pip + venv  │ Einfache Skripte, kein Lock File nötig               │
# │ uv          │ Neue Projekte — schnell, modern, empfohlen           │
# │ Poetry      │ Bibliotheken auf PyPI veröffentlichen                │
# │ pdm         │ Strikt PEP-konform, ähnlich wie Poetry               │
# │ conda       │ Data Science, ML, wissenschaftliches Rechnen         │
# └─────────────┴──────────────────────────────────────────────────────┘
#
# Für Backend-Entwicklung: uv ist aktuell die beste Wahl
# → schnell, Lock File, pyproject.toml, aktiv entwickelt