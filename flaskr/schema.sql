-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS masini;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS model;
DROP TABLE IF EXISTS producator;
DROP TABLE IF EXISTS variante_vanzare_model;
DROP TABLE IF EXISTS probleme_masini;
DROP TABLE IF EXISTS martori;
DROP TABLE IF EXISTS componenta_problema;


------------------------------------TABLE utilizatori-------------------------------
CREATE TABLE "user" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  nume TEXT NOT NULL,
  prenume TEXT NOT NULL,
  email TEXT NOT NULL,
  nr_telefon TEXT NOT NULL,
  cod_masina TEXT NOT NULL,
  FOREIGN KEY (cod_masina) REFERENCES masini (cod_masina)
);

INSERT INTO "user"
    (id, username, password, nume, prenume, email, nr_telefon, cod_masina)
VALUES
    (1, 'admin', 'admin', 'admin', 'admin', 'admin@admin.com', '0743', '1'),
    (2, 'test', 'test', 'test', 'test', 'test@test.com', '0743', '2');
    

------------------------------------TABLE posts-------------------------------

CREATE TABLE "post" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


------------------------------------TABLE masini-------------------------------

CREATE TABLE "masini" (
  cod_masina INTEGER PRIMARY KEY AUTOINCREMENT,
  cod_varianta INTEGER NOT NULL,
  an_masina TEXT NOT NULL
);

INSERT INTO masini
    (cod_masina, cod_varianta, an_masina)
VALUES
    (1, 1, '2004'),
    (2, 2, '2004'),
    (3, 3, '2003'),
    (4, 4, '2003'),
    (5, 5, '2001'),
    (6, 6, '2009');


------------------------------------TABLE marca-------------------------------
CREATE TABLE "marca" (
  cod_marca INTEGER PRIMARY KEY AUTOINCREMENT,
  cod_masina INTEGER NOT NULL,
  nume_marca TEXT NOT NULL,
  cod_producator INTEGER NOT NULL,
  FOREIGN KEY (cod_masina) REFERENCES masini (cod_masina),
  FOREIGN KEY (cod_producator) REFERENCES producator (cod_producator)
);

INSERT INTO marca
    (cod_marca, cod_masina, nume_marca, cod_producator)
VALUES
(1, 1, 'BMW',1),
(2, 2, 'AUDI',2),
(3, 3, 'VOLKSWAGEN',3),
(4, 4, 'VOLKSWAGEN',4),
(5, 5, 'BMW',5),
(6, 6, 'DACIA',6),
(7, 7, 'FORD',7);


------------------------------------TABLE model-------------------------------
CREATE TABLE "model" (
  cod_model INTEGER PRIMARY KEY AUTOINCREMENT,
  cod_marca INTEGER NOT NULL,
  denumire_model TEXT NOT NULL,
  cutie_viteze TEXT NOT NULL,
  an_aparitie TEXT NOT NULL,
  an_disparitie TEXT NOT NULL,
  tip_caroserie TEXT NOT NULL,
  combustibil TEXT NOT NULL,
  FOREIGN KEY (cod_marca) REFERENCES marca (cod_marca)
);

INSERT INTO "model"
    (cod_model, cod_marca, denumire_model, cutie_viteze, an_aparitie, an_disparitie, tip_caroserie, combustibil)
VALUES
    (1, 1, 'Seria 1', 'Automata', '2004', '2011', 'Hatchback', 'DIESEL'),
    (2, 1, 'A4', 'Manuală', '2003', '2012', 'Berlină', 'BENZINA'),
    (3, 1, 'Golf 5', 'Manuală', '2004', '2009', 'Hatchback', 'DIESEL'),
    (4, 4, 'Golf 6', 'Manuală', '2008', '2013', 'Hatchback', 'BENZINĂ'),
    (5, 5, 'Seria 5', 'Automată', '2003', '2010', 'Berlină', 'BENZINĂ'),
    (6, 6, 'Logan', 'Manuală', '2004', '2012', 'Berlină', 'BENZINĂ'),
    (7, 7, 'Focus', 'Manuală', '2011', '2018', 'Berlină', 'DIESEL');
------------------------------------TABLE producator-------------------------------
CREATE TABLE "producator" (
  cod_producator INTEGER PRIMARY KEY AUTOINCREMENT,
  nume_producator TEXT NOT NULL,
  an_infiintare_producator TEXT NOT NULL,
  tara_producator TEXT NOT NULL
);

INSERT INTO producator
    (cod_producator, nume_producator, an_infiintare_producator, tara_producator)
