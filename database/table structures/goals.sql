CREATE TABLE `goals` (
  `goal_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `goals`
  ADD PRIMARY KEY (`goal_id`),
  ADD KEY `goals_FK_employee` (`eid`);

ALTER TABLE `goals`
  MODIFY `goal_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `goals`
  ADD CONSTRAINT `goals_FK_employee` FOREIGN KEY (`eid`) REFERENCES `employee` (`eid`);
COMMIT;
