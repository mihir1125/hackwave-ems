CREATE TABLE `employee` (
  `eid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `doj` date NOT NULL DEFAULT current_timestamp(),
  `mobile_no` varchar(20) NOT NULL,
  `salary` float NOT NULL,
  `department` int(11) NOT NULL,
  `designation` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `employee`
  ADD PRIMARY KEY (`eid`);

ALTER TABLE `employee`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;