CREATE TABLE `zk_node` (
   `id`  bigint(20)NOT NULL AUTO_INCREMENT,
  `appCode`	 varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `content` varchar(5000) DEFAULT NULL,
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;