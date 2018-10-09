#!/bin/bash

DB_USER=
DB_PASSWORD=
DB_SERVER=


#tc.txt
sqlplus -s $DB_USER/$DB_PASSWORD@$DB_SERVER  <<tc

set echo off;
set feedback off;
set heading on;
set pagesize 0;
set linesize 500;
set termout off
set trimspool off;
set verify off;
set trims on;
spool /home/zjyw/ops/taskScript/tc.txt;


select '330000'||'|'||'P330000'||'|'||id||'|'|| 0 ||'|'|| name||'|'||1||'|'||salemodalid||'|'||
to_char(create_time,'yyyy-mm-dd hh24:mi:ss')||'|'||decode(charge_type,5,2,6,3,1)||'|'||
decode(fee,0,2,1)||'|'|| 1 from zjxxt.tranpackage_define 
union all
select '330000'||'|'||'P330000'||'|'||id||'|'|| cp_id||'|'|| name||'|'||2 ||'|'||code||'|'||
to_char(add_date,'yyyy-mm-dd hh24:mi:ss')||'|'||1||'|'||
decode(fee,0,2,1)||'|'|| 1  from zjxxt.cp_transaction; 


spool off
tc


#resource.txt
sqlplus -s $DB_USER/$DB_PASSWORD@$DB_SERVER  <<resource

set echo off;
set feedback off;
set heading on;
set pagesize 0;
set linesize 500;
set termout off
set trimspool off;
set verify off;
set trims on;
spool /home/zjyw/ops/taskScript/resource.txt;


select '330000'||'|'||'P330000'||'|'||id||'|'|| 0||'|'|| lesson_name||'|'||lesson_name||'|'||
 5||'|'||'mp4'||'|'||'' ||'|'|| '' ||'|'|| '' ||'|'|| '' ||'|'|| '' ||'|'|| '' ||'|'|| 
 '' ||'|'|| '' ||'|'|| ''||'|'||''||'|'|| 1048576000||'|'|| to_char(ct,'yyyy-mm-dd hh24:mi:ss')||'|'||
 '' ||'|'|| 1  from zjxxt.xxt_rec_lesson;


spool off
resource