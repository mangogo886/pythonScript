CREATE TABLE `base_jk_ng_config` (
  `ip` varchar(50) DEFAULT NULL,
  `jkname` varchar(50) DEFAULT NULL,
  `remark` int(2) DEFAULT NULL COMMENT '0为前端，1为后端',
  `ng_config` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;