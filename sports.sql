CREATE DATABASE  IF NOT EXISTS `sports` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sports`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: sports
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `achievements`
--

DROP TABLE IF EXISTS `achievements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `achievements` (
  `recordid` char(10) NOT NULL,
  `recorddate` date DEFAULT NULL,
  `position` int DEFAULT NULL,
  `awardorg` varchar(20) DEFAULT NULL,
  `cashprize` int DEFAULT NULL,
  `SRN` char(13) DEFAULT NULL,
  PRIMARY KEY (`recordid`),
  KEY `SRN` (`SRN`),
  CONSTRAINT `achievements_ibfk_1` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `achievements`
--

LOCK TABLES `achievements` WRITE;
/*!40000 ALTER TABLE `achievements` DISABLE KEYS */;
/*!40000 ALTER TABLE `achievements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allotments`
--

DROP TABLE IF EXISTS `allotments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allotments` (
  `allot_time` time NOT NULL,
  `returntime` time NOT NULL,
  `SRN` char(13) DEFAULT NULL,
  `equipid` char(10) DEFAULT NULL,
  KEY `SRN` (`SRN`),
  KEY `equipid` (`equipid`),
  CONSTRAINT `allotments_ibfk_1` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`),
  CONSTRAINT `allotments_ibfk_2` FOREIGN KEY (`equipid`) REFERENCES `equipment` (`equipid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allotments`
--

LOCK TABLES `allotments` WRITE;
/*!40000 ALTER TABLE `allotments` DISABLE KEYS */;
/*!40000 ALTER TABLE `allotments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `SRN` char(13) DEFAULT NULL,
  `courtid` char(5) DEFAULT NULL,
  KEY `SRN` (`SRN`),
  KEY `courtid` (`courtid`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`courtid`) REFERENCES `court` (`courtid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `court`
--

DROP TABLE IF EXISTS `court`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `court` (
  `courtid` char(5) NOT NULL,
  `courttype` varchar(15) DEFAULT NULL,
  `courtdesc` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`courtid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `court`
--

LOCK TABLES `court` WRITE;
/*!40000 ALTER TABLE `court` DISABLE KEYS */;
/*!40000 ALTER TABLE `court` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `equipid` char(10) NOT NULL,
  `equipname` varchar(15) NOT NULL,
  `buydate` date DEFAULT NULL,
  PRIMARY KEY (`equipid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `penalties`
--

DROP TABLE IF EXISTS `penalties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `penalties` (
  `paymentid` char(10) NOT NULL,
  `paymentmode` varchar(10) DEFAULT NULL,
  `reason` varchar(20) NOT NULL,
  `paymentdate` date NOT NULL,
  `SRN` char(13) DEFAULT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `SRN` (`SRN`),
  CONSTRAINT `penalties_ibfk_1` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penalties`
--

LOCK TABLES `penalties` WRITE;
/*!40000 ALTER TABLE `penalties` DISABLE KEYS */;
/*!40000 ALTER TABLE `penalties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `SRN` char(13) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contactno` char(10) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `bloodgroup` enum('A+','B+','AB+','O+','A-','B-','AB-','O-') DEFAULT NULL,
  PRIMARY KEY (`SRN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_trainer`
--

DROP TABLE IF EXISTS `student_trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_trainer` (
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `SRN` char(13) DEFAULT NULL,
  `trainerid` char(10) DEFAULT NULL,
  KEY `SRN` (`SRN`),
  KEY `trainerid` (`trainerid`),
  CONSTRAINT `student_trainer_ibfk_1` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`),
  CONSTRAINT `student_trainer_ibfk_2` FOREIGN KEY (`trainerid`) REFERENCES `trainer` (`trainerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_trainer`
--

LOCK TABLES `student_trainer` WRITE;
/*!40000 ALTER TABLE `student_trainer` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainer`
--

DROP TABLE IF EXISTS `trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainer` (
  `trainerid` char(10) NOT NULL,
  `trainername` varchar(20) NOT NULL,
  `trainercontact` char(10) DEFAULT NULL,
  `trainerspec` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`trainerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainer`
--

LOCK TABLES `trainer` WRITE;
/*!40000 ALTER TABLE `trainer` DISABLE KEYS */;
/*!40000 ALTER TABLE `trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Sex` enum('M','F') NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Password` varchar(20) NOT NULL,
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Jugal','Kothari','M','jugalprakashk19@gmail.com','jugal123'),('Kshitij','Agarwal','M','kshitijagarwal28@gmail.com','kshitij123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-18  9:38:07
