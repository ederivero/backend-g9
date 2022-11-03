-- Utilizando la base de datos colegio
-- crear la tabla de los padres de los alumnos
CREATE TABLE padres(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(200) NOT NULL,
	ape_paterno VARCHAR(50) NOT NULL,
    ape_materno VARCHAR(50) NOT NULL,
    telefono VARCHAR(10) NOT NULL
);

CREATE TABLE alumnos_padres(
	id INT PRIMARY KEY AUTO_INCREMENT,
    padre_id INT,
    alumno_id INT,
    -- Haciendo las referencias hacia las tablas respectivas
    FOREIGN KEY (padre_id) REFERENCES padres(id),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);


INSERT INTO padres VALUES (DEFAULT, 'Juan', 'Rodriguez', 'Cano', '925364155'),
						  (DEFAULT, 'Angel', 'Sanchez', 'Baldarrago', '936205489'),
                          (DEFAULT, 'Jimmy', 'Jara', 'Pomareda', '914253689'),
                          (DEFAULT, 'Juan', 'Barrientos', 'Romero', '936259568'),
                          (DEFAULT, 'Nohemi', 'Ayala', 'Romero', '929655748'),
                          (DEFAULT, 'Christian', 'Martinez', 'Martinez', '976859245');
                          
INSERT INTO alumnos_padres VALUES   (DEFAULT, 1,3),
									(DEFAULT, 1,2),
                                    (DEFAULT, 2,1),
                                    (DEFAULT, 3,2),
                                    (DEFAULT, 5,6),
                                    (DEFAULT, 3,6),
                                    (DEFAULT, 4,6),
                                    (DEFAULT, 4,4),
                                    (DEFAULT, 6,5),
                                    (DEFAULT, 6,4);

-- 1. Listar todos los Padres y sus alumnos_padres (usando inner join)
SELECT * FROM padres INNER JOIN alumnos_padres ON padres.id = alumnos_padres.padre_id;

-- 2. Listar todos los alumnos y sus alumnos_padres (usando inner join)
SELECT * FROM alumnos INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id;


SELECT * 
FROM alumnos 
	INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id
    INNER JOIN padres ON alumnos_padres.padre_id = padres.id;

-- Usando la anterior sentencia, agregar los cursos de los alumnos
SELECT * 
FROM alumnos 
	INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id
    INNER JOIN padres ON alumnos_padres.padre_id = padres.id
    INNER JOIN cursos ON alumnos.curso_id = cursos.id;

-- 1. De la clausula anterior solamente mostrar los resultados cuyo ape_paterno DEL PADRE sea Rodriguez o Jara
SELECT * 
FROM alumnos 
	INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id
    INNER JOIN padres ON alumnos_padres.padre_id = padres.id
    INNER JOIN cursos ON alumnos.curso_id = cursos.id 
WHERE padres.ape_paterno in ('Rodriguez', 'Jara');           