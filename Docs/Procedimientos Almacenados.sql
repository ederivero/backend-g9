USE restaurante;
-- Se usa la palabra DELIMITER que sirve para indicar que hasta que no vuelva a encontrar la palabra
-- todo sera parte del comando
DELIMITER //
CREATE PROCEDURE DevolverTodosLosUsuarios()
BEGIN
	SELECT * FROM usuarios;
    -- El procedimiento almacenado (stored procedure) sirve para un conjunto de operaciones
	-- INSERT INTO platos (...
END //

DELIMITER ;

-- Ahora un SP con parametros
-- en este caso declaramos un parametro de entrada (IN) y a su vez le ponemos un nombre al delimitador
-- Si queremos indicar un parametro de salida (OUT) 
DROP PROCEDURE IF EXISTS DevolverUsuariosSegunTipo;
DELIMITER //
CREATE PROCEDURE DevolverUsuariosSegunTipo(IN tipo varchar(40), OUT usuarioId INT)
BEGIN
	-- Funciones de agregacion (count, sum, avg, max, min, )
    -- https://www.mysqltutorial.org/mysql-aggregate-functions.aspx
    -- COUNT > contabilice cuantos usuarios hay de ese tipo
	SELECT COUNT(id) INTO usuarioId FROM usuarios WHERE tipo_usuario = tipo;
END //

DELIMITER ;


CALL DevolverTodosLosUsuarios();
CALL DevolverUsuariosSegunTipo('ADMIN', @usuarioId);
SELECT @usuarioId ;


CALL DevolverUsuariosSegunTipo('USER', @usuarioUser);
SELECT @usuarioUser;

