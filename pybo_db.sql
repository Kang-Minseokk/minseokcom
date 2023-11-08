-- MySQL dump 10.13  Distrib 8.1.0, for macos13.3 (arm64)
--
-- Host: localhost    Database: pybo_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question_id` int DEFAULT NULL,
  `content` text NOT NULL,
  `create_date` datetime NOT NULL,
  `user_id` int NOT NULL,
  `modify_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE,
  CONSTRAINT `answer_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,1,'123123','2023-08-17 08:32:33',2,'2023-08-17 08:32:36'),(2,12,'wee','2023-08-28 09:08:17',2,NULL),(3,33,'dfasdf','2023-08-28 14:26:53',2,'2023-08-28 14:26:56'),(4,33,'안녕하세요\r\n','2023-08-28 16:45:41',3,'2023-08-28 16:45:48'),(5,35,'카테고리를 모든 화면에 보이게끔 코드 수정하기\r\n','2023-08-29 11:52:25',3,NULL),(7,32,'답변 삭제는 가능하다. 하지만 질문의 삭제는 아직 안된다.','2023-08-29 11:54:20',3,NULL),(8,38,'답변1','2023-08-29 15:52:43',3,NULL),(9,116,'df','2023-09-22 11:20:46',3,NULL),(10,117,'답변입니다','2023-09-22 11:30:28',3,NULL),(11,117,'답변입니다2','2023-09-22 11:30:35',3,NULL),(12,119,'pdf','2023-09-26 16:37:56',3,NULL),(13,119,'sd','2023-09-26 16:37:57',3,NULL),(14,119,'adf','2023-09-26 16:43:42',3,NULL),(15,119,'asdf','2023-09-26 16:43:43',3,NULL),(16,119,'asdf','2023-09-26 16:43:44',3,NULL),(17,119,'asd','2023-09-26 16:43:45',3,NULL),(18,119,'pdf','2023-09-26 16:43:46',3,NULL),(19,119,'asdf','2023-09-26 16:43:47',3,NULL),(20,119,'asdf','2023-09-26 16:43:48',3,NULL),(21,119,'adf','2023-09-26 16:43:49',3,NULL),(22,119,'asdf','2023-09-26 16:43:50',3,NULL),(23,119,'ad','2023-09-26 16:43:52',3,NULL),(24,119,'asd','2023-09-26 16:43:53',3,NULL),(25,119,'add','2023-09-26 16:43:54',3,NULL),(26,119,'safd','2023-09-26 16:43:55',3,NULL),(27,119,'asdf','2023-09-26 16:43:56',3,NULL),(28,119,'sad','2023-09-26 16:43:57',3,NULL),(29,121,'pdf','2023-09-26 16:44:19',3,NULL),(30,119,'asdfasdfasdlfnasdlfkjnalsdnf;kljndkfjnaskdjnkasjndkas;dfas;djf','2023-09-26 17:10:38',3,NULL),(31,130,'앵커로 이도해야 합니다','2023-10-11 10:13:48',3,NULL),(32,16,'답변 입니다. 답변을 수정해봅니다','2023-10-12 15:24:13',3,'2023-10-12 15:24:24'),(33,129,'답변','2023-10-13 10:37:14',3,NULL),(34,117,'답변','2023-10-13 10:37:30',3,NULL),(35,136,'답변 222','2023-10-18 09:56:59',3,'2023-10-18 09:57:06'),(36,138,'답변','2023-10-18 13:53:03',3,NULL),(37,122,'?','2023-11-01 16:13:12',31,NULL),(38,147,'123','2023-11-03 14:59:00',31,NULL),(39,144,'sad','2023-11-03 15:01:19',31,NULL);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer_voter`
--

