-- Esto es un comentario

-- SQL (Structured Query Language) Lenguaje Estructurado de Consultas
-- En SQL siempre hay que colocar el ';' al final de cada query
-- Dos Sub lenguajes de manejo de informacion 
-- DDL (Data Definition Language) > Lenguaje de Definicion de Datos

-- CREATE
CREATE DATABASE pruebas;

-- Sirve para listar las bases de datos que hay en este servidor
SHOW DATABASES;

-- Seleccionar la base de datos que vamos a trabajar
USE pruebas;

-- Siempre las palabras reservadas se recomiendan que se coloquen en mayus
-- Nota: las tablas siempre deben de tener nombre pluralizados
-- https://dev.mysql.com/doc/refman/8.0/en/create-table.html
CREATE TABLE alumnos(
	-- Ahora definimos las columnas
    -- nombre_col tipo_dato [parametros opcionales]
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    -- es un tipo de dato que permite guardar determinados valores
    sexo ENUM('FEMENINO', 'MASCULINO', 'BINARIX', 'OTRO', 'HELICOPTERO'),
    -- agregar la columna tipo_documento que solamente puede ser DNI, C.E., PASAPORTE
    tipo_documento ENUM('DNI', 'C.E.', 'PASAPORTE') DEFAULT 'DNI',
    -- y la columna num_documento que solamente puede tener hasta 10 caracteres
    num_documento VARCHAR(10) NOT NULL,
    fec_nacimiento DATETIME
);

-- Para ver las tablas en la terminal
SHOW TABLES;


-- DML (Data Manipulation Language
-- Lenguaje de Manipulacion de Datos

-- SELECT [columnas] FROM tabla;
SELECT nombre, sexo FROM alumnos;
SELECT * FROM alumnos;

-- INSERT INTO tabla (columnas) VALUES (valores);
INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('Eduardo', 'MASCULINO', '73500746', '1992-08-01');

INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('Ronald', 'BINARIX', '75268256', '1995-07-25'),
                    ('Karim', 'FEMENINO', '85234716', '1991-01-15'),
                    ('Alexa', 'HELICOPTERO', '14729583', '1995-06-08');

SELECT * FROM ALUMNOS;

INSERT INTO alumnos VALUES 
					(DEFAULT, 'Romina', 'FEMENINO', 'C.E.', '456789132', '1987-05-14'),
                    (DEFAULT, 'Roberto', 'BINARIX', 'PASAPORTE', '15946789', '1985-01-01'),
                    (DEFAULT, 'Jair', 'MASCULINO', DEFAULT, '34598746', '1995-04-09');
					
SELECT * FROM ALUMNOS;

-- NOTA : SIEMPRE EN LOS UPDATES Y DELETES TENEMOS QUE EJECUTARLOS CON UNA CONDICIONAL
-- DELETE FROM tabla WHERE condicional
DELETE FROM alumnos WHERE id>=10 AND id <=12;

SELECT * FROM ALUMNOS;

-- UPDATE tabla SET columna='Nuevo valor' WHERE condicional
UPDATE alumnos SET nombre='Marimar' WHERE id = 8;
UPDATE alumnos SET num_documento = '99564879', nombre = 'Rodrigo' WHERE id = 9;

SELECT * FROM alumnos;


INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('Maria Alejandra', 'BINARIX', '49596785', '1995-06-19');


SELECT * FROM alumnos;

-- 1. Mostrar todos los alumnos que tengan C.E.
SELECT * FROM alumnos WHERE tipo_documento = 'C.E.';
-- 2. Mostrar todos los alumnos que tengan SEXO MASCULINO O FEMENINO
SELECT * FROM alumnos WHERE sexo = 'MASCULINO' OR sexo='FEMENINO';
SELECT * FROM alumnos WHERE sexo IN ('MASCULINO', 'FEMENINO');

-- 3. Mostrar a todos los alumnos que nacieron antes del 1990-01-01
SELECT * FROM alumnos WHERE fec_nacimiento < '1990-01-01';

-- Dame todos los alumnos cuyo nombre contenga la letra a
SELECT nombre FROM alumnos WHERE nombre LIKE '%a%';
-- Dame todos los alumnos cuya ultima letra sea la a
-- con la propiedad BINARY le indicamos que haga la comparacion a nivel de binarios esto incluye la comparacion entre mayus, minus
-- y entre tildes y caracteres especiales como la 'ñ'
SELECT nombre FROM alumnos WHERE nombre LIKE BINARY '%A';

SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';

-- Dame todos los alumnos cuya segunda letra sea la o
SELECT nombre FROM alumnos WHERE nombre LIKE '_o%';

-- SELECT nombre FROM alumnos WHERE nombre LIKE 'E__%';

SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';
SELECT nombre FROM alumnos WHERE nombre LIKE '%d_u%';


-- 4. Mostrar todos los alumnos cuyo nombre tenga al menos la letra 'n'
SELECT * FROM alumnos WHERE nombre LIKE '%n%';

-- 5. Mostrar todos los alumnos cuyo segundo digito del documento sea '8'
SELECT * FROM alumnos WHERE num_documento LIKE '_8%';

-- 6. Mostrar todos los alumnos cuyo sexo contenga la letra 'i' seguido de una letra cualquiera y luego la letra 'o'
SELECT * FROM alumnos WHERE sexo LIKE '%i_o%';
