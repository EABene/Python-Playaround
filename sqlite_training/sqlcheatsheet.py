import sqlite3

# =============================================================================
# SQLITE LERNEN — Schritt für Schritt
# Beispiel: Bücherliste
#
# Führe dieses File aus und lies jeden Schritt durch.
# Danach kommentiere einzelne Schritte aus und experimentiere selbst.
# =============================================================================


# -----------------------------------------------------------------------------
# SCHRITT 1 — Verbindung & Tabelle erstellen
# -----------------------------------------------------------------------------

conn = sqlite3.connect("books.db")      # Datei wird erstellt falls nicht vorhanden
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        title       TEXT NOT NULL,
        author      TEXT NOT NULL,
        year        INTEGER,
        pages       INTEGER,
        finished    INTEGER DEFAULT 0   -- 0 = nicht gelesen, 1 = gelesen (SQLite hat kein BOOLEAN)
    )
""")

conn.commit()
print("✓ Schritt 1: Tabelle erstellt\n")


# -----------------------------------------------------------------------------
# SCHRITT 2 — INSERT: Einträge hinzufügen
# -----------------------------------------------------------------------------

# Einzelner Eintrag
cursor.execute("""
    INSERT INTO books (title, author, year, pages, finished)
    VALUES (?, ?, ?, ?, ?)
""", ("Python Crash Course", "Eric Matthes", 2019, 544, 0))

# Mehrere Einträge auf einmal
buecher = [
    ("Automate the Boring Stuff", "Al Sweigart", 2020, 592, 1),
    ("Clean Code", "Robert Martin", 2008, 431, 0),
    ("The Pragmatic Programmer", "David Thomas", 2019, 352, 0),
    ("Deep Work", "Cal Newport", 2016, 296, 1),
]

cursor.executemany("""
    INSERT INTO books (title, author, year, pages, finished)
    VALUES (?, ?, ?, ?, ?)
""", buecher)

conn.commit()
print("✓ Schritt 2: Einträge hinzugefügt\n")


# -----------------------------------------------------------------------------
# SCHRITT 3 — SELECT: Daten lesen
# -----------------------------------------------------------------------------

# Alle Einträge
cursor.execute("SELECT * FROM books")
alle = cursor.fetchall()        # gibt eine Liste von Tuples zurück

print("── Alle Bücher ──────────────────────────")
for row in alle:
    print(row)

# Nur bestimmte Spalten
cursor.execute("SELECT title, author FROM books")
auswahl = cursor.fetchall()

print("\n── Nur Titel und Autor ──────────────────")
for row in auswahl:
    print(f"{row[0]} von {row[1]}")

# Einzelnen Eintrag holen
cursor.execute("SELECT * FROM books WHERE id = ?", (1,))
ein_buch = cursor.fetchone()    # gibt ein einzelnes Tuple zurück, nicht eine Liste
print(f"\n── Buch mit ID 1 ────────────────────────\n{ein_buch}")

print()


# -----------------------------------------------------------------------------
# SCHRITT 4 — WHERE: Filtern
# -----------------------------------------------------------------------------

# Bücher nach Jahr filtern
cursor.execute("SELECT title, year FROM books WHERE year >= ?", (2019,))
neue = cursor.fetchall()

print("── Bücher ab 2019 ───────────────────────")
for row in neue:
    print(f"{row[0]} ({row[1]})")

# Bereits gelesen
cursor.execute("SELECT title FROM books WHERE finished = 1")
gelesen = cursor.fetchall()

print("\n── Bereits gelesen ──────────────────────")
for row in gelesen:
    print(f"✓ {row[0]}")

print()


# -----------------------------------------------------------------------------
# SCHRITT 5 — ORDER BY und LIMIT
# -----------------------------------------------------------------------------

# Nach Seitenzahl sortieren (aufsteigend)
cursor.execute("SELECT title, pages FROM books ORDER BY pages ASC")
nach_seiten = cursor.fetchall()

print("── Nach Seitenzahl (aufsteigend) ────────")
for row in nach_seiten:
    print(f"{row[0]}: {row[1]} Seiten")

# Nur das kürzeste Buch
cursor.execute("SELECT title, pages FROM books ORDER BY pages ASC LIMIT 1")
kuerzstes = cursor.fetchone()
print(f"\n── Kürzestes Buch ───────────────────────\n{kuerzstes[0]}: {kuerzstes[1]} Seiten\n")


# -----------------------------------------------------------------------------
# SCHRITT 6 — UPDATE: Eintrag ändern
# -----------------------------------------------------------------------------

# Buch als gelesen markieren
cursor.execute("""
    UPDATE books SET finished = 1 WHERE title = ?
