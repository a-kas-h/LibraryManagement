-- phpMyAdmin SQL Dump
-- version 4.4.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2021 at 02:17 PM
-- Server version: 5.6.25
-- PHP Version: 5.6.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookissuedetails`
--

CREATE TABLE IF NOT EXISTS `bookissuedetails` (
  `id` int(11) NOT NULL,
  `bookissueid` varchar(30) NOT NULL,
  `bookmasterid` varchar(30) NOT NULL,
  `issueuptodate` date NOT NULL,
  `returnstatus` int(11) NOT NULL DEFAULT '0',
  `returndate` date NOT NULL DEFAULT '0000-00-00',
  `fineamt` int(11) NOT NULL DEFAULT '0',
  `status` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookissuedetails`
--

INSERT INTO `bookissuedetails` (`id`, `bookissueid`, `bookmasterid`, `issueuptodate`, `returnstatus`, `returndate`, `fineamt`, `status`) VALUES
(21, 'neha sharma', 'english', '2021-08-22', 1, '2021-08-25', 600, 1),
(22, 'ayush', 'science', '2021-08-01', 1, '2021-08-04', 1500, 1),
(23, 'ayush', 'english', '2021-08-01', 1, '2021-08-03', 400, 1),
(24, 'neha sharma', 's science', '2021-08-22', 1, '2021-08-23', 300, 1),
(25, 'akash', 'english', '2021-08-31', 1, '2021-09-01', 200, 1),
(26, 'kshitiz', 'english', '2021-08-22', 1, '2021-08-24', 400, 1),
(27, 'kshitiz', 'science', '2021-08-23', 1, '2021-08-24', 500, 1),
(28, 'ayush', 'science', '2021-08-08', 1, '2021-08-09', 500, 1);

-- --------------------------------------------------------

--
-- Table structure for table `bookissuemaster`
--

CREATE TABLE IF NOT EXISTS `bookissuemaster` (
  `id` int(11) NOT NULL,
  `smid` varchar(30) NOT NULL,
  `totalnobook` int(30) NOT NULL,
  `datetime` date NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookissuemaster`
--

INSERT INTO `bookissuemaster` (`id`, `smid`, `totalnobook`, `datetime`, `status`) VALUES
(43, 'akash', 1, '2021-07-30', 1),
(44, 'neha sharma', 1, '2021-08-01', 1),
(45, 'ayush', 2, '2021-08-01', 1),
(46, 'neha sharma', 1, '2021-08-02', 1),
(47, 'akash', 1, '2021-08-02', 1),
(48, 'kshitiz', 2, '2021-08-02', 1),
(49, 'kshitiz', 2, '2021-08-02', 1),
(50, 'kshitiz', 2, '2021-08-02', 1),
(51, 'ayush', 1, '2021-08-02', 1);

-- --------------------------------------------------------

--
-- Table structure for table `bookissuetemp`
--

CREATE TABLE IF NOT EXISTS `bookissuetemp` (
  `id` int(11) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `issueuptodate` date NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bookmaster`
--

CREATE TABLE IF NOT EXISTS `bookmaster` (
  `id` int(11) NOT NULL,
  `bookname` varchar(30) NOT NULL,
  `publication` varchar(30) NOT NULL,
  `serialno` int(30) NOT NULL,
  `edition` varchar(30) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `fineamt` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookmaster`
--

INSERT INTO `bookmaster` (`id`, `bookname`, `publication`, `serialno`, `edition`, `status`, `fineamt`) VALUES
(1, 'maths', 'ncrt', 4566, '2nd edition', 1, 500),
(2, 'science', 'ncrt', 7964, '3rd edition', 1, 500),
(4, 'english', 'ncrt', 568884, '3rd edition', 1, 200),
(5, 's science', 'ncrt', 8979456, '3rd edition', 1, 300);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `rollno` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `mname` varchar(30) NOT NULL,
  `mobileno` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `rollno`, `fname`, `mname`, `mobileno`, `email`, `age`, `status`) VALUES
(1, 'akash', 1522874, 'ashutosh choubey', 'vina choubey', '8210016301', 'akash@gmail.com', 20, 1),
(2, 'ayush', 1342606, 'ss jha', '''''''''''', '7782947802', 'ayush@gmail.com', 25, 1),
(3, 'neha sharma', 190015, 'sivender sharma', 'sangeeta shrama', '8645785689', 'neha@gmail.com', 19, 1),
(4, 'kshitiz', 781115, 'papa', 'ma', '8987545645', 'kshitz@gmail.com', 22, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookissuedetails`
--
ALTER TABLE `bookissuedetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookissuemaster`
--
ALTER TABLE `bookissuemaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookissuetemp`
--
ALTER TABLE `bookissuetemp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookmaster`
--
ALTER TABLE `bookmaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookissuedetails`
--
ALTER TABLE `bookissuedetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `bookissuemaster`
--
ALTER TABLE `bookissuemaster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=52;
--
-- AUTO_INCREMENT for table `bookissuetemp`
--
ALTER TABLE `bookissuetemp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `bookmaster`
--
ALTER TABLE `bookmaster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
