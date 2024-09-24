CREATE TABLE mylist_members (
    id INTEGER PRIMARY KEY,  -- Automatisch inkrementierender Primärschlüssel
    name TEXT NOT NULL,
    color TEXT,
    sum REAL
);

-- Ganze Tabelle löschen 
DROP TABLE mylist_members;      

-- Inhalte der Tabelle löschen
DELETE FROM mylist_members;

-- Einträge löschen
DELETE FROM mylist_members
WHERE id = 1;

-- Einträge hinzufügen
INSERT INTO mylist_members (name, color, sum)
VALUES
    ('-', 'FF00FF', 0.0),
    ('Huber/Hoffmann', 'FF00FF', 0.0),
    ('Teßmann', 'FF00FF', 0.0),
    ('Wenninger/Fiedler', 'FF00FF', 0.0),
    ('Hildegund & Osi', 'FF00FF', 0.0),
    ('Sarita Schwerla', 'FF00FF', 0.0),
    ('Laux', 'FF00FF', 0.0),
    ('Klaus Plessner', 'FF00FF', 0.0),
    ('Susanne Zehetmeier', 'FF00FF', 0.0),
    ('-', 'FF00FF', 0.0),
    ('Nora Siebels', 'FF00FF', 0.0),
    ('Schürkämper', 'FF00FF', 0.0),
    ('Gabi Mitschka', 'FF00FF', 0.0),
    ('Fritz Spörl', 'FF00FF', 0.0),
    ('-', 'FF00FF', 0.0),
    ('-', 'FF00FF', 0.0),
    ('-', 'FF00FF', 0.0);
