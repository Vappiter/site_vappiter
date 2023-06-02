-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: my_db
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

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
-- Table structure for table `vappiter_product`
--

DROP TABLE IF EXISTS `vappiter_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vappiter_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product` varchar(50) NOT NULL,
  `company_id` bigint DEFAULT NULL,
  `titleproduct_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vappiter_product_company_id_06e7f91e_fk_vappiter_company_id` (`company_id`),
  KEY `vappiter_product_titleproduct_id_9db19bf6_fk_vappiter_` (`titleproduct_id`),
  CONSTRAINT `vappiter_product_company_id_06e7f91e_fk_vappiter_company_id` FOREIGN KEY (`company_id`) REFERENCES `vappiter_company` (`id`),
  CONSTRAINT `vappiter_product_titleproduct_id_9db19bf6_fk_vappiter_` FOREIGN KEY (`titleproduct_id`) REFERENCES `vappiter_titleproduct` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vappiter_product`
--

LOCK TABLES `vappiter_product` WRITE;
/*!40000 ALTER TABLE `vappiter_product` DISABLE KEYS */;
INSERT INTO `vappiter_product` VALUES (37,'Cisco Catalyst WS-C2960RX-48FPD-L',1,1),(38,' GLC-LH-SMD=',1,2),(39,'Cisco Catalyst WS-C4500X-40X-ES',1,1),(40,'SFP-10G-LR-S=',1,3),(41,'GLC-TE',1,4),(42,'C4KX-PWR-750AC-R',1,5),(43,'C4KX-PWR-750AC-R/2',1,5),(44,'WS-C6509-V-E',1,6),(45,'VS-S2T-10G',1,7),(46,'C6800-16P10G',1,8),(47,'WS-CAC-6000W',1,5),(48,'WS-C6509-V-E-FAN',1,9),(49,'Cisco Catalyst WS-C2960RX-48TS-L',1,1),(50,'C2960X-STACK=',1,10),(51,'Cisco Catalyst WS-C2960X-24PD-L',1,1),(52,'PI-UCS-APL-K9',1,11),(53,'PI-UCS-H900G10K12G',1,12),(54,'RJ-45 DFC4 C6800-48P-TX=',1,13);
/*!40000 ALTER TABLE `vappiter_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-02 12:36:06
