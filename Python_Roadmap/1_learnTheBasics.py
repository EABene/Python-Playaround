# =============================================================================
# PYTHON BASICS — ROADMAP CHEAT SHEET
# =============================================================================


# -----------------------------------------------------------------------------
# 1. BASIC SYNTAX
# -----------------------------------------------------------------------------

# Einrückung statt geschweifter Klammern
if True:
    print("Indentation matters!")  # 4 Spaces Standard

# Kommentare: # einzeilig, ''' ... ''' mehrzeilig
"""
Mehrzeiliger Kommentar / Docstring
"""

# Semikolons sind optional (und unüblich)
x = 1; y = 2  # möglich, aber nicht empfohlen

# print() mit sep und end
print("Hallo", "Welt", sep="-", end="!\n")  # Hallo-Welt!


# -----------------------------------------------------------------------------
# 2. VARIABLES AND DATA TYPES
# -----------------------------------------------------------------------------

# Dynamisch typisiert — kein expliziter Typ nötig
i = 42           # int
f = 3.14         # float
c = 2 + 3j       # complex
b = True         # bool
s = "Text"       # str
n = None         # NoneType

# Typ prüfen
print(type(i))       # <class 'int'>
print(isinstance(i, int))  # True

# Mehrfachzuweisung
a, b, c = 1, 2, 3
x = y = z = 0


# -----------------------------------------------------------------------------
# 3. WORKING WITH STRINGS
# -----------------------------------------------------------------------------

name = "John"
greeting = f"Hallo, {name}!"   # f-String (empfohlen)
greeting2 = "Hallo, %s!" % name  # alt: %-Formatting
greeting3 = "Hallo, {}!".format(name)  # str.format()

# Wichtige String-Methoden
s = "  hallo welt  "
print(s.strip())          # "hallo welt"
print(s.upper())          # "  HALLO WELT  "
print(s.replace("welt", "python"))
print("hallo".startswith("ha"))   # True
print("welt".endswith("lt"))      # True
print(",".join(["a", "b", "c"]))  # "a,b,c"
print("a,b,c".split(","))         # ['a', 'b', 'c']

# Slicing
s = "Python"
print(s[0])      # P
print(s[-1])     # n
print(s[1:4])    # yth
print(s[::-1])   # nohtyP (reversed)

# String-Eigenschaften
print(len("Python"))    # 6
print("py" in "python") # True


# -----------------------------------------------------------------------------
# 4. CONDITIONALS
# -----------------------------------------------------------------------------

age = 20

if age < 18:
    print("Minderjährig")
elif age == 18:
    print("Gerade volljährig")
else:
    print("Volljährig")

# Ternary (one-liner)
status = "adult" if age >= 18 else "minor"

# match-case (ab Python 3.10)
command = "quit"
match command:
    case "quit":
        print("Beenden")
    case "help":
        print("Hilfe")
    case _:
        print("Unbekannter Befehl")

# Vergleichs- & logische Operatoren
# ==, !=, <, >, <=, >=
# and, or, not
# is (Identität), in (Mitgliedschaft)
print(1 == 1 and 2 > 1)  # True
print(None is None)       # True


# -----------------------------------------------------------------------------
# 5. LOOPS
# -----------------------------------------------------------------------------

# for-Loop
for i in range(5):        # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i, end=" ")
print()

# while-Loop
n = 3
while n > 0:
    print(n, end=" ")
    n -= 1
print()

# break / continue / else
for i in range(10):
    if i == 3:
        continue   # überspringen
    if i == 6:
        break      # abbrechen
    print(i, end=" ")
else:
    print("Loop normal beendet")  # nur ohne break
print()

# enumerate & zip
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)


# -----------------------------------------------------------------------------
# 6. TYPE CASTING
# -----------------------------------------------------------------------------

# Explizite Umwandlung
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(100))          # "100"
print(bool(0))           # False
print(bool("text"))      # True
print(list((1, 2, 3)))   # [1, 2, 3]
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 1, 2, 3])) # {1, 2, 3}

# Vorsicht bei Konvertierungen
# int("3.14") → ValueError! → erst float(), dann int()
print(int(float("3.14")))  # 3


# -----------------------------------------------------------------------------
# 7. EXCEPTIONS
# -----------------------------------------------------------------------------

# try / except / else / finally
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehler: {e}")
except (TypeError, ValueError) as e:
    print(f"Typ/Value-Fehler: {e}")
else:
    print("Kein Fehler!")    # nur wenn kein except ausgelöst
finally:
    print("Wird immer ausgeführt")

# Eigene Exception werfen
def check_age(age):
    if age < 0:
        raise ValueError(f"Ungültiges Alter: {age}")
    return age

