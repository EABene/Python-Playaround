# =============================================================================
# PYTHON INTERMEDIATE — ROADMAP CHEAT SHEET
# Data Structures & Algorithms + Advanced Concepts
# =============================================================================


# -----------------------------------------------------------------------------
# 1. ARRAYS AND LINKED LISTS
# -----------------------------------------------------------------------------

# Python hat kein natives "Array" — list ist der Standard
# Für echte Arrays (typisiert, performant): array-Modul oder numpy

import array
arr = array.array("i", [1, 2, 3, 4])   # 'i' = signed int
arr.append(5)
print(arr)   # array('i', [1, 2, 3, 4, 5])

# List als dynamisches Array (das nutzt man in der Praxis)
lst = [1, 2, 3]
lst.append(4)     # O(1) amortisiert
lst.insert(0, 0)  # O(n) — alle Elemente verschieben
lst.pop()         # O(1)
lst.pop(0)        # O(n) — deshalb: deque für Queues verwenden!

# Linked List — in Python manuell implementiert
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()   # 1 → 2 → 3 → None


# -----------------------------------------------------------------------------
# 2. HASHMAPS
# -----------------------------------------------------------------------------

# Python dict IST eine HashMap (Hash Table unter der Haube)
# Durchschnittlich O(1) für get, set, delete

hashmap = {}
hashmap["key"] = "value"
print(hashmap.get("key"))        # "value"
print(hashmap.get("missing", "default"))   # "default"

# Typischer Anwendungsfall: Häufigkeiten zählen
from collections import Counter, defaultdict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = Counter(words)
print(freq)                        # Counter({'apple': 3, 'banana': 2, ...})
print(freq.most_common(2))         # [('apple', 3), ('banana', 2)]

# defaultdict: kein KeyError bei fehlendem Key
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print(dd)   # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# OrderedDict (ab Python 3.7 behält dict Einfügereihenfolge — meist unnötig)
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])


# -----------------------------------------------------------------------------
# 3. HEAPS, STACKS AND QUEUES
# -----------------------------------------------------------------------------

# --- STACK (LIFO) ---
# Einfach mit list: append() = push, pop() = pop
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack.pop())   # "c"
print(stack.pop())   # "b"

# --- QUEUE (FIFO) ---
# list.pop(0) ist O(n) — stattdessen: deque verwenden!
from collections import deque

queue = deque()
queue.append("a")     # enqueue rechts
queue.append("b")
queue.append("c")
print(queue.popleft())   # "a" — O(1)
print(queue.popleft())   # "b"

# deque kann auch als Stack verwendet werden (appendleft / popleft)

# --- HEAP (Priority Queue) ---
# Python: Min-Heap via heapq (kleinstes Element immer oben)
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heapq.heappop(heap))   # 1 (kleinster Wert)
print(heapq.heappop(heap))   # 3

# Max-Heap: Werte negieren
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))   # 5 (größter Wert)

# Liste zur Heap umwandeln
nums = [3, 1, 4, 1, 5, 9]
heapq.heapify(nums)
print(nums)   # gültige Heap-Struktur


# -----------------------------------------------------------------------------
# 4. BINARY SEARCH TREE (BST)
# -----------------------------------------------------------------------------

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return BSTNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if val == node.val:
                return True
            return _search(node.left, val) if val < node.val else _search(node.right, val)
        return _search(self.root, val)

    def inorder(self):
        """Inorder-Traversal liefert sortierte Reihenfolge"""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result

bst = BST()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

print(bst.inorder())       # [1, 3, 4, 5, 6, 7, 8]
print(bst.search(4))       # True
print(bst.search(99))      # False

# BST-Eigenschaften:
# - Suchen / Einfügen / Löschen: O(log n) im Durchschnitt, O(n) im Worst Case
# - Inorder-Traversal ergibt sortierte Sequenz


# -----------------------------------------------------------------------------
# 5. RECURSION
# -----------------------------------------------------------------------------

# Basiskonzept: Funktion ruft sich selbst auf
# Immer zwei Teile: Base Case + Recursive Case

def factorial(n):
    if n <= 1:      # Base Case
        return 1
    return n * factorial(n - 1)   # Recursive Case

print(factorial(5))   # 120

# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))   # 55  (aber: O(2^n) — sehr langsam für große n!)

