-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2023 at 06:59 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `log_book`
--

-- --------------------------------------------------------

--
-- Table structure for table `log_book`
--

CREATE TABLE `log_book` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `variable_type` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1-active 0-inactive',
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log_book`
--

INSERT INTO `log_book` (`id`, `name`, `variable_type`, `user_id`, `status`, `created_date`) VALUES
(15, 'Anil Book (String)', 'string', 1, 1, '2023-06-03 11:42:51'),
(16, 'Sunil Book1', 'type1', 2, 1, '2023-06-03 11:44:23'),
(17, 'Sunil Book2', 'type2', 2, 1, '2023-06-03 11:44:36'),
(19, 'Anil Mohite (Double)', 'double', 1, 1, '2023-06-03 14:44:43'),
(20, 'ANIL MOHITE', 'type2', 3, 1, '2023-06-03 14:44:43'),
(21, 'ANIL MOHITE (Integer)', 'int', 1, 1, '2023-06-03 14:48:09'),
(22, 'ANIL MOHITE', 'string', 1, 1, '2023-06-03 15:35:57');

-- --------------------------------------------------------

--
-- Table structure for table `log_entry`
--

CREATE TABLE `log_entry` (
  `id` int(11) NOT NULL,
  `logbook_id` int(11) NOT NULL,
  `log_value` text NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1-active 0-inactive',
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log_entry`
--

INSERT INTO `log_entry` (`id`, `logbook_id`, `log_value`, `status`, `created_date`) VALUES
(19, 15, 'bk2 ent1', 1, '2023-06-03 11:43:19'),
(20, 15, 'bk2 ent2', 1, '2023-06-03 11:43:26'),
(21, 17, 'sunil bk2 ent2 ', 1, '2023-06-03 11:44:48'),
(22, 16, 'sunil bk1 ent1', 1, '2023-06-03 11:45:10'),
(38, 21, '123', 1, '2023-06-03 15:03:19'),
(39, 21, '234', 1, '2023-06-03 15:03:19'),
(40, 19, '12123', 1, '2023-06-03 15:03:19'),
(41, 19, '123.123', 1, '2023-06-03 15:03:19'),
(42, 15, '123', 1, '2023-06-03 15:03:19'),
(43, 15, 'sdfadf', 1, '2023-06-03 15:03:19'),
(44, 19, '123', 1, '2023-06-03 15:17:03'),
(45, 19, '123', 1, '2023-06-03 15:17:45'),
(46, 21, '2', 1, '2023-06-03 15:19:12'),
(47, 19, '101', 1, '2023-06-03 15:19:12'),
(48, 19, '101', 1, '2023-06-03 15:19:12'),
(49, 19, '101.01', 1, '2023-06-03 15:19:12'),
(50, 19, '123', 1, '2023-06-03 15:19:12'),
(51, 19, '123.45', 1, '2023-06-03 15:19:12'),
(52, 19, '123', 1, '2023-06-03 15:19:12'),
(53, 21, '12', 1, '2023-06-03 15:19:12'),
(55, 15, 'test', 1, '2023-06-05 04:57:51');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `status` tinyint(1) DEFAULT 1 COMMENT '1-active 0-inactive',
  `created_date` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `status`, `created_date`) VALUES
(1, 'Anil Mohite', 'mohiteanil22@gmail.com', 'pbkdf2:sha256:600000$nHmF9h0u0NmUjiMo$0f276f0847ad83a5403cd15755601490c70fd4e69e690cf6f62f87736fffea13', 1, '2023-06-02 13:44:26'),
(2, 'Sunil Mohite', 'sunil@gmail.com', 'pbkdf2:sha256:600000$29GBgS3LyyphwYSn$18e2b1ad6ababda28680653f6221f36f6d301b568f1a31274d638992a4e6193d', 1, '2023-06-03 05:31:09'),
(3, 'Sai Mohite', 'sai@gmail.com', 'pbkdf2:sha256:600000$yC0T2Lnu24rqSkqz$fc0248264509db92cab93ea22ce48e79a164ada9c17db8936bc05776a8004dd8', 1, '2023-06-03 14:44:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log_book`
--
ALTER TABLE `log_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log_entry`
--
ALTER TABLE `log_entry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `logbook_id` (`logbook_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log_book`
--
ALTER TABLE `log_book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `log_entry`
--
ALTER TABLE `log_entry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
