-- Crear una base de datos llamada colegio
CREATE DATABASE colegio;

-- Utilizar esa base de datos creada
USE colegio;

-- En la bd colegio necesitamos almacenar los alumnos pero con la siguiente informacion:
-- id PK entero autoincrementable, nombre string hasta 100 caracteres, ape_paterno string
-- hasta 50 caracteres, ape_materno string hasta 50 caracteres, correo no se puede repetir va a ser
-- texto, num_emergencia string hasta 10 caracteres.
-- Cuando queremos utilizar una columna TEXT o BLOB esta no puede ser tratada como un indice (UNIQUE)
-- porque mysql al no conocer la longitud maxima de esos valores no podra garantizar la unicidad
-- no se repitan esos valores por lo que no se puede utilizar los tipos de datos TEXT o BLOB para 
-- columnas UNIQUES
-- https://stackoverflow.com/questions/1827063/mysql-error-key-specification-without-a-key-length

DROP TABLE cursos;
DROP TABLE alumnos;


CREATE TABLE cursos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    color TEXT,
    dificultad ENUM('FACIL','MEDIO','DIFICIL')
);

CREATE TABLE alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ape_paterno VARCHAR(50) NOT NULL,
    ape_materno VARCHAR(50) NOT NULL,
    correo VARCHAR(250) UNIQUE NOT NULL,
    num_emergencia VARCHAR(10),
    -- Creo una columna referenciando segun el nombre de la tabla_nombre columna
    curso_id INT,
    -- Ahora relacionamos esa columna con la tabla alumnos
    FOREIGN KEY(curso_id) REFERENCES cursos(id)
);


-- Este seria el proceso para la eliminacion de la FK y la creacion de la FK en la tabla alumnos
-- NO REALIZAR ESTO!
ALTER TABLE alumnos ADD COLUMN curso_id INT;
ALTER TABLE cursos DROP FOREIGN KEY cursos_ibfk_1;
ALTER TABLE cursos DROP COLUMN curso_id;
ALTER TABLE alumnos ADD FOREIGN KEY(curso_id) REFERENCES cursos(id);

INSERT INTO cursos VALUES   (DEFAULT, 'MATEMATICA', 'AMARILLO', 'MEDIO'),
							(DEFAULT, 'CTS', 'NARANJA', 'DIFICIL'),
                            (DEFAULT, 'ARTE', 'MORADO', 'FACIL'),
                            (DEFAULT, 'EDUCACION FISICA', 'VERDE', 'MEDIO'),
                            (DEFAULT, 'INGLES', 'CELESTE', 'FACIL'),
                            (DEFAULT, 'COMUNICACION', 'ROJO', 'DIFICIL');

INSERT INTO alumnos VALUES  (DEFAULT, 'Eduardo', 'de Rivero', 'Manrique', 'ederiveroman@gmail.com','974207075',1),
							(DEFAULT, 'Carla', 'Monterrosa', 'Macedo', 'cmonterrosa@gmail.com','974207074',3),
                            (DEFAULT, 'Juan', 'Perez', 'Rodriguez', 'jperez@gmail.com','974207076',5),
							(DEFAULT, 'Rodrigo', 'Buenaventura', 'Rodrigues', 'rbuenaventura@gmail.com','974159075',2),
                            (DEFAULT, 'Sofia', 'Baldarrago', 'Vera', 'sbaldarrago@gmail.com','972503648',6);


SELECT * FROM alumnos;
SELECT * FROM cursos WHERE id= 1;


-- 1. Seleccionar todos los cursos que sean FACIL o DIFICIL
SELECT * FROM cursos WHERE dificultad IN('FACIL','DIFICIL');

-- 2. Seleccionar todos los cursos que sean color AMARILLO o CELESTE y que sean dificultad MEDIO
SELECT * FROM cursos WHERE color IN('AMARILLO','CELESTE') AND dificultad='MEDIO';

SELECT * 
FROM alumnos
INNER JOIN cursos ON alumnos.curso_id = cursos.id
WHERE correo LIKE '%gmail%';

INSERT INTO alumnos VALUES (DEFAULT, 'Jhonatan', 'Maicelo', 'Roman', 'jmaicelo@gmail.com', '925361048', NULL);

-- LEFT JOIN
SELECT * 
FROM alumnos
LEFT JOIN cursos ON alumnos.curso_id = cursos.id;

-- RIGHT JOIN
SELECT * 
FROM alumnos
RIGHT JOIN cursos ON alumnos.curso_id = cursos.id;