# Memoization mit lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(fib_memo(50))   # schnell! O(n)

# Rekursion mit Datenstrukturen
def flatten(lst):
    """Verschachtelte Liste flach machen"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], 5]))   # [1, 2, 3, 4, 5]

# Achtung: Python hat ein Standard-Rekursionslimit von 1000
import sys
print(sys.getrecursionlimit())   # 1000
# sys.setrecursionlimit(10000) — anpassbar, aber mit Vorsicht


# -----------------------------------------------------------------------------
# 6. SORTING ALGORITHMS
# -----------------------------------------------------------------------------

# --- Built-in (immer bevorzugen!) ---
lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(lst))              # neue Liste, Original unverändert
lst.sort()                      # in-place
lst.sort(reverse=True)          # absteigend
lst.sort(key=lambda x: -x)     # custom key

# Objekte sortieren
people = [{"name": "Ana", "age": 30}, {"name": "Bert", "age": 25}]
people.sort(key=lambda p: p["age"])

# Python verwendet Timsort: O(n log n), stabil

# --- Bubble Sort — O(n²) — nur zum Verständnis ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --- Binary Search — O(log n) ---
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_list, 7))    # 3 (Index)
print(binary_search(sorted_list, 4))    # -1

# Built-in bisect für Binary Search
import bisect
print(bisect.bisect_left(sorted_list, 7))   # 3


# =============================================================================
# ADVANCED CONCEPTS
# =============================================================================


# -----------------------------------------------------------------------------
# 7. MODULES
# -----------------------------------------------------------------------------

# --- Builtin Module (Auswahl der wichtigsten) ---
import os
import sys
import math
import random
import datetime
from pathlib import Path

# os
print(os.getcwd())                  # aktuelles Verzeichnis
print(os.listdir("."))              # Verzeichnisinhalt
os.path.join("folder", "file.txt") # plattformunabhängige Pfade

# pathlib (moderner als os.path)
p = Path(".")
print(list(p.glob("*.py")))        # alle .py Dateien

# math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(math.ceil(3.2))   # 4
print(math.floor(3.9))  # 3

# random
print(random.randint(1, 10))           # zufällige int
print(random.choice(["a", "b", "c"])) # zufälliges Element
random.shuffle(lst)                    # in-place mischen

# datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
delta = datetime.timedelta(days=7)
next_week = now + delta

# --- Custom Module ---
# Datei: my_module.py
#   def greet(name): return f"Hallo, {name}!"
#   PI = 3.14159
#
# Import:
#   import my_module
#   from my_module import greet, PI
#   from my_module import greet as g

# __name__ == "__main__" — Code nur ausführen wenn direkt gestartet
if __name__ == "__main__":
    print("Direkt ausgeführt")
# → wird NICHT ausgeführt wenn das Modul importiert wird


# -----------------------------------------------------------------------------
# 8. LAMBDAS
# -----------------------------------------------------------------------------

# Lambda = anonyme Einzeiler-Funktion
# Syntax: lambda parameter(s): ausdruck

double = lambda x: x * 2
add = lambda x, y: x + y

print(double(5))    # 10
print(add(3, 4))    # 7

# Lambdas glänzen als Argumente für höhere Funktionen
nums = [1, 2, 3, 4, 5, 6]

# map: Funktion auf jedes Element anwenden
squared = list(map(lambda x: x**2, nums))

# filter: Elemente filtern
evens = list(filter(lambda x: x % 2 == 0, nums))

# sorted mit key
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=lambda w: len(w)))   # nach Länge sortieren

# Achtung: Für komplexere Logik → normale Funktion bevorzugen
# Lambda ist für kurze, lesbare Einzeiler gedacht


# -----------------------------------------------------------------------------
# 9. DECORATORS
# -----------------------------------------------------------------------------

# Decorator = Funktion die eine andere Funktion umhüllt und erweitert

# Grundprinzip
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Vor dem Aufruf")
        result = func(*args, **kwargs)
        print("Nach dem Aufruf")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hallo, {name}!")

say_hello("Benedikt")
# Vor dem Aufruf
# Hallo, Benedikt!
# Nach dem Aufruf

# functools.wraps — Metadaten der Originalfunktion erhalten
from functools import wraps

def timer(func):
    import time
    @wraps(func)            # erhält __name__, __doc__ etc.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} dauerte {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)

slow_function()

# Decorator mit Argumenten (Factory-Pattern)
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def wave():
    print("Hi!")

wave()   # Hi! Hi! Hi!

# Gebräuchliche Built-in Decorators
class MyClass:
    class_var = "shared"

    @staticmethod
    def static_method():    # kein self, kein cls
        print("Statische Methode")

    @classmethod
    def class_method(cls):  # erhält die Klasse als erstes Argument
        print(f"Klasse: {cls.__name__}")

    @property
    def value(self):        # Zugriff wie Attribut: obj.value
        return self._value


# -----------------------------------------------------------------------------
# 10. ITERATORS
# -----------------------------------------------------------------------------

# Iterable: Objekt das __iter__ hat (list, str, dict, ...)
# Iterator: Objekt das __iter__ UND __next__ hat

# iter() und next() manuell
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it)        # StopIteration!

# Eigenen Iterator bauen
class CountUp:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self    # Iterator gibt sich selbst zurück

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for n in CountUp(1, 5):
    print(n, end=" ")   # 1 2 3 4
print()

# Generator — eleganterer Weg für Iteratoren
def count_up(start, stop):
    while start < stop:
        yield start     # pausiert hier und gibt Wert zurück
        start += 1

for n in count_up(1, 5):
    print(n, end=" ")   # 1 2 3 4
print()

# Generator Expression (wie List Comprehension, aber lazy)
gen = (x**2 for x in range(1000000))   # kein Speicherproblem!
print(next(gen))   # 0
print(next(gen))   # 1

# Nützliche Iterator-Tools
from itertools import islice, chain, product, combinations, permutations

print(list(islice(count_up(0, 100), 5)))    # nur erste 5: [0, 1, 2, 3, 4]
print(list(chain([1, 2], [3, 4], [5])))     # [1, 2, 3, 4, 5]
print(list(combinations("ABC", 2)))         # [('A','B'), ('A','C'), ('B','C')]


# -----------------------------------------------------------------------------
# 11. REGULAR EXPRESSIONS
# -----------------------------------------------------------------------------

import re

text = "Meine Email ist max.mustermann@example.com und die Handynummer 0664 1234567"

# Grundlegende Methoden
print(re.search(r"\d+", text))          # erstes Match-Objekt
print(re.findall(r"\d+", text))         # alle Matches als Liste
print(re.match(r"Meine", text))         # nur am Anfang des Strings
print(re.sub(r"\d", "X", text))         # ersetzen

# Match-Objekt
m = re.search(r"(\w+)@(\w+)\.(\w+)", text)
if m:
    print(m.group(0))   # ganzer Match
    print(m.group(1))   # erste Gruppe (username)
    print(m.start(), m.end())   # Positionen

# Wichtige Regex-Symbole
# .       beliebiges Zeichen (außer \n)
# *       0 oder mehr
# +       1 oder mehr
# ?       0 oder 1 (optional)
# ^       Anfang des Strings
# $       Ende des Strings
# \d      Ziffer [0-9]
# \D      keine Ziffer
# \w      Wortzeichen [a-zA-Z0-9_]
# \W      kein Wortzeichen
# \s      Whitespace
# \S      kein Whitespace
# [abc]   Zeichenklasse
# [^abc]  negierte Zeichenklasse
# (...)   Gruppe
# |       Oder

# Kompiliertes Pattern (effizienter bei mehrfacher Nutzung)
email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
emails = email_pattern.findall(text)
print(emails)

# Flags
re.search(r"meine", text, re.IGNORECASE)   # Groß-/Kleinschreibung ignorieren


# -----------------------------------------------------------------------------
# 12. VARIABLE SCOPE
# -----------------------------------------------------------------------------

# LEGB-Regel: Local → Enclosing → Global → Built-in

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # "local"

    inner()
    print(x)        # "enclosing"

outer()
print(x)            # "global"

# global-Keyword: globale Variable in Funktion ändern
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)   # 2

# nonlocal-Keyword: Variable in Enclosing-Scope ändern
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3

# Scope-Check mit locals() und globals()
def scope_demo():
    a = 1
    b = 2
    print(locals())    # {'a': 1, 'b': 2}

# Wichtige Faustregel:
# → Vermeide global wo möglich (schwer nachvollziehbar, fehleranfällig)
# → Übergib Werte lieber als Parameter und gib sie zurück