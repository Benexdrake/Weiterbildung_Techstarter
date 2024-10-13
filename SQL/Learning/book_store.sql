-- create table if not exists
-- Erstelle eine .db Datei, du kannst diese mit der SQLite Extension durch rechtsklick auf der Datei und Open Database.
-- Wenn du eines der Statements hier ausführst, wirst du normalerweise nach der DB gefragt, falls in der Liste vorhanden, diese auswählen, ansonsten die Datei suchen.

-- author
CREATE TABLE IF NOT EXISTS author
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name varchar(32) not null,
    last_name varchar(32) not null,
    birth_date date
);

-- book
CREATE TABLE IF NOT EXISTS book
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(64) not null,
    genre_id INTEGER not null,
    release date,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES author(id),
    FOREIGN KEY(genre_id) REFERENCES genre(id)
);

-- customer
CREATE TABLE IF NOT EXISTS customer
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name varchar(32) not null,
    last_name varchar(32) not null,
    street varchar(32) not null,
    nr varchar(12) not null,
    postcode varchar(12) not null,
    location varchar(32) not null,
    email varchar(64) not null
);

-- sell
CREATE TABLE IF NOT EXISTS sell
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER not null,
    customer_id INTEGER not null,
    sell_date date not null,
    number int not null
);

-- genre
CREATE TABLE IF NOT EXISTS genre
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre varchar(32) not null
);

-- insert into
-- author
INSERT INTO author (first_name, last_name, birth_date)
VALUES
("Antoine","de Saint.Exepéry","1900-29-06"),
("George","Orwell","1903-25-06"),
("Umberto","Eco","1932-05-01"),
("J.K.","Rowling","1965-31-7");

-- genre
INSERT INTO genre (genre)
VALUES
("Kinderbuch"),
("Science Fiction"),
("Krimi"),
("Fantasy");

-- book
INSERT INTO book (title, genre_id, release, author_id)
VALUES
("Der kleine Prinz",1,"1943",1),
("1984",2,"1949",2),
("Der Name der Rose",3,"1980",3),
("Harry Potter und der Stein der Weisen",4,"1997",4);

-- customer
INSERT INTO customer (first_name,last_name,street,nr,postcode,location,email)
VALUES
("Max","Müller","Hauptstraße","42","12345","München","m.m@live.de"),
("Lisa","Meier","Bergstraße","17","56789","Berlin","lisa_meier@outlook.de"),
("Peter","Schmidt","Am See","8","98765","Hamburg","p.s@gmail.com"),
("Anna","Schneider","Gartenweg","23","43210","Dortmund","a.schneider@aol.de");

-- sell
INSERT INTO sell (book_id, customer_id, sell_date, number)
VALUES
(1,1,"2023-01-01", 2),
(2,2,"2023-02-15", 1),
(3,3,"2023-03-10", 3),
(4,4,"2023-04-05", 2);

-- select * from
SELECT * FROM author;
SELECT * FROM book;
SELECT * FROM customer;
SELECT * FROM genre;
SELECT * FROM sell;

-- select with join
SELECT
b.title, b.release, a.first_name || ' ' || a.last_name 'author', g.genre
FROM book b
JOIN author a ON b.author_id = a.id
join genre g ON b.genre_id = g.id;

SELECT
*
FROM sell s
join book b on s.book_id = b.id
join customer c on s.customer_id = c.id;


-- create view
create view view_book_author_genre AS
SELECT
b.title, b.release, a.first_name || ' ' || a.last_name 'author', g.genre
FROM book b
JOIN author a ON b.author_id = a.id
join genre g ON b.genre_id = g.id;

create view view_sell_book_customer AS
SELECT
s.id, s.sell_date, number, b.title, g.genre, a.first_name || ' ' || a.last_name 'author', c.first_name || ' ' ||c.last_name 'customer', c.street || '.' || c.nr 'street', c.postcode,c.location
FROM sell s
join book b on s.book_id = b.id
join customer c on s.customer_id = c.id
join author a on b.author_id = a.id
join genre g on b.genre_id = g.id;

-- select * from view

SELECT * FROM view_book_author_genre;

SELECT * FROM view_sell_book_customer;

-- update
UPDATE customer set first_name = 'Kobold' WHERE id = 1;

-- modify

-- drop

drop table book;
drop table author;
drop table sell;
drop table customer;
drop table genre;

-- CRUD

-- C: Create - Insert
-- R: Read - Select
-- U: Update
-- D: Delete