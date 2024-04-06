CREATE TABLE `leaves` (
  `leave_id` int(11) NOT NULL,
  `leave_type` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

  ADD PRIMARY KEY (`leave_id`),
  ADD KEY `leaves_FK_employee` (`eid`);

ALTER TABLE `leaves`
  MODIFY `leave_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `leaves`
  ADD CONSTRAINT `leaves_FK_employee` FOREIGN KEY (`eid`) REFERENCES `employee` (`eid`);
COMMIT;