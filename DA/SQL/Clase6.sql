--CREAR BASE DE DATOS --CREATE DATABASE Clase6;USE Clase6;--CREAR TABLA CLIENTES--CREATE TABLE Clientes(N_Cliente int NOT NULL PRIMARY KEY, Nombre varchar(20) NOT NULL, Sexo varchar(1) NOT NULL,Telefono varchar(10) NOT NULL,ID_Edad int NOT NULL);--INSERTAR EL CONTENIDO DENTRO DE TABLA CLIENTES--INSERT INTO ClientesVALUES (345,'Juan', 'M','34484056',8), (390,'Mariela', 'F','45835000',9), (398,'Cristian', 'M','45786349',1),(562,'Fernando', 'M','42568360',3),(610,'Fernando', 'M','42568360',3),(817,'Silvana', 'F','32583159',5);SELECT * FROM Clientes;SELECTN_Cliente,NombreFROM Clientes;SELECT distinct--N_Cliente,NombreFROM Clientes;SELECT N_Cliente as Usuario,Nombre as Cliente,Sexo Genero,Telefono as MovilFROM Clientes;SELECT *FROM Clienteswhere Sexo = 'M';SELECT *FROM Clienteswhere ID_Edad >= 3;SELECT N_Cliente AS usuario,ID_edad As edad,N_cliente + ID_edad AS SUMA,N_cliente - ID_edad AS RESTA,N_cliente * ID_edad AS MULTIPLICACION,N_cliente / ID_edad AS DIVISIONFROM Clientes;