VALUES
    (1, 'BMW', '1916', 'Germania'),
    (2, 'AUDI', '1909', 'Germania'),
    (3, 'VOLKSWAGEN', '1937', 'Germania'),
    (4,'VOLKSWAGEN','1937', 'Germania'),
    (5,'BMW', '1916', 'Germania'),
    (6,'DACIA', '1966', 'România'),
    (7,'FORD', '1903', 'SUA');
------------------------------------TABLE variante vanzare modele-------------------------------
CREATE TABLE "variante_vanzare_model" (
  cod_varianta INTEGER PRIMARY KEY AUTOINCREMENT,
  cod_model INTEGER NOT NULL,
  an_inceput_fabricatie TEXT NOT NULL,
  an_final_fabricatie TEXT NOT NULL,
  FOREIGN KEY (cod_model) REFERENCES model (cod_model)
);


INSERT INTO variante_vanzare_model
    (cod_varianta, cod_model, an_inceput_fabricatie, an_final_fabricatie)
VALUES
    (1, 1, '2004', '2011'),
    (2, 2, '2004', '2013'),
    (3, 3, '2003', '2010'),
    (4, 3,'2003', '2010'),
    (5, 3,'2003', '2010'),
    (6, 3,'2004', '2012'),
    (7, 3,'2011', '2018');

------------------------------------TABLE probleme masini-------------------------------
CREATE TABLE "probleme_masini" (
  id_problema_masina INTEGER PRIMARY KEY AUTOINCREMENT,
  marca_masina INTEGER NOT NULL,
  model_masina INTEGER NOT NULL,
  componenta_problema INTEGER NOT NULL,
  data_semnalizare_problema TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (marca_masina) REFERENCES marca (cod_marca),
  FOREIGN KEY (model_masina) REFERENCES model (cod_model),
  FOREIGN KEY (componenta_problema) REFERENCES componenta_problema (id_componenta_problema)
);

INSERT INTO probleme_masini
    (id_problema_masina, data_semnalizare_problema, marca_masina, model_masina,componenta_problema)
VALUES
    (1,'11/5/2021', 1 ,1 , 2), 
    (2,'10/31/2020', 2 ,2 , 1),
     (3,'1/20/2022',3 ,3 , 3),
     (4,'4/4/2022',4 ,4 , 4),
      (5,'6/9/2021',5 ,5 , 5),
       (6,'8/9/2021',6 ,6 , 6),
    (7,'9/9/2021',7 ,7 , 7);
------------------------------------TABLE componenete problema -------------------------------
CREATE TABLE "componenta_problema" (
  id_componenta_problema INTEGER PRIMARY KEY AUTOINCREMENT,
  denumire_componenta TEXT NOT NULL,
  tip_problema TEXT NOT NULL,
  categorie_problema TEXT NOT NULL
);


INSERT INTO componenta_problema
      (id_componenta_problema, denumire_componenta, tip_problema, categorie_problema)
VALUES
(1, 'Far', 'Electric', 'Electrice'),
(2, 'Cap de bara', 'Mecanic', 'Suspensie, tije'),
(3, 'Curea distributie', 'Mecanic', 'Curele, lanturi si role'),
(4, 'Filtru ulei', 'Mecanic', 'Filtru ulei'),
(5, 'Bobine inducție', 'Mecanic', 'Motor'),
(6, 'Pompă servodirecție', 'Mecanic', 'Direcție'),
(7, 'Turbina', 'Mecanic', 'Motor');
------------------------------------TABLE martori-------------------------------
CREATE TABLE "martori" (
  id_martor INTEGER PRIMARY KEY AUTOINCREMENT,
  id_problema_masina INTEGER NOT NULL,
  cod_masina INTEGER NOT NULL,
  denumire_martor TEXT NOT NULL,
  posibile_cauze TEXT NOT NULL,
  FOREIGN KEY (id_problema_masina) REFERENCES probleme_masini (id_problema_masina),
  FOREIGN KEY (cod_masina) REFERENCES masini (cod_masina)
);
INSERT INTO martori
    (id_martor,id_problema_masina,cod_masina, denumire_martor, posibile_cauze)
VALUES
  (1, 1, 1, 'Probleme filtru de particule', 'Filtru de particule înfundat cu impurități'),
  (2, 2, 2, 'Bec ars', 'Uzura filamentului sau supratensiune'),
  (3, 3, 3, 'Combustibil scăzut', 'Terminarea combustibilului sau un furtun de combustibil spart'),
  (4, 4, 4,'Pompa injecție', 'Consum excesiv de ulei' ),
   (5, 5, 5,'Check-engine', 'Diverse probleme' ),
  (6, 6, 6,'Servodirectie', 'Diverse probleme' ),
  (7, 7, 7,'Check-engine', 'Diverse probleme' );