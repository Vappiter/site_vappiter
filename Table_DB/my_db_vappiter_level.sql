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
-- Table structure for table `vappiter_level`
--

DROP TABLE IF EXISTS `vappiter_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vappiter_level` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vappiter_level`
--

LOCK TABLES `vappiter_level` WRITE;
/*!40000 ALTER TABLE `vappiter_level` DISABLE KEYS */;
INSERT INTO `vappiter_level` VALUES (1,'U3'),(2,'U2'),(3,'U1'),(4,'L1'),(5,'L2'),(6,'L3'),(7,'L4'),(8,'L5'),(9,'L6'),(10,'L7'),(11,'L8'),(12,'L9'),(13,'L10'),(14,'L11'),(15,'L12'),(16,'L13'),(17,'L14'),(18,'L15'),(19,'L16'),(20,'L17'),(21,'L18'),(22,'L33'),(23,'L19'),(24,'L20'),(25,'L21'),(26,'L22'),(27,'L23'),(28,'L24'),(29,'L25'),(30,'L26'),(31,'L27'),(32,'L28'),(33,'L29'),(34,'L30'),(35,'L31'),(36,'L32'),(37,'L34'),(38,'L49'),(39,'L35'),(40,'L36'),(41,'L37'),(42,'L38'),(43,'L39'),(44,'L40'),(45,'L41'),(46,'L42'),(47,'L43'),(48,'L44'),(49,'L45'),(50,'L46'),(51,'L47'),(52,'L48'),(53,'L50'),(54,'L51'),(55,'L52'),(56,'L53'),(57,'L54'),(58,'L55'),(59,'L56'),(60,'L57'),(61,'L58'),(62,'L59'),(63,'L60'),(64,'L61'),(65,'L62'),(66,'L63'),(67,'L64'),(68,'L65'),(69,'L66'),(70,'L67'),(71,'L68'),(72,'L69'),(73,'L70'),(74,'L71'),(75,'L72'),(76,'L73'),(77,'L74'),(78,'L75'),(79,'L76'),(80,'L77'),(81,'L78'),(82,'L79'),(83,'L81'),(84,'L82'),(85,'L84');
/*!40000 ALTER TABLE `vappiter_level` ENABLE KEYS */;
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
