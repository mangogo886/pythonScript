CREATE TABLE `zk_node` (
   `id`  bigint(20)NOT NULL AUTO_INCREMENT,
  `appCode`	 varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `content` varchar(5000) DEFAULT NULL,
  `mark`  int(1) NOT NULL  DEFAULT '1',
  `update_time`  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;