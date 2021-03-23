-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: the_warehouse
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `idemployees` int NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(45) DEFAULT NULL,
  `employee_last_name` varchar(45) DEFAULT NULL,
  `employee_address` varchar(45) DEFAULT NULL,
  `employee_sector` varchar(45) DEFAULT NULL,
  `idpermisions` int DEFAULT NULL,
  `employee_username` varchar(45) DEFAULT NULL,
  `employee_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idemployees`)
) ENGINE=InnoDB AUTO_INCREMENT=247 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Ismet','Mujezinovic','Tesanj','administartion',1,'ipo','123'),(2,'Berina','Mujezinovic','Tesanj','administration',2,'ber','123'),(3,'Jenny','Salibasic','Lepenica','saler',4,'jen','123'),(4,'Ermin','Salibasic','Lepenica','saler',4,'erm','123'),(6,'Eman','Subasic','Tesanj','saler',4,'ema','123'),(9,'Kenan','Topcic','Maglaj','saler',4,'ken','789'),(10,'Adnan','Brkic','Vukovo,Tesanj','Administration',2,'ado','123'),(11,'Hamdija','Husic','Tesanj','Sale',4,'ham','hus'),(13,'Husein','Husibegovic','Kotlanice','administration',1,'hus','123'),(14,'Nermin','Mulbdic','Tesanj','saler',4,'ner','456'),(244,'Senaid','Salkanovic','Alibegovci','administration',1,'sen','123'),(245,'Dzenana','Subasic','Tesanj','administration',1,'dyen','123');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisions`
--

DROP TABLE IF EXISTS `permisions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisions` (
  `idpermisions` int NOT NULL AUTO_INCREMENT,
  `permision_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpermisions`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisions`
--

LOCK TABLES `permisions` WRITE;
/*!40000 ALTER TABLE `permisions` DISABLE KEYS */;
INSERT INTO `permisions` VALUES (1,'superuser'),(2,'administrator'),(3,'user'),(4,'saler');
/*!40000 ALTER TABLE `permisions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_type`
--

DROP TABLE IF EXISTS `product_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_type` (
  `idproduct_type` int NOT NULL AUTO_INCREMENT,
  `product_type_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idproduct_type`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_type`
--

LOCK TABLES `product_type` WRITE;
/*!40000 ALTER TABLE `product_type` DISABLE KEYS */;
INSERT INTO `product_type` VALUES (1,'Motorna ulja'),(2,'Prehrana'),(3,'Auto kozmetika');
/*!40000 ALTER TABLE `product_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `idproducts` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(45) NOT NULL,
  `idproduct_type` int NOT NULL,
  `product_code` int NOT NULL,
  `product_quantity` int NOT NULL,
  `idsupplier` int DEFAULT NULL,
  `product_price` float DEFAULT NULL,
  PRIMARY KEY (`idproducts`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'HG Line 10w40 1lit',1,1000001,500,1,9.5),(2,'HG Line 10w40 4lit',1,1000001,500,1,28.5),(3,'HG line 5w40 1lit',1,1000003,400,1,12.59),(6,'Kinder Bueno',2,10004567,800,4,0.99),(8,'Auto Kristal 3lit',3,1001234,200,5,2.99),(9,'HG line TraktOL 10w40 4lit',1,10040450,500,1,68.2),(10,'Cokolada Zlatna Dzezva',2,10004555,2000,2,1.7);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `idsupplier` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(45) DEFAULT NULL,
  `supplier_location` varchar(45) DEFAULT NULL,
  `supplier_address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsupplier`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Olma','Slovenia','Ljubljana'),(2,'AS-Holding','BiH','Jelah'),(4,'Violeta','BiH','Grude'),(8,'Planet','BiH','Sarajevo'),(9,'Violeta','BiH','Grude');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-22 22:34:24
