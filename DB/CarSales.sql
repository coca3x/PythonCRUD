--By Eduardo3X
CREATE DATABASE CarSales
USE CarSales
CREATE TABLE [dbo].[TblCars](
	[ID] [int] NOT NULL,
	[Name] [varchar](100) NULL,
	[Year] [int] NOT NULL,
	[Price] [float] NOT NULL)

INSERT INTO TblCars VALUES (1, 'Toyota Camry', 2018, 2000)
INSERT INTO TblCars VALUES (2, 'Honda Civic', 2019, 2200)
INSERT INTO TblCars VALUES (3, 'Chevrolet Silverado', 2017, 1800)
INSERT INTO TblCars VALUES (4, 'Ford F-150', 2020, 2500)
INSERT INTO TblCars VALUES (5, 'Nissan Altima', 2021, 3000)