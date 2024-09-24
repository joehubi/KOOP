CREATE TABLE mylist_save (
    id INTEGER PRIMARY KEY,  -- Automatisch inkrementierender Primärschlüssel
    nr_save INTEGER DEFAULT 0,
    sum_save REAL DEFAULT 0.0
);

-- Ganze Tabelle löschen 
DROP TABLE mylist_save;   
    
-- Inhalte der Tabelle löschen
DELETE FROM mylist_save;

