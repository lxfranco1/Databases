-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: twitterinfluence
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `isa`
--

DROP TABLE IF EXISTS `isa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `isa` (
  `isa_oc_url` varchar(255) NOT NULL,
  `isa_re_url` varchar(255) NOT NULL,
  `isa_username` char(15) NOT NULL,
  PRIMARY KEY (`isa_oc_url`,`isa_username`),
  KEY `isa_username_idx` (`isa_username`),
  CONSTRAINT `isa_oc_url_fk` FOREIGN KEY (`isa_oc_url`) REFERENCES `tweet` (`oc_url`),
  CONSTRAINT `isa_username_fk` FOREIGN KEY (`isa_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `posts_oc_url` varchar(255) NOT NULL,
  `posts_username` varchar(15) NOT NULL,
  PRIMARY KEY (`posts_oc_url`,`posts_username`),
  KEY `posts_username_fk1` (`posts_username`),
  CONSTRAINT `posts_oc_url_fk` FOREIGN KEY (`posts_oc_url`) REFERENCES `tweet` (`oc_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repost`
--

DROP TABLE IF EXISTS `repost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repost` (
  `repost_re_url` varchar(255) NOT NULL,
  PRIMARY KEY (`repost_re_url`),
  CONSTRAINT `repost_re_url` FOREIGN KEY (`repost_re_url`) REFERENCES `retweet` (`re_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `retweet`
--

DROP TABLE IF EXISTS `retweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `retweet` (
  `re_url` varchar(255) NOT NULL,
  `re_username` varchar(15) NOT NULL,
  `re_location` mediumtext,
  `re_date` datetime NOT NULL,
  `re_likes` int(11) NOT NULL,
  `re_replies` int(11) NOT NULL,
  PRIMARY KEY (`re_url`),
  KEY `re_username_fk` (`re_username`),
  CONSTRAINT `re_username_fk` FOREIGN KEY (`re_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tweet`
--

DROP TABLE IF EXISTS `tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweet` (
  `oc_url` varchar(255) NOT NULL,
  `oc_date` datetime NOT NULL,
  `oc_likes` int(11) NOT NULL,
  `oc_location` mediumtext,
  `oc_username` char(15) NOT NULL,
  `oc_replies` int(11) NOT NULL,
  PRIMARY KEY (`oc_url`),
  KEY `oc_username_fk` (`oc_username`),
  CONSTRAINT `oc_username_fk` FOREIGN KEY (`oc_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` char(15) NOT NULL,
  `name` char(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-04 10:13:26
