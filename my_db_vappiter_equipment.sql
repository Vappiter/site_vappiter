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
-- Table structure for table `vappiter_equipment`
--

DROP TABLE IF EXISTS `vappiter_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vappiter_equipment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sernum` varchar(20) NOT NULL,
  `block_id` bigint DEFAULT NULL,
  `building_id` bigint DEFAULT NULL,
  `level_id` bigint DEFAULT NULL,
  `room_id` bigint DEFAULT NULL,
  `type_product_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vappiter_equipment_block_id_79a79af6_fk_vappiter_block_id` (`block_id`),
  KEY `vappiter_equipment_building_id_820ab97f_fk_vappiter_building_id` (`building_id`),
  KEY `vappiter_equipment_level_id_2d77d4bc_fk_vappiter_level_id` (`level_id`),
  KEY `vappiter_equipment_room_id_3f486762_fk_vappiter_room_id` (`room_id`),
  KEY `vappiter_equipment_type_product_id_1bafe19c_fk_vappiter_` (`type_product_id`),
  CONSTRAINT `vappiter_equipment_block_id_79a79af6_fk_vappiter_block_id` FOREIGN KEY (`block_id`) REFERENCES `vappiter_block` (`id`),
  CONSTRAINT `vappiter_equipment_building_id_820ab97f_fk_vappiter_building_id` FOREIGN KEY (`building_id`) REFERENCES `vappiter_building` (`id`),
  CONSTRAINT `vappiter_equipment_level_id_2d77d4bc_fk_vappiter_level_id` FOREIGN KEY (`level_id`) REFERENCES `vappiter_level` (`id`),
  CONSTRAINT `vappiter_equipment_room_id_3f486762_fk_vappiter_room_id` FOREIGN KEY (`room_id`) REFERENCES `vappiter_room` (`id`),
  CONSTRAINT `vappiter_equipment_type_product_id_1bafe19c_fk_vappiter_` FOREIGN KEY (`type_product_id`) REFERENCES `vappiter_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vappiter_equipment`
--

LOCK TABLES `vappiter_equipment` WRITE;
/*!40000 ALTER TABLE `vappiter_equipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `vappiter_equipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-31 19:03:44
