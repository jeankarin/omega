-- MySQL dump 10.19  Distrib 10.3.32-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: 192.168.1.136    Database: EUROMILLON_DB
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB-1:10.6.5+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary table structure for view `EXCELCONS`
--

DROP TABLE IF EXISTS `EXCELCONS`;
/*!50001 DROP VIEW IF EXISTS `EXCELCONS`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `EXCELCONS` (
  `NUM01` tinyint NOT NULL,
  `NUM02` tinyint NOT NULL,
  `NUM03` tinyint NOT NULL,
  `NUM04` tinyint NOT NULL,
  `NUM05` tinyint NOT NULL,
  `STAR01` tinyint NOT NULL,
  `STAR02` tinyint NOT NULL,
  `DIASEM` tinyint NOT NULL,
  `DIA` tinyint NOT NULL,
  `MES` tinyint NOT NULL,
  `ANYO` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `MILLONES`
--

DROP TABLE IF EXISTS `MILLONES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MILLONES` (
  `ID_MILL` int(11) NOT NULL AUTO_INCREMENT,
  `MILLON` varchar(10) COLLATE utf8mb3_spanish_ci NOT NULL,
  `ID_SORTEO` int(11) NOT NULL,
  PRIMARY KEY (`ID_MILL`)
) ENGINE=InnoDB AUTO_INCREMENT=420 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `NUMEROS`
--

DROP TABLE IF EXISTS `NUMEROS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NUMEROS` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NUM01` int(11) NOT NULL,
  `NUM02` int(11) NOT NULL,
  `NUM03` int(11) NOT NULL,
  `NUM04` int(11) NOT NULL,
  `NUM05` int(11) NOT NULL,
  `STAR01` int(11) NOT NULL,
  `STAR02` int(11) NOT NULL,
  `DIASEM` varchar(8) COLLATE utf8mb3_spanish_ci NOT NULL,
  `DIA` int(11) NOT NULL,
  `MES` varchar(45) COLLATE utf8mb3_spanish_ci NOT NULL,
  `ANYO` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1491 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `SORTEOS2020`
--

DROP TABLE IF EXISTS `SORTEOS2020`;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2020`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `SORTEOS2020` (
  `ID` tinyint NOT NULL,
  `NUM01` tinyint NOT NULL,
  `NUM02` tinyint NOT NULL,
  `NUM03` tinyint NOT NULL,
  `NUM04` tinyint NOT NULL,
  `NUM05` tinyint NOT NULL,
  `STAR01` tinyint NOT NULL,
  `STAR02` tinyint NOT NULL,
  `DIASEM` tinyint NOT NULL,
  `DIA` tinyint NOT NULL,
  `MES` tinyint NOT NULL,
  `ANYO` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `SORTEOS2021`
--

DROP TABLE IF EXISTS `SORTEOS2021`;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2021`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `SORTEOS2021` (
  `ID` tinyint NOT NULL,
  `NUM01` tinyint NOT NULL,
  `NUM02` tinyint NOT NULL,
  `NUM03` tinyint NOT NULL,
  `NUM04` tinyint NOT NULL,
  `NUM05` tinyint NOT NULL,
  `STAR01` tinyint NOT NULL,
  `STAR02` tinyint NOT NULL,
  `DIASEM` tinyint NOT NULL,
  `DIA` tinyint NOT NULL,
  `MES` tinyint NOT NULL,
  `ANYO` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `SORTEOS2022`
--

DROP TABLE IF EXISTS `SORTEOS2022`;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2022`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `SORTEOS2022` (
  `ID` tinyint NOT NULL,
  `NUM01` tinyint NOT NULL,
  `NUM02` tinyint NOT NULL,
  `NUM03` tinyint NOT NULL,
  `NUM04` tinyint NOT NULL,
  `NUM05` tinyint NOT NULL,
  `STAR01` tinyint NOT NULL,
  `STAR02` tinyint NOT NULL,
  `DIASEM` tinyint NOT NULL,
  `DIA` tinyint NOT NULL,
  `MES` tinyint NOT NULL,
  `ANYO` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `dataframe`
--

DROP TABLE IF EXISTS `dataframe`;
/*!50001 DROP VIEW IF EXISTS `dataframe`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `dataframe` (
  `NUM01` tinyint NOT NULL,
  `NUM02` tinyint NOT NULL,
  `NUM03` tinyint NOT NULL,
  `NUM04` tinyint NOT NULL,
  `NUM05` tinyint NOT NULL,
  `STAR01` tinyint NOT NULL,
  `STAR02` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `EXCELCONS`
--

/*!50001 DROP TABLE IF EXISTS `EXCELCONS`*/;
/*!50001 DROP VIEW IF EXISTS `EXCELCONS`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`euromillon_user`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `EXCELCONS` AS select `NUMEROS`.`NUM01` AS `NUM01`,`NUMEROS`.`NUM02` AS `NUM02`,`NUMEROS`.`NUM03` AS `NUM03`,`NUMEROS`.`NUM04` AS `NUM04`,`NUMEROS`.`NUM05` AS `NUM05`,`NUMEROS`.`STAR01` AS `STAR01`,`NUMEROS`.`STAR02` AS `STAR02`,`NUMEROS`.`DIASEM` AS `DIASEM`,`NUMEROS`.`DIA` AS `DIA`,`NUMEROS`.`MES` AS `MES`,`NUMEROS`.`ANYO` AS `ANYO` from `NUMEROS` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `SORTEOS2020`
--

/*!50001 DROP TABLE IF EXISTS `SORTEOS2020`*/;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2020`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `SORTEOS2020` AS select `NUMEROS`.`ID` AS `ID`,`NUMEROS`.`NUM01` AS `NUM01`,`NUMEROS`.`NUM02` AS `NUM02`,`NUMEROS`.`NUM03` AS `NUM03`,`NUMEROS`.`NUM04` AS `NUM04`,`NUMEROS`.`NUM05` AS `NUM05`,`NUMEROS`.`STAR01` AS `STAR01`,`NUMEROS`.`STAR02` AS `STAR02`,`NUMEROS`.`DIASEM` AS `DIASEM`,`NUMEROS`.`DIA` AS `DIA`,`NUMEROS`.`MES` AS `MES`,`NUMEROS`.`ANYO` AS `ANYO` from `NUMEROS` where `NUMEROS`.`ANYO` = 2020 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `SORTEOS2021`
--

/*!50001 DROP TABLE IF EXISTS `SORTEOS2021`*/;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2021`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `SORTEOS2021` AS select `NUMEROS`.`ID` AS `ID`,`NUMEROS`.`NUM01` AS `NUM01`,`NUMEROS`.`NUM02` AS `NUM02`,`NUMEROS`.`NUM03` AS `NUM03`,`NUMEROS`.`NUM04` AS `NUM04`,`NUMEROS`.`NUM05` AS `NUM05`,`NUMEROS`.`STAR01` AS `STAR01`,`NUMEROS`.`STAR02` AS `STAR02`,`NUMEROS`.`DIASEM` AS `DIASEM`,`NUMEROS`.`DIA` AS `DIA`,`NUMEROS`.`MES` AS `MES`,`NUMEROS`.`ANYO` AS `ANYO` from `NUMEROS` where `NUMEROS`.`ANYO` = 2021 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `SORTEOS2022`
--

