-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: localhost
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudad` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES (1,'Ciudad de México','01000'),(2,'Guadalajara','44100'),(3,'Monterrey','64000'),(4,'Cancún','77500'),(5,'Puebla','72000'),(6,'Mérida','97000'),(7,'Tijuana','22000'),(8,'Culiacán','80000'),(9,'Oaxaca','68000'),(10,'León','37000'),(11,'Aguascalientes','20000'),(12,'Chihuahua','31000'),(13,'Hermosillo','83000'),(14,'Saltillo','25000'),(15,'Torreón','27000'),(16,'San Luis Potosí','78000'),(17,'Mazatlán','82000'),(18,'Veracruz','91700'),(19,'Durango','34000'),(20,'Morelia','58000'),(21,'Querétaro','76000'),(22,'Toluca','50000'),(23,'Zacatecas','98000'),(24,'Tuxtla Gutiérrez','29000'),(25,'Xalapa','91000'),(26,'Colima','28000'),(27,'Villahermosa','86000'),(28,'Manzanillo','28200'),(29,'Nogales','84000'),(30,'Cuernavaca','62000'),(31,'Irapuato','36500'),(32,'Ensenada','22800'),(33,'Mazatlán','82000'),(34,'Reynosa','88700'),(35,'Pachuca','42000'),(36,'San Cristóbal de las Casas','29200'),(37,'Celaya','38000'),(38,'Tapachula','30700'),(39,'Apatzingán','60600'),(40,'La Paz','23000'),(41,'Chilpancingo','39000'),(42,'Coatzacoalcos','96500'),(43,'Matamoros','87400'),(44,'Los Cabos','23400'),(45,'Campeche','24000'),(46,'Tehuacán','75800'),(47,'Guaymas','85400'),(48,'Nogales','84000'),(49,'Chetumal','77000'),(50,'Lázaro Cárdenas','60900'),(51,'Tlaxcala','90000'),(52,'sexolandia','10');
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-05 14:52:31
