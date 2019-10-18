select * from base_jk_ng_config
where jkname in (select   jkname from   base_jk_ng_config group by  jkname having count(jkname) > 1);