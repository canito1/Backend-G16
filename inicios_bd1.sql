DROP DATABASE alumnos;

CREATE DATABASE alumnos;

USE alumnos;
SELECT * FROM alembic_version;

INSERT INTO usuarios (nombre, apellido, fechaNacimiento, correo, sexo)
VALUES ('Eduardo', 'de Rivero', '1192-08-01', 'ederiveroma@gmail.com', 'MASCULINO');

