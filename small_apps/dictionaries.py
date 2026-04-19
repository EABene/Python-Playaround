# Learning dictionaries here

# Erstellen -----

d = {}
d = dict()

# mit Inhalt -----

person = {"name": "John", "age": 25, "car": "VW Golf", "city": "Stockholm"}

person = {"name": "John",
          "age": 25,
          "car": "VW Golf",
          "city": "Stockholm"
          }

# Lesen -----

xa = person["name"]
b = person.get("name")
c = person.get("job", "N/A")

# Schreiben und Löschen -----

person["job"] = "Developer" # hinzufügen / überschreiben
del person["city"] # löschen - KeyError wenn nicht vorhanden
# person.pop("city") # löschen + Wert zurückgeben
person.pop("age", None) # löschen - kein Error wenn nicht vorhanden

# Iterieren -----

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items(): # am häufigsten und wichtigsten
    print(f"{key}: {value}")

# Nützliche Methoden -----

person.keys() # alle Keys
person.values() # alle Values
person.items() # alle Key-Value Paare
person.update({"country": "Austria", "hobby": "Sports"}) # mehrere Keys auf einmal updaten
check = "name" in person # True - Key existiert?
len(person) # Anzahl Einträge

# Nested Dictionaries -----

users = {
"user1" : {"name": "Mark", "age": 25},
"user2" : {"name": "Anna", "age": 23},
}
x = users["user1"]["name"]

# Dictionary Comprehension -----
# Quadratzahlen von 1 bis 5
squares = {x: x**2 for x in range(1, 6)}

# Quadratzahlen von 1 bis 10, aber nur gerade Zahlen
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# Zusammenführen -----

a = {"x": 1}
b = {"y": 2}
merged = a | b # merged = {'x': 1, 'y': 2}; Pipe Operator!
a |= b # a = {'x': 1, 'y': 2}
merged2 = {**a, **b} # merged2 = {'x': 1, 'y': 2} ** = unpacking operator. Entpackt Dict in einzelne Key-Value Paare

# setdefault -----

person.setdefault("job", "Unknown")
# Nützlich um KeyErrors zu vermeiden beim ersten Befüllen
# Key setzen NUR, wenn er noch nicht existiert

#Anwendung:
text = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}

for word in text:
    count.setdefault(word, 0)  # falls noch nicht vorhanden: auf 0 setzen
    count[word] += 1

# {'apple': 3, 'banana': 2, 'cherry': 1}

# Anwendung als tatsächliches Dict -----

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


operations = {
    "add": add,             # Konzept vergleichbar mit Pointer, ist Referenz auf die Funktion
    "subtract": subtract,
    "multiply": multiply,
}

user_input = "add"  # kommt z.B. vom User

operation = operations.get(user_input)

if operation is None:
    raise ValueError(f"Unknown operation: {user_input}")

result = operation(10, 5)
print(result)  # 15

# Konzept Functions as first class objects:
# "First-class" bedeutet: Funktionen können überall hin wo auch ein normaler Wert hin kann.