# Eigene Exception-Klasse
class CustomError(Exception):
    pass

# Häufige Built-in Exceptions
# ValueError, TypeError, KeyError, IndexError,
# FileNotFoundError, ZeroDivisionError, AttributeError


# -----------------------------------------------------------------------------
# 8. FUNCTIONS & BUILT-IN FUNCTIONS
# -----------------------------------------------------------------------------

# Definition
def greet(name, greeting="Hallo"):   # Default-Parameter
    """Gibt eine Begrüßung zurück."""  # Docstring
    return f"{greeting}, {name}!"

print(greet("Benedikt"))
print(greet("Benedikt", greeting="Hey"))

# *args und **kwargs
def variadic(*args, **kwargs):
    print(args)    # Tuple
    print(kwargs)  # Dict

variadic(1, 2, 3, lang="Python", version=3)

# Lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Wichtige Built-in Functions
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))          # 8
print(min(nums))          # 1
print(max(nums))          # 9
print(sum(nums))          # 31
print(sorted(nums))       # aufsteigend sortiert
print(sorted(nums, reverse=True))  # absteigend
print(list(reversed(nums)))
print(list(map(lambda x: x * 2, nums)))    # jedes Element verdoppeln
print(list(filter(lambda x: x > 3, nums))) # nur Elemente > 3
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(abs(-7))            # 7
print(round(3.567, 2))    # 3.57


# -----------------------------------------------------------------------------
# 9. LISTS
# -----------------------------------------------------------------------------

lst = [1, 2, 3, 4, 5]

# Zugriff & Slicing
print(lst[0])      # 1
print(lst[-1])     # 5
print(lst[1:3])    # [2, 3]

# Methoden
lst.append(6)          # anhängen
lst.insert(0, 0)       # an Position einfügen
lst.remove(3)          # erstes Vorkommen entfernen
popped = lst.pop()     # letztes Element entfernen & zurückgeben
lst.sort()             # in-place sortieren
lst.reverse()          # in-place umkehren
print(lst.index(2))    # Index des Wertes
print(lst.count(1))    # Anzahl Vorkommen
lst2 = lst.copy()      # flache Kopie
lst.extend([7, 8])     # Liste erweitern

# List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
print(squares)
print(evens)


# -----------------------------------------------------------------------------
# 10. TUPLES
# -----------------------------------------------------------------------------

t = (1, 2, 3)
t_single = (42,)   # Achtung: Komma nötig für Single-Element-Tuple!

# Unveränderlich (immutable) → kein append, remove, etc.
print(t[0])         # 1
print(t[-1])        # 3
print(len(t))       # 3
print(2 in t)       # True

# Unpacking
a, b, c = t
first, *rest = (1, 2, 3, 4, 5)   # *rest = [2, 3, 4, 5]

# Tuples als Dictionary-Keys nutzbar (Listen nicht!)
coords = {(0, 0): "Ursprung", (1, 0): "Rechts"}

# Named Tuple (für lesbareren Code)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)    # 3 4


# -----------------------------------------------------------------------------
# 11. SETS
# -----------------------------------------------------------------------------

s = {1, 2, 3, 3, 2}   # Duplikate werden entfernt
print(s)               # {1, 2, 3}

s.add(4)
s.remove(2)            # KeyError wenn nicht vorhanden
s.discard(99)          # kein Fehler wenn nicht vorhanden

# Mengenoperationen
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)     # Vereinigung:    {1, 2, 3, 4, 5, 6}
print(a & b)     # Schnittmenge:   {3, 4}
print(a - b)     # Differenz:      {1, 2}
print(a ^ b)     # Sym. Differenz: {1, 2, 5, 6}

# Membership-Test ist O(1) → viel schneller als bei Listen!
print(3 in a)    # True

# Set Comprehension
s = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}


# -----------------------------------------------------------------------------
# 12. DICTIONARIES
# -----------------------------------------------------------------------------

d = {"name": "Joe", "age": 29, "lang": "Python"}

# Zugriff
print(d["name"])           # Joe
print(d.get("age"))        # 29
print(d.get("x", "N/A"))   # N/A (kein KeyError)

# Hinzufügen / Ändern / Löschen
d["city"] = "Krems"
d["age"] = 28
del d["lang"]
removed = d.pop("city")    # entfernen & zurückgeben

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key}: {value}")

print(list(d.keys()))
print(list(d.values()))

# Nützliche Methoden
d.update({"x": 1, "y": 2})   # mehrere Keys auf einmal setzen
d2 = d.copy()                 # flache Kopie
d.setdefault("z", 0)          # nur setzen wenn Key fehlt

# Dict Comprehension
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging (ab Python 3.9)
merged = d | {"new_key": "new_val"}