/*!50001 DROP TABLE IF EXISTS `SORTEOS2022`*/;
/*!50001 DROP VIEW IF EXISTS `SORTEOS2022`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`euromillon_user`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `SORTEOS2022` AS select `NUMEROS`.`ID` AS `ID`,`NUMEROS`.`NUM01` AS `NUM01`,`NUMEROS`.`NUM02` AS `NUM02`,`NUMEROS`.`NUM03` AS `NUM03`,`NUMEROS`.`NUM04` AS `NUM04`,`NUMEROS`.`NUM05` AS `NUM05`,`NUMEROS`.`STAR01` AS `STAR01`,`NUMEROS`.`STAR02` AS `STAR02`,`NUMEROS`.`DIASEM` AS `DIASEM`,`NUMEROS`.`DIA` AS `DIA`,`NUMEROS`.`MES` AS `MES`,`NUMEROS`.`ANYO` AS `ANYO` from `NUMEROS` where `NUMEROS`.`ANYO` = 2022 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dataframe`
--

/*!50001 DROP TABLE IF EXISTS `dataframe`*/;
/*!50001 DROP VIEW IF EXISTS `dataframe`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`euromillon_user`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `dataframe` AS select `NUMEROS`.`NUM01` AS `NUM01`,`NUMEROS`.`NUM02` AS `NUM02`,`NUMEROS`.`NUM03` AS `NUM03`,`NUMEROS`.`NUM04` AS `NUM04`,`NUMEROS`.`NUM05` AS `NUM05`,`NUMEROS`.`STAR01` AS `STAR01`,`NUMEROS`.`STAR02` AS `STAR02` from `NUMEROS` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-02 16:54:32
