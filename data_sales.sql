-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2023 at 10:27 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data_sales`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_master`
--

CREATE TABLE `customer_master` (
  `CUST_ID` varchar(6) NOT NULL,
  `NAMADEPAN` varchar(15) NOT NULL,
  `NAMABELAKANG` varchar(15) DEFAULT NULL,
  `CITY` varchar(15) DEFAULT NULL,
  `PHONE_NO` varchar(13) DEFAULT NULL,
  `BONUS` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_master`
--

INSERT INTO `customer_master` (`CUST_ID`, `NAMADEPAN`, `NAMABELAKANG`, `CITY`, `PHONE_NO`, `BONUS`) VALUES
('C00001', 'GERRANT', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `INVOICENO` varchar(19) NOT NULL,
  `TRANSACTION_DATE` date NOT NULL,
  `BARCODE` varchar(12) NOT NULL,
  `QTY` int(4) NOT NULL,
  `HARGA_MODAL` int(8) NOT NULL,
  `HARGA_JUAL` int(8) NOT NULL,
  `CUST_ID` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`INVOICENO`, `TRANSACTION_DATE`, `BARCODE`, `QTY`, `HARGA_MODAL`, `HARGA_JUAL`, `CUST_ID`) VALUES
('2023/INV-1/29-06', '2023-06-29', '001', 3, 30000, 84360, 'C00001'),
('2023/INV-1/29-06', '2023-06-29', '002', 2, 4000, 6080, 'C00001'),
('2023/INV-2/29-06', '2023-06-29', '001', 1, 5000, 14060, 'C00001'),
('2023/INV-2/29-06', '2023-06-29', '002', 1, 2000, 3040, 'C00001'),
('2023/INV-3/29-06', '2023-06-29', '003', 1, 0, 15000, 'C00001');

-- --------------------------------------------------------

--
-- Table structure for table `price_master`
--

CREATE TABLE `price_master` (
  `STARTDATE` date NOT NULL,
  `ENDDATE` date NOT NULL,
  `BARCODE` varchar(12) NOT NULL,
  `HARGA_SATUAN` int(8) NOT NULL,
  `KETERANGAN` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `price_master`
--

INSERT INTO `price_master` (`STARTDATE`, `ENDDATE`, `BARCODE`, `HARGA_SATUAN`, `KETERANGAN`) VALUES
('2023-06-01', '2023-06-30', '001', 14800, NULL),
('2023-06-01', '2023-06-30', '002', 3200, NULL),
('2023-06-01', '2023-06-30', '003', 15000, NULL),
('2023-06-27', '2023-06-30', '001', 14060, 'diskon'),
('2023-06-27', '2023-06-30', '002', 3040, 'diskon');

-- --------------------------------------------------------

--
-- Table structure for table `product_master`
--

CREATE TABLE `product_master` (
  `BARCODE` varchar(12) NOT NULL,
  `MERK` varchar(15) NOT NULL,
  `NAMA` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_master`
--

INSERT INTO `product_master` (`BARCODE`, `MERK`, `NAMA`) VALUES
('001', 'OREO', 'SOFTCAKE 48g'),
('002', 'OREO', 'SOFTCAKE 16g'),
('003', 'BengBeng', 'ShareIt 10pcs');

-- --------------------------------------------------------

--
-- Table structure for table `staff_master`
--

CREATE TABLE `staff_master` (
  `STAFF_ID` varchar(5) NOT NULL,
  `NAMA_DEPAN` varchar(10) NOT NULL,
  `NAMA_BELAKANG` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff_master`
--

INSERT INTO `staff_master` (`STAFF_ID`, `NAMA_DEPAN`, `NAMA_BELAKANG`) VALUES
('S001', 'Gerrant', 'Hiya');

-- --------------------------------------------------------

--
-- Table structure for table `stock_master`
--

CREATE TABLE `stock_master` (
  `ENTRYDATE` date NOT NULL,
  `SUP_ID` varchar(6) DEFAULT NULL,
  `BARCODE` varchar(12) NOT NULL,
  `QTY` int(4) NOT NULL,
  `MODAL_SATUAN` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock_master`
--

INSERT INTO `stock_master` (`ENTRYDATE`, `SUP_ID`, `BARCODE`, `QTY`, `MODAL_SATUAN`) VALUES
('2023-06-25', 'SUP01', '001', 76, 5000),
('2023-06-25', 'SUP01', '002', 75, 2000),
('2023-06-26', 'SUP01', '002', 2, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `supervisor`
--

CREATE TABLE `supervisor` (
  `STAFF_ID` varchar(5) NOT NULL,
  `SUPERVISOR_ID` varchar(4) NOT NULL,
  `PIN` char(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `supervisor`
--

INSERT INTO `supervisor` (`STAFF_ID`, `SUPERVISOR_ID`, `PIN`) VALUES
('S001', '331', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `supplier_master`
--

CREATE TABLE `supplier_master` (
  `SUP_ID` varchar(6) NOT NULL,
  `NAMA` varchar(15) NOT NULL,
  `CITY` varchar(15) NOT NULL,
  `PHONE_NO` varchar(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `supplier_master`
--

INSERT INTO `supplier_master` (`SUP_ID`, `NAMA`, `CITY`, `PHONE_NO`) VALUES
('SUP01', 'SupplierName', 'Jakarta', '0000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_master`
--
ALTER TABLE `customer_master`
  ADD PRIMARY KEY (`CUST_ID`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`INVOICENO`,`BARCODE`),
  ADD KEY `BARCODE` (`BARCODE`),
  ADD KEY `CUST_ID` (`CUST_ID`);

--
-- Indexes for table `price_master`
--
ALTER TABLE `price_master`
  ADD PRIMARY KEY (`STARTDATE`,`BARCODE`),
  ADD KEY `BARCODE` (`BARCODE`);

--
-- Indexes for table `product_master`
--
ALTER TABLE `product_master`
  ADD PRIMARY KEY (`BARCODE`);

--
-- Indexes for table `staff_master`
--
ALTER TABLE `staff_master`
  ADD PRIMARY KEY (`STAFF_ID`);

--
-- Indexes for table `stock_master`
--
ALTER TABLE `stock_master`
  ADD PRIMARY KEY (`ENTRYDATE`,`BARCODE`),
  ADD KEY `BARCODE` (`BARCODE`),
  ADD KEY `SUP_ID` (`SUP_ID`);

--
-- Indexes for table `supervisor`
--
ALTER TABLE `supervisor`
  ADD PRIMARY KEY (`STAFF_ID`);

--
-- Indexes for table `supplier_master`
--
ALTER TABLE `supplier_master`
  ADD PRIMARY KEY (`SUP_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `invoice`
--
ALTER TABLE `invoice`
  ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`BARCODE`) REFERENCES `product_master` (`BARCODE`),
  ADD CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`CUST_ID`) REFERENCES `customer_master` (`CUST_ID`);

--
-- Constraints for table `price_master`
--
ALTER TABLE `price_master`
  ADD CONSTRAINT `price_master_ibfk_1` FOREIGN KEY (`BARCODE`) REFERENCES `product_master` (`BARCODE`);

--
-- Constraints for table `stock_master`
--
ALTER TABLE `stock_master`
  ADD CONSTRAINT `stock_master_ibfk_1` FOREIGN KEY (`BARCODE`) REFERENCES `product_master` (`BARCODE`),
  ADD CONSTRAINT `stock_master_ibfk_2` FOREIGN KEY (`SUP_ID`) REFERENCES `supplier_master` (`SUP_ID`);

--
-- Constraints for table `supervisor`
--
ALTER TABLE `supervisor`
  ADD CONSTRAINT `supervisor_ibfk_1` FOREIGN KEY (`STAFF_ID`) REFERENCES `staff_master` (`STAFF_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
