-- Löscht die Tabellen
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS User;

-- Erstellt Tabelle Department
CREATE TABLE Department
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(32) NOT null
);

-- Erstellt Tabelle User
CREATE TABLE User 
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(32) NOT null,
	email VARCHAR(64),
	age tinyint,
	dept_id int,
	FOREIGN KEY(dept_id) references Department(id) -- verbindet die Tabelle User mit der Tabelle Department
);

-- Fügt Daten in die Tabelle
INSERT INTO Department (name) values ("Lagerwirtschaft");
INSERT INTO Department (name) values ("Buchhaltung");
INSERT INTO Department (name) values ("Fuhrpark");

INSERT INTO User (name, email, age, dept_id) values ("Tom","tom@ga.de", 25,1);
INSERT INTO User (name, email, age, dept_id) values ("Tina","tina.meier@ga.de", 22,2);
INSERT INTO User (name, email, age, dept_id) values ("Hans-Peter","hans-peter.muellerhausern@ga.de", 44,3);

-- Zeigt alle Daten aus der Tabelle X an
SELECT * FROM User;
SELECT * FROM Department;

-- Zeigt nur spezifische Daten aus der Tabelle an, Columns.
SELECT name, email, age FROM User;

-- Sucht nach dem User Tina
SELECT age FROM User WHERE name = "Tina";

-- Sucht nach dem Namen Hans, aber dieser kann mehr Buchstaben nach Hans haben.
SELECT age FROM User WHERE name LIKE "Hans%";

-- Sucht nach Namen und Emails von Usern, die vom Alter zwischen 20 und 30 sind.
SELECT name, email FROM User WHERE age BETWEEN 20 AND 30;

-- Join, verbindet die Tabelle User mit Department, verbindet die Daten, Thema Inner Join
-- Abkürzung der Tabelle durch u und d
SELECT u.name "User Name", u.email, u.age, d.name "Dept Name" FROM User u
JOIN Department d ON d.id = u.dept_id;

-- Views, vereinfachen eine Select Query
CREATE VIEW view_user_department as
SELECT u.name "User Name", u.email, u.age, d.name "Dept Name" FROM User u
JOIN Department d ON d.id = u.dept_id;

-- Dadurch dass eine View erstellt wurde, kann man diese ganz einfach durch ein Select aufrufen
SELECT * FROM view_user_department

-- Update
-- Ändert den Namen von Hans-Peter in Hans-Wurst
UPDATE User SET name = "Hans-Wurst" WHERE id = 3;

-- Delete
-- Löscht den User mit der ID 2
DELETE FROM User WHERE id = 2;

-- Alter
-- Fügt der vorhandenen Tabelle User die Spalte Tel hinzu
ALTER TABLE User
ADD Tel VARCHAR(32);

-- Löscht die Spalte Tel aus der Tabelle User
ALTER TABLE User
DROP COLUMN Tel;

-- Löscht die Spalte age und fügt eine neue hinzu
ALTER TABLE User
DROP COLUMN age
ADD birthdate DATE;

-- Oder verändert die Spalte age zum Datentyp Date und ändert den Namen
ALTER TABLE User
MODIFY COLUMN age DATE
RENAME COLUMN age TO birthdate