DROP TABLE IF EXISTS `answer_voter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer_voter` (
  `user_id` int NOT NULL,
  `answer_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`answer_id`),
  KEY `answer_id` (`answer_id`),
  CONSTRAINT `answer_voter_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `answer_voter_ibfk_2` FOREIGN KEY (`answer_id`) REFERENCES `answer` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_voter`
--

LOCK TABLES `answer_voter` WRITE;
/*!40000 ALTER TABLE `answer_voter` DISABLE KEYS */;
INSERT INTO `answer_voter` VALUES (3,3);
/*!40000 ALTER TABLE `answer_voter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendar`
--

DROP TABLE IF EXISTS `calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES (1,'일정 1','2023-09-11 00:00:00','2023-09-15 00:00:00','...'),(2,'일정 2','2023-09-20 00:00:00','2023-09-22 00:00:00','일정 2입니다!'),(3,'일정 3','2023-09-12 00:00:00','2023-09-13 00:00:00','일정 3이다'),(4,'일정 4','2023-09-28 00:00:00','2023-09-30 00:00:00','일정 4'),(5,'일정5','2023-09-26 00:00:00','2023-09-28 00:00:00','...'),(6,'중요','2023-09-20 00:00:00','2023-09-23 00:00:00','목표 완료'),(7,'하루','2023-09-24 00:00:00','2023-09-26 00:00:00','1'),(8,'하루','2023-09-25 00:00:00','2023-09-26 00:00:00','하루'),(9,'12','2023-09-07 00:00:00','2023-09-09 00:00:00','12'),(10,'asd','2023-09-05 00:00:00','2023-09-14 00:00:00','as'),(11,'test','2023-09-25 00:00:00','2023-09-27 00:00:00','...'),(18,'새일정1','2023-10-04 00:00:00','2023-10-07 00:00:00','1'),(19,'일정 1','2023-10-09 00:00:00','2023-10-11 00:00:00','...'),(20,'일정 123','2023-10-16 00:00:00','2023-10-19 00:00:00','123'),(21,'일정 제목이 일정 길이가 넘어가는 경우에','2023-10-31 00:00:00','2023-10-26 00:00:00','일정 길이123'),(22,'일정 길이가 일정의 레이아웃보다 큰 경우에는 생략한다.','2023-10-14 00:00:00','2023-10-15 00:00:00','일정'),(23,'오늘','2023-10-02 00:00:00','2023-10-04 00:00:00','일정'),(24,'카카오 기능 구현하기','2023-10-31 00:00:00','2023-11-03 00:00:00','카카오 로그인 기능 및 로그아웃 기능 구현하기');
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (58,'새로운 카테고리1'),(59,'새로운 카테고리2'),(60,'123');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `content` text NOT NULL,
  `create_date` datetime NOT NULL,
  `modify_date` datetime DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `question_id` (`question_id`),
  KEY `answer_id` (`answer_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_3` FOREIGN KEY (`answer_id`) REFERENCES `answer` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,2,'123312','2023-08-17 08:32:39','2023-08-17 08:32:44',NULL,1),(2,2,'asdf','2023-08-28 14:27:04',NULL,NULL,3),(3,2,'asdf','2023-08-28 14:27:07',NULL,33,NULL),(4,3,'댓글 추가하는 칸에서도 카테고리 화면의 고정\r\n','2023-08-29 11:52:44',NULL,NULL,5),(5,3,'댓글의 댓글도 카테고리 고정이 가능하다.','2023-08-29 11:54:33',NULL,NULL,7),(8,3,'엥','2023-09-27 07:43:26',NULL,119,NULL),(9,3,'답변의 답변입니다\r\n','2023-10-12 15:24:33',NULL,NULL,32),(10,3,'댓글','2023-10-13 10:37:43',NULL,114,NULL),(11,31,'asdasdf','2023-11-01 16:13:17',NULL,NULL,37);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_visit`
--

DROP TABLE IF EXISTS `daily_visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_visit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `visit_list` text,
  `count` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_visit`
--

LOCK TABLES `daily_visit` WRITE;
/*!40000 ALTER TABLE `daily_visit` DISABLE KEYS */;
INSERT INTO `daily_visit` VALUES (1,'2023-10-10','[1, 2, 5]',3),(2,'2023-10-11','[3, 21, 13, 14]',4),(3,'2023-10-12','[1, 2]',2),(4,'2023-10-13','[1, 2]',2),(5,'2023-10-14','[1, 2, 3]',3),(6,'2023-10-15','[2, 3, 4]',3),(7,'2023-10-16','[2, 3, 4]',3),(8,'2023-10-17','[1, 14, 15, 16]',4),(9,'2023-10-18','[16, 3, 13, 14]',4),(10,'2023-10-19','[3, 13]',2),(11,'2023-10-20','[13, 3, 14]',3),(12,'2023-10-21','[3]',1),(13,'2023-10-23','[3]',1),(14,'2023-10-24','[3]',1),(15,'2023-10-25','[3]',1),(16,'2023-10-26','[3, 15]',2),(17,'2023-10-30','[3, 13]',2),(18,'2023-10-31','[3]',1),(19,'2023-11-01','[3, 15, 16, 31]',4),(20,'2023-11-02','[3, 31]',2),(21,'2023-11-03','[31]',1),(22,'2023-11-06','[3]',1),(23,'2023-11-07','[]',0),(24,'2023-11-08','[31, 35, 37]',3);
/*!40000 ALTER TABLE `daily_visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goal`
--

DROP TABLE IF EXISTS `goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `period` varchar(100) NOT NULL,
  `done` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goal`
--

LOCK TABLES `goal` WRITE;
/*!40000 ALTER TABLE `goal` DISABLE KEYS */;
INSERT INTO `goal` VALUES (1,'월 목표1','월 목표1','month',1),(2,'월 목표2','월 목표2ㅇㅇㅇ','month',0),(3,'월 목표3','월 목표3','month',0),(4,'연 목표1','연 목표1','year',0),(5,'연 목표2','연 목표2','year',0),(7,'연 목표4','연 목표4','year',1),(8,'월 목표4','테이블의 크기보다 텍스트의 길이가 긴 경우 초과되는 텍스트는 생략한다.\r\ninput 태그는 기본적으로 줄바꿈 요소를 지원해주지 않는다\r\n심지어 엔터를 쳐도 텍스트 부분에서 줄 바꿈이 되는 것이 아니라 버튼이 눌린다. \r\n','month',1),(9,'월 목표5','월 목표5 수정입니다','month',1),(12,'12','123','month',1),(14,'책1','책1입니다','book',0),(15,'책2 ','책2입니다','book',0),(16,'목표의 제목이 일정 너비를 넘어가면 ...으로 표시한다.','...','month',0),(17,'일정 길이를 넘어가는 경우에 유동적으로 길이가 변하는 것이 아니라, 고정된 길이를 가지고 있어야 한다. 길이를 초과하면 생략한다.','...','month',0),(18,'목표 생성하기 1(수정)','....','month',1);
/*!40000 ALTER TABLE `goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kakao`
--

DROP TABLE IF EXISTS `kakao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kakao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `profile_img` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123123132 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kakao`
--

LOCK TABLES `kakao` WRITE;
/*!40000 ALTER TABLE `kakao` DISABLE KEYS */;
INSERT INTO `kakao` VALUES (123123131,'dreampilot920@naver.com','http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg');
/*!40000 ALTER TABLE `kakao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `create_date` datetime NOT NULL,
  `user_id` int DEFAULT NULL,
  `modify_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `tag` varchar(30) DEFAULT 'etc',
  `views` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'123',' 123','2023-08-17 08:32:26',2,NULL,'Data Science',NULL,1),(2,'1234','  13 ','2023-08-17 09:55:45',1,NULL,'Development','flask',0),(3,'123123312123',' 123123123','2023-08-17 10:38:12',1,NULL,'Communication',NULL,1),(4,'wqer',' ewer','2023-08-17 11:23:14',1,NULL,'Communication','com',4),(5,'ㅈㄷㄱ',' ㅂㅈㄷㄱ','2023-08-17 11:34:07',1,NULL,'Communication','free',3),(6,'123',' 123','2023-08-18 13:20:43',2,NULL,'Development','python',4),(7,'123','   12','2023-08-18 13:20:56',2,NULL,'Communication',NULL,3),(8,'we','we','2023-08-18 13:21:21',2,NULL,'Artificial Intelligence',NULL,1),(9,'ㅈㅂㅇ',' ㅊㅈㅇㅂ','2023-08-18 14:01:45',2,NULL,'Computer Science',NULL,5),(10,'12','  123','2023-08-28 08:25:07',2,NULL,'Development','ai',0),(11,'ew','    qwer','2023-08-28 08:33:33',2,NULL,'Development','javascript',0),(12,'12','       ㄷ12','2023-08-28 08:51:33',2,NULL,'Data Science','java',1),(13,'123',' 123','2023-08-28 09:02:21',2,NULL,'Data Science',NULL,2),(14,'ㅈㄷㄱ',' ㅂㅈㄱ','2023-08-28 09:04:43',2,NULL,'Development','github',0),(15,'ㅂㅈㄷㄹㅇ',' ㅁㄴㅇ','2023-08-28 09:24:30',2,NULL,'Development','java',0),(16,'ㄴㅇㄹ',' ㅁㄴㅇ','2023-08-28 09:24:41',2,NULL,'Data Science',NULL,2),(17,'ㅂㅈㄷㄹ','   ㄹㅂㅈewfd','2023-08-28 09:35:05',2,'2023-08-28 09:56:23','Development','html',1),(18,'qwer','  qwefqdfsafa','2023-08-28 09:55:02',2,NULL,'Development',NULL,0),(19,'qwer','  qwefqdfsafa','2023-08-28 09:55:10',2,NULL,'Development',NULL,0),(20,'qwer','  qwefqdfsafa','2023-08-28 09:55:23',2,NULL,'Development',NULL,0),(21,'qwer','  qwefqdfsafa','2023-08-28 09:55:57',2,NULL,'Development',NULL,0),(22,'awe',' ewer','2023-08-28 11:43:09',2,NULL,'Data Science',NULL,2),(23,'wqer',' where','2023-08-28 11:43:16',2,NULL,'Artificial Intelligence',NULL,0),(24,'qwer',' qwerw','2023-08-28 11:43:26',2,NULL,'Artificial Intelligence',NULL,1),(25,'asdf',' asdf','2023-08-28 11:56:19',2,NULL,'Data Science',NULL,1),(26,'ander',' dfa','2023-08-28 11:58:36',2,NULL,'Computer Science',NULL,28),(27,'123ㄷㅇㅁㄴ',' ㅁㄴㅇㄹㅁㄴ','2023-08-28 13:17:11',2,NULL,'Development',NULL,0),(28,'ㅂㄷㅈㄴㄹ',' ㅁㄴㅇㄹ','2023-08-28 13:20:23',2,NULL,'Data Science',NULL,1),(29,'ㅂㅈㄷㄹ',' ㅁㅇ','2023-08-28 13:20:28',2,NULL,'Data Science',NULL,1),(30,'ㅁㄴㅇㄹ',' ㄴㅁㅇ','2023-08-28 13:20:33',2,NULL,'Data Science',NULL,1),(32,'플라스큼',' ㄴㄴㅇㄹ','2023-08-28 13:20:53',2,NULL,'Data Science',NULL,1),(33,'wqer','   whereasdf','2023-08-28 13:31:44',2,'2023-08-28 14:25:30','Data Science',NULL,1),(34,'Javascript의 FullCalender을 이용하여 달력 표현하기.',' {% extends \'base.html\' %}\r\n{% block content %}\r\n<html lang=\"en\">\r\n<head>\r\n<meta charset=\"UTF-8\">\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n<link href=\"https://cdn.jsdelivr.net/npm/fullcalendar@5.5.0/main.css\" rel=\"stylesheet\">\r\n<script src=\"https://cdn.jsdelivr.net/npm/fullcalendar@5.5.0/main.js\"></script>\r\n</head>\r\n<body>\r\n<div id=\"calendar\"></div>\r\n<script>\r\n  document.addEventListener(\'DOMContentLoaded\', function() {\r\n    var calendarEl = document.getElementById(\'calendar\');\r\n\r\n    var calendar = new FullCalendar.Calendar(calendarEl, {\r\n      initialView: \'dayGridMonth\', // 월별 뷰\r\n      events: [\r\n        // 이벤트 데이터를 추가하거나 API 요청을 통해 데이터를 가져와 추가할 수 있음\r\n        {% for event in events %}\r\n        {\r\n          title: \'{{ event.title }}\',\r\n          start: \'{{ event.start_date }}\',\r\n          end: \'{{ event.end_date }}\'\r\n        },\r\n        {% endfor %}\r\n      ]\r\n    });\r\n\r\n    calendar.render(); // 달력 렌더링\r\n  });\r\n</script>\r\n</body>\r\n</html>\r\n{% endblock %}\r\n이와 같이 작성을 하면 오늘의 날짜를 표현한 달력이 나타난다.','2023-08-28 13:36:00',2,NULL,'Development',NULL,1),(35,'코드 본문에 작성해보기',' <html lang=\"en\">','2023-08-28 13:36:39',2,NULL,'Development',NULL,0),(38,'이미지 등록하는 방법',' !  data:image/jpeg;base64,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','2023-08-29 14:03:33',3,'2023-08-29 15:52:33','Development',NULL,0),(39,'질문의 개수','질문이 4개가 되어야 테이블 헤드의 크기가 줄어드는 것인지 확인해보도록 한다.','2023-08-30 08:30:07',3,NULL,'Artificial Intelligence',NULL,2),(40,'특수기호가 입력되지 않는 오류가 존재한다.','    <>/\\{}[]()!@#$%^&*_+ \r\n<li class=\"page-item disabled\">\r\n    <a class=\"page-link\" tabindex=\"-1\" aria-disabled=\"true\" href=\"#\">다음</a>\r\n</li>','2023-08-30 13:30:47',3,'2023-08-30 13:31:52','Data Science',NULL,4),(42,'form','form에 대한 코드를 작성할 때 \r\nSelectField와 TextField의 차이가 있을까','2023-09-05 11:24:20',3,NULL,'Development',NULL,0),(43,'플라스크로 웹사이트 구축하기 위한 첫단계','1. 가상환경을 위한 디렉터리와 프로젝트를 모으기 위한 프로젝트 루트 디렉터리를 만든다.\r\n가상환경은 필수가 아니지만 가상환경에서 프로젝트를 만들었을 경우 프로젝트의 독립적인 관리를 용이하게 해주기 때문에 가상환경을 사용한다. \r\n가상환경을 설치하기 위해서는 pyhon3 -m venv (가상환경 이름) 을 입력한다.\r\n2. 가상환경 진입하기\r\n가상환경 진입을 위해서 맥에서는 \r\ncd (가상환경 이름)/bin\r\nsource activate\r\n라고 입력해주면 된다.\r\n3. 가상환경에 진입하기 위해서 이 모든것을 반복적으로 입력하려면 시간이 걸리므로 편의를 위해 vim editor를 이용해서 내가 설정한 명령어로 가상환경에 진입할 수 있게끔 한다.\r\nvim editor에 들어가기 위해서는 vi .zshrc 라고 입력하면 된다. 그 후 설정값을 입력해주면 된다.\r\n4. 해당 가상환경에 플라스라고 하는 파이썬 웹 프레임워크를 pip을 이용해서 다운로드 해주면 된다.\r\n5. 가상환경이 실행되는 디렉토리 아래에 파이썬 디렉터리 또는 패키지를 두고 사용하면 된다.','2023-09-07 08:42:33',3,NULL,'Development',NULL,0),(44,'코드를 입력할 수 있나요?','{% extends \'base.html\' %}\r\n{% block content %}\r\nasdfasfasdf\r\n    <div class=\"table-container m-5\">\r\n        <h5 class=\"my-3 border-bottom pb-2\">질문등록</h5>\r\n        <form method=\"post\" class=\"post-form my-3\">\r\n            {{ form.csrf_token }}\r\n            <!-- 오류표시 start -->\r\n            {% for field, errors in form.errors.items() %}\r\n            <div class=\"alert alert-danger\" role=\"alert\">\r\n                <strong>{{ form[field].label }}</strong>: {{ \', \'.join(errors) }}\r\n            </div>\r\n            {% endfor %}\r\n            <!-- 오류표시 End -->\r\n            <div class=\"form-group\">\r\n                <label for=\"subject\">제목</label>\r\n                <input type=\"text\" class=\"form-control\" name=\"subject\" id=\"subject\" value=\"{{ form.subject.data or \'\' }}\">\r\n            </div>\r\n            <div class=\"form-group\">\r\n                <label for=\"content\">내용</label>\r\n                <textarea class=\"form-control\" name=\"content\" id=\"content\" rows=\"10\">{{ form.content.data or \'\' }}</textarea>\r\n            </div>\r\n            <div class=\"form-group\">\r\n                <label for=\"category\">카테고리</label>\r\n                <select class=\"form-control\" name=\"category\" id=\"category\">\r\n                    <option value=\"\">Select a category</option>\r\n                    <option value=\"Data Science\">Data Science</option>\r\n                    <option value=\"Development\">Development</option>\r\n                    <option value=\"Computer Science\">Computer Science</option>\r\n                    <option value=\"Artificial Intelligence\">Artificial Intelligence</option>\r\n                    <option value=\"Relaxation\">Relaxation</option>\r\n                    <option value=\"Communication\">Communication</option>\r\n                </select>\r\n            </div>\r\n            <button type=\"submit\" class=\"btn btn-primary\">저장하기</button>\r\n        </form>\r\n    </div>\r\n</div>\r\n{% endblock %}','2023-09-08 10:28:25',3,'2023-09-08 11:42:56','Development',NULL,0),(47,'코드입력','코드 입력을 할 때 코드가 해석되어 실행되지 않게끔 하기 위해서는 escape메서드를 사용하면 된다. \r\n','2023-09-08 11:03:07',3,'2023-09-12 08:54:09','Development',NULL,0),(49,'사진 등록하기','사진을 등록해보자','2023-09-12 11:36:45',4,NULL,'Development','c',0),(50,'이미지','파일로만 직접 이미지 파일을 가져올 수는 없다.','2023-09-12 11:58:30',5,NULL,'Development',NULL,0),(54,'업로드한 이미지를 원하는 경로에 저장하기','우선 이미지를 업로드 받는 html코드를 작성하겠다.\r\n<form method=\"post\" class=\"post-form\" enctype=\"multipart/form-data\">\r\n    <label for=\"profile_img\">프로필 사진</label>\r\n    <input type=\"file\" class=\"form-control\" name=\"profile_img\" id=\"profile_img\">\r\n</form>\r\n\r\nenctype은 form의 데이터 타입이 file인 경우 필수적으로 사용해주어야 한다. enctype=\"multipart/form-data\"이다.\r\n\r\n\r\n위와 같이 업로드된 이미지를 저장하자.\r\nprofile_img.save(os.path.join(\'/User/minseokkang/projects/myproject/pybo/static/image\', filename))\r\n이렇게 하면 이미지를 해당 주소에 저장할 수 있다.\r\n\r\n','2023-09-13 09:51:50',3,NULL,'Development',NULL,1),(55,'pagination 메서드를 사용한 페이징 처리','1. 뷰 함수에서는 페이지에 대한 정의와 쿼리 결과에 pagination메서드를 적용해준다.\r\npage = request.args.get(\'page\', type=int, default=1)\r\ngoal_list = Goal.query.filter(Goal.period == \'month\', Goal.done==False).paginate(page=page, per_page=5, error_out=False)\r\n\r\n2. 페이지의 번호를 보여주는 html코드는 다음과 같다.\r\n<ul class=\"pagination justify-content-center\">\r\n\r\n    {% if goal_list.has_prev %}\r\n        <li class=\"page-item\">\r\n            <a class=\"page-link\" href=\"?page={{ goal_list.prev_num }}\">이전</a>\r\n        </li>\r\n    {% else %}\r\n        <li class=\"page-item disabled\">\r\n            <a class=\"page-link\" href=\"#\" tabindex=\"-1\" aria-disabled=\"true\">이전</a>\r\n        </li>\r\n    {% endif %}\r\n\r\n    {% for page_num in goal_list.iter_pages() %}\r\n        {% if page_num %}\r\n            {% if page_num != goal_list.page %}\r\n            <li class=\"page-item\">\r\n                <a class=\"page-link\" href=\"?page={{ page_num }}\" data-page=\"{{ page_num }}\">{{ page_num }}</a>\r\n            </li>\r\n            {% else %}\r\n            <li class=\"page-item active\" aria-current=\"page\">\r\n                <a class=\"page-link\" href=\"#\" aria-current=\"true\" >{{ page_num }}</a>\r\n            </li>\r\n            {% endif %}\r\n        {% else %}\r\n            <li class=\"disabled\">\r\n                <a class=\"page-link\" href=\"#\">...</a>\r\n            </li>\r\n        {% endif %}\r\n    {% endfor %}\r\n\r\n    {% if goal_list.has_next %}\r\n    <li class=\"page-item\">\r\n        <a class=\"page-link\" href=\"?page={{ goal_list.next_num }}\">다음</a>\r\n    </li>\r\n    {% else %}\r\n    <li class=\"page-item disable\">\r\n        <a class=\"page-link\" href=\"#\" aria-disabled=\"true\">다음</a>\r\n    </li>\r\n    {% endif %}\r\n</ul>','2023-09-14 09:14:47',3,NULL,'Development','python',4),(56,'html을 이용해서 웹 페이지에 이미지 나타내기&업로드하기','1. 이미지를 웹 페이지에 나타내기 위해서는 두 방법이 존재한다.\r\n(첫번째 방법)\r\n<img src=\"/static/image/사진1.jpeg\">\r\n정적 파일을 사용한다면 이 코드를 사용해도 된다. 상대 경로를 이용해서 이미지를 로드하는 코드이다.\r\n\r\n(두번째 방법)\r\n<img src = \"{{ url_for(\'static\', filename=\'/image/사진1.jpeg\') }}\">\r\n정적 파일을 사용하지 않는다면 이 코드를 사용하는 것이 좋다. 동적으로 관리할 수 있기 때문이다.\r\n\r\n2. 이미지를 업로드하기 위해서 아래와 같은 방법을 사용한다.\r\n우선 html에서 폼 태그를 이용해서 이미지의 파일 경로를 받아온다.\r\n<form method=post enctype=\"multipart/form-data\">\r\n    <input type=\"file\" name=\"profile_img\">\r\n</form>\r\n뷰 함수에서 해당 이미지 파일을 지정한 경로에 저장해준다.\r\nprofile_img = form.profile_img.data\r\nfilename = profile_img.filename\r\nprofile_img.save(os.path.join(\'Users/minseokkang/projects/myproject/pybo/static/image\', filename))\r\n\r\n이렇게 하면 내가 지정한 경로에 폼을 통해 전달한 파일이 저장된다.\r\n\r\n','2023-09-14 09:37:47',3,'2023-09-14 09:51:52','Development',NULL,1),(57,'데이터 조합 방지하기(조회수, 구독자 기능 구현을 위해서)','1. 복합 기본 키 이용하기\r\nDB의 column을 설정할 때 두개의 열 모두 primary_key=True로 설정하면 해당 두 열의 조합이 중복되면 integrity error가 발생한다.\r\nfrom_user_id=db.Column(db.Integer, primary_key=True)\r\nto_user_id=db.Column(db.Integer, primary_key=True)\r\n\r\n2. 쿼리에서 필터로 찾아내기(filter_by 메서드를 사용한다.)\r\nif request.method == \'POST\':\r\n    existing_subscription = Subscriber.query.filter_by(\r\n        from_user_id=from_user_id,\r\n        to_user_id=to_user_id\r\n    ).first()\r\n    if from_user_id == to_user_id:\r\n        flash(\'본인을 구독할 수 없습니다!\')\r\n    else:\r\n        #구독자 수 증가시키고, 테이블에 해당 조합 저장하기\r\n\r\n','2023-09-14 10:58:13',3,NULL,'Development',NULL,1),(62,'SMTP를 이용해서 이메일 보내기','import smtplib\r\nfrom email.message import EmailMessage\r\n\r\n# STMP 서버의 url과 port 번호\r\nSMTP_SERVER = \'smtp.gmail.com\'\r\nSMTP_PORT = 465\r\n\r\n# 1. SMTP 서버 연결\r\nsmtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)\r\n\r\nEMAIL_ADDR = \'m23235180@gmail.com\'\r\nEMAIL_PASSWORD = \'bpzwmnstpwrxmevk\'\r\n\r\n# 2. SMTP 서버에 로그인\r\nsmtp.login(EMAIL_ADDR, EMAIL_PASSWORD)\r\n\r\n# 3. MIME 형태의 이메일 메세지 작성\r\nmessage = EmailMessage()\r\nmessage.set_content(\'이메일 본문\')\r\nmessage[\"Subject\"] = \"이메일 제목\"\r\nmessage[\"From\"] = EMAIL_ADDR  #보내는 사람의 이메일 계정\r\nmessage[\"To\"] = \'dreampilot920@naver.com\'\r\n\r\n# 4. 서버로 메일 보내기\r\nsmtp.send_message(message)\r\n\r\n# 5. 메일을 보내면 서버와의 연결 끊기\r\nsmtp.quit()\r\n\r\n------------------------------------------------------------------------------------------------------------------------------------\r\n이 전에 수신하는 메일에 대한 계정의 설정을 바꿔주어야 한다.\r\n해당 계정 보안과 관련된 설정 변경에 대한 정보는 아래의 링크에서 확인하면 된다.\r\n내가 빼먹은 부분은 앱 비밀번호와 2단계 인증이었다. 그리고 포트 번호는 465이다.\r\nhttps://coding-kindergarten.tistory.com/204','2023-09-14 16:19:20',3,'2023-09-14 16:26:41','Development','123',1),(63,'with_entities() 와 load_only()의 차이점','두 메서드 모두 데이터 베이스에서의 특정 열에 대한 데이터를 가져온다는 점에서는 동일하다. \r\n먼저 입력을 할 때 with_entities는 모델 열 속성에 대한 참조가 필요하지만, load_only는 해당 column의 이름을 문자열로 입력하면 된다는 차이점이 있다.\r\n\r\n그리고, 질문에서 원치 않는 열을 제거할 때 load_only를 사용하면 여전히 객체 (모델 인스턴스)가 생성되지만 with_entities를 사용하면 선택한 열의 값이 포함된 튜플만 얻을 수 있다.','2023-09-15 09:17:41',3,NULL,'Development',NULL,1),(64,'1234','1234','2023-09-15 09:37:33',3,NULL,'Data Science','python',1),(65,'1234','1234','2023-09-15 09:37:51',3,NULL,'Data Science','c',1),(66,'1234','1234','2023-09-15 09:40:42',3,NULL,'Data Science','python',3),(67,'태그 중복으로 선택하기','태그를 중복으로 선택한다.','2023-09-15 10:08:27',3,NULL,'Data Science','python',1),(68,'1234','1234','2023-09-15 10:45:01',3,NULL,'Development','python',1),(69,'1234','1234','2023-09-15 10:45:15',3,NULL,'Data Science','com',1),(70,'ㅂㅈㄷㄱ','ㅂㅈㄷㄱ','2023-09-15 11:01:22',3,NULL,'Development','free',1),(71,'SQLite에서 MetaData클래스를 사용하여 규칙을 정의하기','PostgreSQL이나 MySQL등의 다른 데이터 베이스는 포함되지 않고 SQLite에게 해당하는 내용이다. \r\nSQLite 데이터베이스를 플라스크 ORM에서 정상으로 작동하기 위해서 하는 작업이다.\r\n\r\n1. 이 부분은 sqlite 데이터베이스의 제약조건을 정의하는 코드이다.\r\nfrom sqlalchemy import MetaData\r\n\r\nnaming_convention = {\r\n    \"ix\": \'ix_%(column_0_label)s\',\r\n    \"uq\": \"uq_%(table_name)s_%(column_0_name)s\",\r\n    \"ck\": \"ck_%(table_name)s_%(column_0_name)s\",\r\n    \"fk\": \"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s\",\r\n    \"pk\": \"pk_%(table_name)s\"\r\n}\r\ndb = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))\r\nmigrate = Migrate()\r\n\r\n2. SQLAlchemy를 사용하여 데이터베이스를 다루고 데이터베이스 마이그레이션을 관리할 때 사용하는 코드이다.\r\ndb.init_app(app)\r\nif app.config[\'SQLALCHEMY_DATABASE_URI\'].startswith(\"mysql\"):\r\n    migrate.init_app(app, db, render_as_batch=True)\r\nelse:\r\n    migrate.init_app(app, db)\r\nfrom . import models\r\n','2023-09-15 11:33:40',3,NULL,'Development','None',1),(72,'글을 작성하면 메일 보내기','이메일을 보내야 한다.','2023-09-15 14:56:00',3,NULL,'Development','None',0),(73,'SMTP를 이용해서 이메일을 보내는 코드 블럭입니다.','파이썬으로 이메일을 보내는 코드 블럭입니다. 필요한 경우 가져다 쓰면 됩니다.\r\n\r\nimport smtplib\r\nfrom email.message import EmailMessage\r\n\r\n# STMP 서버의 url과 port 번호\r\nSMTP_SERVER = \'smtp.gmail.com\'\r\nSMTP_PORT = 465\r\n\r\n# 1. SMTP 서버 연결\r\nsmtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)\r\n\r\nEMAIL_ADDR = \'m23235180@gmail.com\'\r\nEMAIL_PASSWORD = \'bpzwmnstpwrxmevk\'\r\n\r\n# 2. SMTP 서버에 로그인\r\nsmtp.login(EMAIL_ADDR, EMAIL_PASSWORD)\r\n\r\n# 3. MIME 형태의 이메일 메세지 작성\r\nmessage = EmailMessage()\r\nmessage.set_content(\'이메일 본문\')\r\nmessage[\"Subject\"] = \"이메일 제목\"\r\nmessage[\"From\"] = EMAIL_ADDR  #보내는 사람의 이메일 계정\r\nmessage[\"To\"] = \'dreampilot920@naver.com\'\r\n\r\n# 4. 서버로 메일 보내기\r\nsmtp.send_message(message)\r\n\r\n# 5. 메일을 보내면 서버와의 연결 끊기\r\nsmtp.quit()','2023-09-15 14:57:32',3,NULL,'Development','None',0),(74,'1234','124','2023-09-15 15:24:32',3,NULL,'Development','None',0),(75,'qw','asdf','2023-09-15 15:33:23',3,NULL,'Development','None',1),(76,'메일 보내기','1234','2023-09-15 15:37:49',3,NULL,'Relaxation','None',0),(77,'qwer','ewer','2023-09-15 15:42:53',3,NULL,'Development','None',0),(79,'sd','sd','2023-09-15 15:50:50',3,NULL,'Development','None',0),(80,'ㅂㅈㄷ','ㅂㅈㄷ','2023-09-15 15:52:38',3,NULL,'Development','None',1),(81,'1234','1234','2023-09-15 15:54:23',3,NULL,'Development','None',0),(82,'1234','1234','2023-09-15 15:55:32',3,NULL,'Computer Science','None',3),(83,'1243','ㅂㅈㄷㄱ','2023-09-15 15:57:24',3,NULL,'Development','None',1),(84,'1234','아이고 사장님','2023-09-15 16:02:08',3,NULL,'Artificial Intelligence','None',4),(85,'태그 1개 선택','태그를 한개 선택','2023-09-18 09:18:32',3,NULL,'Data Science','None',2),(86,'태그 2개 선택','2','2023-09-18 09:20:40',3,NULL,'Computer Science','None',1),(87,'123','1234','2023-09-18 09:30:05',3,NULL,'Data Science','python',1),(88,'123','1234','2023-09-18 09:31:41',3,NULL,'Data Science','free',1),(89,'1234','123','2023-09-18 09:33:04',3,NULL,'Data Science','123',1),(90,'123','12','2023-09-18 10:16:51',3,NULL,'Data Science','ㅁㄴ',1),(91,'태그 null','ewer','2023-09-18 14:06:02',3,NULL,'Data Science','ㅁㄴ',1),(92,'태그 5','태그 5','2023-09-19 09:56:54',3,NULL,'Data Science','태그5',3),(93,'중복된 태그','123','2023-09-19 10:11:31',3,NULL,'Data Science','123',10),(94,'1234','e','2023-09-21 13:57:01',3,NULL,'Data Science','123',1),(95,'1234','1234','2023-09-21 13:59:47',3,NULL,'Data Science','flask',1),(96,'이메일','이메일','2023-09-21 14:52:00',3,NULL,'Data Science','태그5',3),(97,'13','1234','2023-09-21 15:04:32',3,NULL,'Data Science','javascript',12),(98,'ㄴㅇ','ㅁㄴㅇㄹ','2023-09-21 15:07:00',3,NULL,'Development','github',1),(99,'qwe','ewer','2023-09-21 15:10:15',3,NULL,'Data Science','html',16),(100,'qwe','ewer','2023-09-21 15:10:16',3,NULL,'Data Science','html',28),(101,'qr','df','2023-09-21 15:13:26',3,NULL,'Development','태그5',0),(102,'ㅁㄴㅇㄹ','ㅁㄴㅇㄹ','2023-09-21 15:16:07',3,NULL,'Development','flask',0),(103,'sadf','ask','2023-09-21 15:18:56',3,NULL,'Development','flask',0),(104,'sadf','ask','2023-09-21 15:18:57',3,NULL,'Development','flask',0),(105,'asdf','asdf','2023-09-21 15:19:48',3,NULL,'Data Science','free',28),(106,'asf','ask','2023-09-21 15:23:06',3,NULL,'Development','javascript',0),(107,'asdf','adsfasdasdfadlfjlasdfasf\r\nasdfasdfas','2023-09-21 15:28:02',3,NULL,'Development','ㅁㄴ',0),(108,'as','asdfdfasdfasdfasf\r\nfasdfasf','2023-09-21 15:29:01',3,NULL,'Development','ai',0),(109,'as','asdfdfasdfasdfasf\r\nfasdfasf','2023-09-21 15:29:17',3,NULL,'Development','ai',0),(110,'asdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsa','2023-09-21 15:30:52',3,NULL,'Computer Science','None',0),(111,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadf','2023-09-21 15:31:49',3,NULL,'Computer Science','None',0),(112,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdf','2023-09-21 15:32:56',3,NULL,'Computer Science','None',0),(113,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdfad','2023-09-21 15:36:31',3,NULL,'Computer Science','None',7),(114,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdfad','2023-09-21 15:40:28',3,NULL,'Computer Science','None',3),(115,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdfad','2023-09-21 15:40:36',3,NULL,'Computer Science','None',3),(116,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdfadsdf','2023-09-21 15:41:47',3,NULL,'Computer Science','None',10),(117,'asdfdf','asdfasdfjhabkdtfcgyvhkbj\r\nasdfasjdlkklfhkjsadfasdfadsdf','2023-09-21 15:42:51',3,NULL,'Computer Science','None',26),(118,'sdf','asdf','2023-09-21 17:36:53',3,NULL,'Data Science','python',43),(119,'메일 미리보기 추기하기','메일 미리보기 기능을 추가해보자','2023-09-22 13:27:11',3,NULL,'Communication','html',6),(120,'sf','asdf            <a class=\"btn btn-primary\" href=\"{{ url_for(\'question.tagged_list\', tag=tag if tag else \'etc\',\r\n            category=category if category else \'default_category\') }}\" style=\"margin-top: 10px;\">{{ tag or \'etc\' }}</a>\r\n        {% endfor %}\r\n    </div>\r\n    <div class=\"row\" style=\"margin: 20px;\">\r\n        <div class=\"col-md-1\" style=\"display: flex; flex-direction: column; justify-content: center; align-items: center;\">\r\n            {% if question_list[num-1] %}\r\n                <a href=\"{{ url_for(\'question.ai_list\', num=num-1) }}\" class=\"btn btn-secondary\" style=\"font-size: 40px;\"><</a>\r\n            {% endif %}\r\n        </div>\r\n        <div class=\"col-md-10\">\r\n            <div class=\"container\" style=\"border: 1px solid #000; border-radius: 10px;\">\r\n\r\n                <div class=\"col-md-10\">\r\n                    <div class=\"row\" style=\"height: 10%; border-bottom: 1px solid #000;\">\r\n                        <div class=\"container\" style=\"font-size: 30px; margin-top: 10px;\">{{ question_list[num].subject }}</div>\r\n                    </div>\r\n                    <div class=\"row\">\r\n                        <pre class=\"container\" style=\"margin-top: 10px;\">{{ question_list[num].content }}</pre>\r\n                    </div>\r\n                </div>\r\n\r\n            </div>\r\n        </div>\r\n        <div class=\"col-md-1\" style=\"display: flex; flex-direction: column; justify-content: center; align-items: center;\">\r\n            {% if question_list[num+1] %}\r\n                <a href=\"{{ url_for(\'question.ai_list\', num=num+1) }}\" class=\"btn btn-secondary\" style=\"font-size:40px;\">></a>\r\n            {% endif %}','2023-09-22 14:25:29',3,NULL,'Artificial Intelligence','c',5),(121,'이메일에서 html 이스케이프','단순하게 escape함수를 적용시키면 되는가?\r\n','2023-09-25 15:18:02',3,NULL,'Data Science','html',2),(122,'이메일에서 html이스케이프','<div class=\"col-md-10\">\r\n    <div class=\"row\">\r\n        {% for tag in tag_list %}\r\n            <a class=\"btn btn-primary\" href=\"{{ url_for(\'question.tagged_list\', tag=tag if tag else \'etc\',\r\n            category=category if category else \'default_category\') }}\" style=\"margin-top: 10px;\">{{ tag or \'etc\' }}</a>\r\n        {% endfor %}\r\n    </div>\r\n    <div class=\"row\" style=\"margin: 20px;\">\r\n        <div class=\"col-md-1\" style=\"display: flex; flex-direction: column; justify-content: center; align-items: center;\">\r\n            {% if question_list[num-1] %}\r\n                <a href=\"{{ url_for(\'question.ai_list\', num=num-1) }}\" class=\"btn btn-secondary\" style=\"font-size: 40px;\"><</a>\r\n            {% endif %}\r\n        </div>\r\n        <div class=\"col-md-10\">\r\n            <div class=\"container\" style=\"border: 1px solid #000; border-radius: 10px;  max-height: 680px;\">\r\n                <div class=\"col-md-12\">\r\n                    <div class=\"row\" style=\"height: 10%;\">\r\n                        <div class=\"col\" style=\"height: 50px;\">\r\n                            <div class=\"container\" style=\"font-size: 30px; margin-top: 10px; height: 50px;\">{{ question_list[num].subject }}</div>\r\n                        </div>\r\n                        <div class=\"col-3\">\r\n                            <div class=\"card\" style=\"margin-top: 20px;\">{{ question_list[num].create_date|datetime }}</div>\r\n                        </div>\r\n                        <div class=\"col-2\">\r\n                            <div class=\"container\" style=\"margin-top: 20px;\">{{ question_list[num].user.username }}</div>\r\n                        </div>\r\n                    </div>\r\n                    <div class=\"row\">\r\n                        <pre class=\"container\" style=\"margin-top: 10px; border: 1px solid #000; max-height: 500px;\">{{ question_list[num].content }}</pre>\r\n                    </div>\r\n                    <div class=\"row\">\r\n                        <a href=\"#\" class=\"recommend btn btn-secondary\"\r\n                           data-uri=\"{{ url_for(\'vote.question\', question_id=question_list[num].id) }}\">👍 {{ question_list[num].voter|length }}</a>\r\n                        <a href=\"{{ url_for(\'question.detail\', question_id=question_list[num].id) }}\" class=\"btn btn-secondary\" style=\"margin-left: 10px;\">💬 {{ question_list[num].answer_set|length }}</a>\r\n                        <a href=\"#\" class=\"btn btn-secondary\" style=\"margin-left: 10px;\">👀 {{ question_list[num].views }}</a>\r\n                    </div>\r\n                </div>','2023-09-25 15:18:57',3,NULL,'Data Science','html',10),(123,'카테고리 ','ㅇㄹ','2023-09-26 11:22:38',3,NULL,'Relaxation','123',1),(124,'휴식','휴식은 우리의 신체와 마음에 중요한 역할을 합니다. 휴식이 없다면, 우리는 신체적, 정신적으로 과도한 스트레스와 피로를 경험할 수 있으며, 생산성과 전반적인 생활 만족도가 떨어질 수 있습니다. 휴식의 중요성은 다음과 같이 설명할 수 있습니다:\r\n\r\n1. 신체적 건강: 휴식은 신체의 회복과 재생을 돕습니다. 충분한 수면과 적절한 휴식을 통해 근육과 조직이 회복되며, 면역 체계가 강화됩니다. 만약 충분한 휴식을 취하지 않으면 만성적인 스트레스와 수면 부족으로 인한 건강 문제가 발생할 수 있습니다.\r\n\r\n2. 정신적 건강: 휴식은 스트레스 관리와 정신적 안녕을 지원합니다. 스트레스와 감정적인 압박이 계속되면, 우리의 정신적 건강에 해를 끼칠 수 있으며, 우울증과 불안 등의 문제가 발생할 수 있습니다. 휴식은 마음을 평안하게 하고 정서적인 안정을 제공합니다.\r\n\r\n3. 창의성과 생산성: 휴식은 창의성과 생산성을 촉진합니다. 쉬는 동안에는 아이디어가 떠오르고 문제를 해결하는 데 도움이 됩니다. 일정한 휴식을 취하면 업무 효율성이 증가하고 업무에 집중할 수 있게 됩니다.\r\n\r\n4. 인간관계: 휴식은 가족, 친구, 동료와의 인간관계에도 긍정적인 영향을 미칩니다. 휴식을 통해 스트레스와 긴장을 해소하고, 더 나은 소통과 대인관계를 유지할 수 있습니다.\r\n\r\n5. 창조성과 자기계발: 휴식은 취미 활동, 새로운 기술 습득, 책 읽기 등의 활동을 통해 자기계발을 지원합니다. 휴식 시간에 자기 계발 활동을 통해 새로운 관심사를 발견하고 개인적인 성장을 이룰 수 있습니다.\r\n\r\n요약하면, 휴식은 신체와 정신적 건강, 창의성, 생산성, 인간관계, 창조성, 자기계발 등 다양한 측면에서 중요한 역할을 합니다. 따라서 휴식을 소홀히하지 않고 일상 생활에 꾸준히 휴식을 통합하는 것이 중요합니다.','2023-09-26 11:37:58',3,NULL,'Relaxation','diary',1),(125,'새로운 질문 1234','ㅁㄴㅇㄹ','2023-09-26 12:07:47',3,NULL,'Communication','None',2),(126,'ㅁ','ㅁㄴㅇ','2023-09-26 15:13:12',3,NULL,'Communication','free',1),(127,'ㅁㄴㅇㄹ','ㅁㄴㅇ','2023-09-26 15:27:49',3,NULL,'Communication','github',2),(128,'휴식의 중요성','휴식은 중요합니다','2023-09-26 15:55:29',3,NULL,'Relaxation','com',3),(129,'computer science list 최대길이','computer science.\r\n최대 길이는 설정이 가능하다.\r\n줄이 여러개인 경우\r\n모두 표현하기','2023-10-10 15:09:26',3,NULL,'Computer Science','test',3),(130,'url에 앵커를 설정해서 html파일에서 특정 앵커의 위치로 이동해보기','{% extends \'base.html\' %}\r\n{% block content %}\r\n\r\n<head>\r\n    <style>\r\n        .col-md-3:hover {\r\n            cursor: pointer;\r\n            border: 3px solid #000;\r\n        }\r\n        .col-md-6:hover {\r\n            cursor: pointer;\r\n            border: 2px solid #000;\r\n        }\r\n        .col-md-3 {\r\n            height: 280px;\r\n            margin-right: 30px;\r\n            margin-bottom: 20px;\r\n            margin-left: 100px;\r\n            margin-top: 20px;\r\n            background-color: white;\r\n            border-radius: 10px;\r\n        }\r\n        .col-md-6 {\r\n            height: 280px;\r\n            margin-right: 30px;\r\n            margin-bottom: 20px;\r\n            margin-top: 20px;\r\n            background-color: white;\r\n            border-radius: 10px;\r\n        }\r\n    </style>\r\n</head>\r\n\r\n<div class=\"col-md-10\">\r\n    <div class=\"row\" style=\"height: 70px;\">\r\n        <div class=\"col-md-8\" style=\"margin: 10px;\">\r\n            <span style=\"font-size: 30px; color: white;\">Communication</span>\r\n        </div>\r\n        <div class=\"col-md-2\" style=\"margin-top:20px;\">\r\n            <a href=\"{{ url_for(\'question.create\') }}\" class=\"btn btn-light\">✏️ 질문 등록하기</a>\r\n        </div>\r\n    </div>\r\n    {% for tag in tag_list %}\r\n    <a class=\"btn\" href=\"{{ url_for(\'question.tagged_list\', tag=tag if tag else \'etc\',\r\n    category=category if category else \'default_category\') }}\" style=\"margin: 5px; background-color: #ed9542; color: white; font-family: monospace;\">{{ tag or \'etc\' }}</a>\r\n    {% endfor %}\r\n    <div class=\"row\">\r\n        {% for question in question_list %}\r\n            <div class=\"col-md-3 question-detail\" data-uri=\"http://127.0.0.1:5000/question/detail/{{ question.id }}/\">\r\n                <h4 style=\"overflow: hidden;\">{{ question.subject }}</h4>\r\n                <h5 style=\"text-align: right; border-bottom: 1px solid #000;\"><a href=\"{{ url_for(\'auth.user_info\',\r\n                user_id=question.user.id) }}\" style=\"color: black;\">✎{{ question.user.username }}</a></h5>\r\n                <h6 style=\"height: 160px;\">{{ question.content }}</h6>\r\n                <a href=\"#\" class=\"recommend btn btn-secondary\"\r\n                   data-uri=\"{{ url_for(\'vote.question\', question_id=question.id) }}\">👍 {{ question.voter|length }}</a>\r\n                <a href=\"{{ url_for(\'question.detail\', question_id=question.id) }}\" class=\"btn btn-secondary\">💬 {{ question.answer_set|length }}</a>\r\n                <a href=\"#\" class=\"btn btn-secondary\">👀 {{ question.views }}</a>\r\n            </div>\r\n            <div class=\"col-md-6 answer-detail\" data-uri=\"http://127.0.0.1:5000/question/detail/{{ question.id }}/#watch_detail/\"\r\n                 style=\"overflow: auto;\">\r\n                <h4 style=\"border-bottom: 1px solid #000;\">💬 Comments</h4>\r\n                {% if question.answer_set %}\r\n                {% for answer in question.answer_set %}\r\n                    <div class=\"row answer-detail\" style=\"margin: 5px; margin-bottom: 10px;\">\r\n                        <h6 style=\"margin-right: 5px; max-width: 100px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;\">{{ answer.content }}</h6>\r\n                        <h6> | {{ answer.user.username }} </h6>\r\n                        <h6> | {{ answer.create_date|datetime }}</h6>\r\n                    </div>\r\n                {% endfor %}\r\n                {% else %}\r\n                    <h6 style=\"color: grey;\">답변이 없습니다.</h6>\r\n                {% endif %}\r\n            </div>\r\n        {% endfor %}\r\n    </div>\r\n</div>\r\n\r\n<script>\r\n    document.addEventListener(\'DOMContentLoaded\', function() {\r\n        var questionDetails = document.querySelectorAll(\'.question-detail\');\r\n\r\n        questionDetails.forEach(function(question) {\r\n            question.addEventListener(\"click\", function() {\r\n                var uri = question.getAttribute(\'data-uri\');\r\n                if (uri) {\r\n                    window.location.href = uri;\r\n                }\r\n            });\r\n        });\r\n        var answerDetails = document.querySelectorAll(\'.answer-detail\');\r\n\r\n        answerDetails.forEach(function(answer) {\r\n            answer.addEventListener(\"click\", function() {\r\n                var uri = answer.getAttribute(\'data-uri\');\r\n                if (uri) {\r\n                    window.location.href = uri;\r\n                }\r\n            });\r\n        });\r\n    });\r\n</script>\r\n<script>\r\n    $(document).ready(function(){\r\n    $(\".recommend\").on(\'click\', function() {\r\n        if(confirm(\"정말로 추천하시겠습니까?\")) {\r\n            location.href = $(this).data(\'uri\');\r\n        }\r\n    });\r\n</script>\r\n{% endblock %}\r\n\r\n','2023-10-11 10:05:43',3,NULL,'Communication','test',2),(131,'none질문등록','ㅠㅠ','2023-10-11 14:22:15',3,NULL,'Development','None',3),(132,'새로운 카테고리 테스트','새로운 카테고리 1에 대한 첫 글입니다\r\n','2023-10-17 17:26:16',15,NULL,'Communication','test',3),(133,'글을 작성했을 때 smtp에러가 발생한다.','smtp에러가 발생','2023-10-18 09:20:15',16,NULL,'Development','test',1),(134,'글을 작성했을 때 smtp에러 발생','구독자가 없는 경우 해당 오류가 발생하는 것인가\r\n','2023-10-18 09:23:16',3,NULL,'Development','test',1),(135,'smtp 에러가 발생했던 이유','smtp 에러가 발생했던 이유는 메일을 발송할 대상자가 없어서이다.','2023-10-18 09:28:40',3,NULL,'Development','test',1),(136,'smtp 에러 ','구독자가 없는 계정으로 하는 경우에 에러가 생기지 않아야 한다.','2023-10-18 09:29:55',16,NULL,'Development','test',2),(137,'not a valid choice 에러 해결하기','에러가 발생한다.','2023-10-18 09:59:34',3,NULL,'Development','test',0),(138,'새로운 태그 선택하면 오류발생','새로운 태그 선택하면 오류가 발생한다.','2023-10-18 13:17:01',3,NULL,'Statistic','ㅁㄴ',1),(139,'카테고리 추가 테스트','테스트','2023-10-18 13:21:15',3,NULL,'Statistic','test',2),(141,'카테고리 폼을 텍스트형식으로 변경','테스트','2023-10-19 11:31:54',3,NULL,'Development','test',4),(142,'Question의 카테고리 폼을 TextAreaField로 변경','테스트','2023-10-19 11:33:38',3,NULL,'새로운 카테고리 1','test',3),(143,'새로운 카테고리 1에 대한 글','새로운 카테고리','2023-10-20 13:34:43',3,NULL,'새로운 카테고리1','test',2),(144,'새로운 카테고리2에 대한 글','동적으로 새로운 카테고리에 대한 글을 볼 수 있게끔 한다.','2023-10-20 16:49:59',3,NULL,'새로운 카테고리2','test',3),(145,'소스코드','```\r\ndef add(a, b):\r\n     return a+b\r\n```','2023-10-25 16:03:22',3,NULL,'Development','test',3),(146,'카카오톡 메시지 API를 사용해서 카카오톡 공유하기 기능 추가하기','1. 카카오 공유하기 기능을 사용하기 위한 자바스크립트 코드\r\n<script type=\"text/javascript\">\r\n  // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.\r\n  Kakao.init(\'애플리케이션의 자바스크립트 앱 키\');\r\n\r\n  // SDK 초기화 여부를 판단합니다.\r\n  console.log(Kakao.isInitialized());\r\n\r\n  function kakaoShare() {\r\n    Kakao.Link.sendDefault({\r\n      objectType: \'feed\',\r\n      content: {\r\n        title: \'카카오공유하기 시 타이틀\',\r\n        description: \'카카오공유하기 시 설명\',\r\n        imageUrl: \'카카오공유하기 시 썸네일 이미지 경로\',\r\n        link: {\r\n          mobileWebUrl: \'http://minseok.com\',\r\n          webUrl: \'http://minseok.com\',\r\n        },\r\n      },\r\n      buttons: [\r\n        {\r\n          title: \'웹으로 보기\',\r\n          link: {\r\n            mobileWebUrl: \'http://minseok.com\',\r\n            webUrl: \'http://minseok.com\',\r\n          },\r\n        },\r\n      ],\r\n      // 카카오톡 미설치 시 카카오톡 설치 경로이동\r\n      installTalk: true,\r\n    })\r\n  }\r\n</script>\r\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\r\n\r\n2. 공유하기를 실행하기 위한 아이콘 만들기\r\n<a id=\"kakao-link-btn\" href=\"javascript:kakaoShare()\">\r\n     <img src=\"https://developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_medium.png\"  style=\"height: 40px;\"/>\r\n</a>\r\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\r\n\r\n3. 카카오 SDK호출하기\r\n<script src=\"https://developers.kakao.com/sdk/js/kakao.js\"></script>\r\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\r\n\r\n이와 같이 세가지만 완료해준다면 해당 아이콘을 누르면 카카오톡 공유하기 기능을 사용할 수 있다.','2023-10-26 14:06:56',15,NULL,'Development','javascript',3),(147,'카카오 계정으로 글 작성','글 작성해봅니다','2023-11-01 16:13:47',31,NULL,'Development','test',3);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_voter`
--

DROP TABLE IF EXISTS `question_voter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_voter` (
  `user_id` int NOT NULL,
  `question_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`question_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `question_voter_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `question_voter_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_voter`
--

LOCK TABLES `question_voter` WRITE;
/*!40000 ALTER TABLE `question_voter` DISABLE KEYS */;
INSERT INTO `question_voter` VALUES (3,9),(3,13),(3,16),(3,24),(3,26),(3,33),(3,34),(3,35),(13,122),(31,122),(21,131),(3,132),(3,136),(13,136),(13,141),(14,141),(13,142),(14,142),(3,146),(3,147);
/*!40000 ALTER TABLE `question_voter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistic`
--

DROP TABLE IF EXISTS `statistic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `labels` text NOT NULL,
  `data_value` text NOT NULL,
  `stepsize` int DEFAULT NULL,
  `border_color` varchar(10) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `background_color` varchar(20) DEFAULT NULL,
  `border_width` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistic`
--

LOCK TABLES `statistic` WRITE;
/*!40000 ALTER TABLE `statistic` DISABLE KEYS */;
INSERT INTO `statistic` VALUES (1,'그래프','[1,2,3,4,5]','[18, 20, 21, 16, 17]',2,'green','line','blue',1),(2,'제목','[\"월\", \"화\", \"수\", \"목\", \"금\"]','[12,21,14,31,11]',NULL,'blue','line','green',2),(3,'overflow','[1,2,3,4,5,6,7,8,9,10]','[1,2,3,4,1,2,3,4,1,2]',NULL,'green','line','red',1),(4,'re','[\'월\', \'화\', \'수\', \'목\', \'금\', \'토\', \'일\']','[1, 1, 2, 1, 2, 3, 2]',NULL,'green','line','blue',1),(5,'d','[1,2,3]','[3,4,5]',NULL,'white','line','gray',NULL),(6,'123','[\"월\", \"화\", \"수\"]','[1,4,7]',NULL,'blue','line','blue',1),(7,'제목1','[\"월\", \"화\", \"수\", \"목\", \"금\", \"토\", \"일\"]','[1,4,3,6,3,6,9]',NULL,'gray','line','black',1);
/*!40000 ALTER TABLE `statistic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscriber`
--

DROP TABLE IF EXISTS `subscriber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscriber` (
  `from_user_id` int NOT NULL,
  `to_user_id` int NOT NULL,
  PRIMARY KEY (`from_user_id`,`to_user_id`),
  KEY `to_user_id` (`to_user_id`),
  CONSTRAINT `subscriber_ibfk_1` FOREIGN KEY (`from_user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `subscriber_ibfk_2` FOREIGN KEY (`to_user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscriber`
--

LOCK TABLES `subscriber` WRITE;
/*!40000 ALTER TABLE `subscriber` DISABLE KEYS */;
INSERT INTO `subscriber` VALUES (3,1),(3,2),(1,3),(2,3),(5,3),(7,3),(3,5),(3,6),(3,9),(3,16);
/*!40000 ALTER TABLE `subscriber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(120) NOT NULL,
  `profile_img` varchar(200) DEFAULT 'minsoek.png',
  `subscribe_num` int DEFAULT '0',
  `score` int DEFAULT '0',
  `kakao` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'minseok','pbkdf2:sha256:600000$zw3xk0ELgX4xpoGr$60870771aa10339cf73a28ef8141aa6c3f0ddde4ef3e9155afff35ad9cafde0a','dreampilot920@naver.com','minsoek.png',0,0,0),(2,'minseok1','pbkdf2:sha256:600000$aEY5Uon72TDbCiaV$253d0181345c8fe655c9a2ad33f1907f520119c4c65b1722646d89111fc3cfb9','dresadfkjn@naver.com','minsoek.png',0,9,0),(3,'강민석','pbkdf2:sha256:600000$iywgjvCClxnjK1l8$3f92c56a39e3b13525c3a60d967293227e89f6424676f480ab37cd7b198d2762','minseok@naver.com','minsoek.png',0,7,0),(4,'강민석2','pbkdf2:sha256:600000$yCfjuKoLz6K2dqZE$916b56586a50ad19df31a3d107a6c93c17843b0d33d7effe6480a18ae45b6d48','anasdfla@naver.com','minsoek.png',0,0,0),(5,'강민석3','pbkdf2:sha256:600000$ASBooWIn6wyLXMRb$2303a7751f323a312843257aa271fb50a74de176bc3ff44faff0085ab35cfa1a','dasfaskj@naver.com','minsoek.png',0,0,0),(6,'123','pbkdf2:sha256:600000$z5ZsVo72oXCoF4Gf$cd2e2f983be8bfae18745008d865a98a5f0beb8e3ffc459d14fa66ecb39060df','sdffd@naver.com','minsoek.png',0,0,0),(7,'1234','pbkdf2:sha256:600000$7SGULQQUJKgSqA7x$3bd6d6328a9e69748624ab2d00241b70304e89e89c008e0c0d7740b6a1ce5157','dsdfsaf@naver.co','minsoek.png',0,0,0),(8,'12345','pbkdf2:sha256:600000$rbz5E9vHqohm8cP5$f51e2bfd501b4d6630482463d24be93486b1c7cc63026a0f798c11bed8ee0981','asdf@naver.com','minsoek.png',0,0,0),(9,'강민석7','pbkdf2:sha256:600000$XZRTWyfyGpZt72fw$ed82b47daa6fae69c9f54839cc09e18f7d45071ab48f8614e8c8158617743bdb','1234@naver.com','사진1.jpeg',0,0,0),(13,'민석2','pbkdf2:sha256:600000$RvItRwTQA9pXdAyY$a03ccd7e79acaa7dd12abb1cc3a9be53b9002fc682e21489952a87a30d39b345','minseok2@naver.com','github.png',0,0,0),(14,'민석3','pbkdf2:sha256:600000$3kbt5AyAwtkD7hCg$f61cb657750c3c8070fc83b013d4b55425634cfd4fa40147da1d0da9e08cd511','mmmmm@naver.com','ai.png',0,0,0),(15,'민석4','pbkdf2:sha256:600000$ywKTEzFW7ZiPD64T$c25cd654222a11199ac71d385aecdd83956be6420ad1fa2f852ccb115ee448e1','msms@gmail.com','minsoek.png',0,2,0),(16,'민석5','pbkdf2:sha256:600000$SPt4aedl4SjfRRuD$f77c19f7f8f0ed1e69f91ab17eb82eac1959e78b2ecec78de076f493ca7e5c58','minmin@gmail.com','minsoek.png',1,2,0),(17,'민석6','pbkdf2:sha256:600000$o1pJ5tOkGuE2xSGn$217b3b4172c0bcc0d07e909856807bb764e40d30259e1b5a5325c46e4e9ced75','minminseok@naver.com','datascience_bg.jpeg',0,0,0),(18,'민석7','pbkdf2:sha256:600000$wW07x055pk2UeDJA$71630422a8b4c5bae195498733845c4ef8b8e922e3d8c583db5a8c85caddb109','qwer@naver.com','github.png',0,0,0),(20,'민석8','pbkdf2:sha256:600000$mtJLZKOEhaWipffD$19deb3faa2e2ed635360401f56870d0c681023b7577b3eede00facfb6b2a11ab','asdfasdf@naver.com','github.png',0,0,0),(21,'강민석01','pbkdf2:sha256:600000$LktR2hYEYFTPh0LI$c0381fe16f8538ea6fb9ebff9cb763da809133e5e18d15fead8c56d0082446d3','nnnjjjj@gmail.com','minsoek.png',0,0,0),(22,'민석 03','pbkdf2:sha256:600000$c0DQQpx0l16zQJRj$9a55822cb625c84ff9723176a6e62a1be9c0a9c3c244ae332307ef33f1074991','mjmj123@gmail.com','minsoek.png',0,0,0),(23,'민석06','pbkdf2:sha256:600000$yLH8UkRgYFZzgyex$0a6406fab8b35fdce7416a9a342c6ef0e0dd111291087526d2ed1e4c328ecafd','minmin09@naver.com','minsoek.png',0,0,0),(24,'민석07','pbkdf2:sha256:600000$SlMrhs26OR6nGFh5$4e2b1372cded0e913a75faeee2752a59bfc87a25d40595b4a040e2ba2953c822','mdmd@naver.com','ai.png',0,0,0),(25,'testmin','1','asdasdfasdfasfd@naver.com','sdf',0,0,0),(31,'러브파이','None','ssook0211@naver.com','http://k.kakaocdn.net/dn/ckEu13/btrFFjNxGf9/kzDlkmFmQKAsQ4oFgPWMMK/img_640x640.jpg',0,1,1),(35,'Andrea','None','m23235180@gmail.com','http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg',0,0,1),(37,'테스트 민석','None','dreampilot0103@gmail.com','http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg',0,0,1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-08 15:40:12