""", ("Python Crash Course",))

conn.commit()

# Prüfen ob es geklappt hat
cursor.execute("SELECT title, finished FROM books WHERE title = ?", ("Python Crash Course",))
print("── Nach Update ──────────────────────────")
print(cursor.fetchone())
print()


# -----------------------------------------------------------------------------
# SCHRITT 7 — DELETE: Eintrag löschen
# -----------------------------------------------------------------------------

cursor.execute("DELETE FROM books WHERE id = ?", (3,))
conn.commit()

cursor.execute("SELECT COUNT(*) FROM books")    # COUNT(*) zählt alle Zeilen
anzahl = cursor.fetchone()[0]
print(f"── Nach Delete ──────────────────────────\nNoch {anzahl} Bücher in der Datenbank\n")


# -----------------------------------------------------------------------------
# SCHRITT 8 — Aggregatfunktionen
# -----------------------------------------------------------------------------

cursor.execute("SELECT COUNT(*) FROM books")
print(f"Anzahl Bücher:        {cursor.fetchone()[0]}")

cursor.execute("SELECT SUM(pages) FROM books")
print(f"Seiten gesamt:        {cursor.fetchone()[0]}")

cursor.execute("SELECT AVG(pages) FROM books")
print(f"Durchschnitt Seiten:  {round(cursor.fetchone()[0], 1)}")

cursor.execute("SELECT MAX(pages) FROM books")
print(f"Längstes Buch:        {cursor.fetchone()[0]} Seiten")

cursor.execute("SELECT MIN(year) FROM books")
print(f"Ältestes Buch:        {cursor.fetchone()[0]}")


# -----------------------------------------------------------------------------
# ABSCHLUSS
# -----------------------------------------------------------------------------

conn.close()
print("\n✓ Verbindung geschlossen.")
print("\n── SQL Befehle die du heute gelernt hast ─")
print("  CREATE TABLE    → Tabelle erstellen")
print("  INSERT INTO     → Eintrag hinzufügen")
print("  SELECT          → Daten lesen")
print("  WHERE           → Filtern")
print("  ORDER BY        → Sortieren")
print("  LIMIT           → Anzahl begrenzen")
print("  UPDATE          → Eintrag ändern")
print("  DELETE          → Eintrag löschen")
print("  COUNT / SUM / AVG / MAX / MIN → Aggregatfunktionen")




# =============================================================================
# PYTHON sqlite3 — API Cheat Sheet
# Nicht SQL-Syntax, sondern: wie Python mit SQLite spricht
# =============================================================================

import sqlite3

# -----------------------------------------------------------------------------
# 1. VERBINDUNG
# -----------------------------------------------------------------------------

conn = sqlite3.connect("database.db")   # Datei erstellen / öffnen
conn = sqlite3.connect(":memory:")      # nur im RAM — perfekt zum Testen, verschwindet danach

conn.close()                            # Verbindung schließen — immer am Ende!


# -----------------------------------------------------------------------------
# 2. CURSOR
# -----------------------------------------------------------------------------

# Der Cursor ist der Vermittler zwischen Python und der Datenbank.
# Ohne Cursor kannst du keine Befehle abschicken.

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()                  # Cursor erstellen


# -----------------------------------------------------------------------------
# 3. EXECUTE — SQL Befehl abschicken
# -----------------------------------------------------------------------------

# Einfacher Befehl
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Mit Parametern — IMMER ? verwenden, niemals f-Strings!
name = "John"
cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))      # Tuple mit einem Wert → Komma beachten!
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

# Mehrere Einträge auf einmal
daten = [("Anna",), ("Klaus",), ("Maria",)]
cursor.executemany("INSERT INTO users (name) VALUES (?)", daten)


# -----------------------------------------------------------------------------
# 4. FETCH — Ergebnisse abholen
# -----------------------------------------------------------------------------

cursor.execute("SELECT * FROM users")

cursor.fetchone()       # ein einzelnes Ergebnis als Tuple  → (1, "John")
                        # gibt None zurück wenn nichts gefunden

cursor.fetchall()       # alle Ergebnisse als Liste von Tuples → [(1, "John"), (2, "Anna")]
                        # gibt [] zurück wenn nichts gefunden

cursor.fetchmany(3)     # die nächsten 3 Ergebnisse


# Ergebnis direkt auslesen — row ist ein Tuple
cursor.execute("SELECT * FROM users")
for row in cursor:          # cursor ist direkt iterierbar
    print(row[0])           # ID
    print(row[1])           # Name


# -----------------------------------------------------------------------------
# 5. COMMIT & ROLLBACK
# -----------------------------------------------------------------------------

# Änderungen (INSERT, UPDATE, DELETE) werden erst mit commit() gespeichert!
# Ohne commit() → Änderungen gehen verloren wenn conn.close() aufgerufen wird

conn.commit()           # Änderungen speichern ✓

conn.rollback()         # Änderungen rückgängig machen — nützlich bei Fehlern


# -----------------------------------------------------------------------------
# 6. CURSOR ATTRIBUTE
# -----------------------------------------------------------------------------

cursor.execute("SELECT * FROM users")

cursor.rowcount         # Anzahl betroffener Zeilen (nach INSERT/UPDATE/DELETE)
cursor.lastrowid        # ID des zuletzt eingefügten Eintrags — nützlich nach INSERT
cursor.description      # Spaltennamen der letzten Query


# Spaltennamen ausgeben — so weißt du was in row[0], row[1] etc. steckt
cursor.execute("SELECT * FROM users")
spalten = [desc[0] for desc in cursor.description]
print(spalten)          # ['id', 'name']


# -----------------------------------------------------------------------------
# 7. ROW FACTORY — Ergebnisse als Dictionary statt Tuple
# -----------------------------------------------------------------------------

# Standard: row ist ein Tuple → row[0], row[1]
# Mit Row Factory: row ist ein dict-ähnliches Objekt → row["id"], row["name"]

conn.row_factory = sqlite3.Row      # einmal setzen, gilt für alle Queries danach

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"])                  # "John" — viel lesbarer als row[1]


# -----------------------------------------------------------------------------
# 8. CONTEXT MANAGER — with statt manuell close()
# -----------------------------------------------------------------------------

# Ohne with — manuell:
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
conn.close()

# Mit with — automatisches commit() und close():
with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    # conn.close() wird automatisch aufgerufen
    # bei Fehler → automatisch rollback()


# -----------------------------------------------------------------------------
# 9. FEHLERBEHANDLUNG
# -----------------------------------------------------------------------------

try:
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Datenbankfehler: {e}")      # z.B. UNIQUE constraint verletzt
except sqlite3.OperationalError as e:
    print(f"Operationsfehler: {e}")     # z.B. Tabelle existiert nicht
finally:
    conn.close()                        # wird IMMER ausgeführt, auch bei Fehler


# -----------------------------------------------------------------------------
# ZUSAMMENFASSUNG — die wichtigsten Zeilen im Alltag
# -----------------------------------------------------------------------------

# conn   = sqlite3.connect("file.db")      → Verbindung aufbauen
# cursor = conn.cursor()                   → Cursor erstellen
# cursor.execute("SQL", (params,))         → Befehl abschicken
# cursor.fetchall()                        → alle Ergebnisse holen
# cursor.fetchone()                        → ein Ergebnis holen
# cursor.lastrowid                         → ID des letzten INSERT
# conn.commit()                            → Änderungen speichern
# conn.close()                             → Verbindung schließen
