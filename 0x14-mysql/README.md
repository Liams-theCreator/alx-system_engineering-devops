Installing MySQL in web servers


link to install mysql specific version: https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/

had to import key, error when apt update after mysql repo instalation: https://itsfoss.com/solve-gpg-error-signatures-verified-ubuntu/

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv- <pub key>

to create holb user and password: mysql> SET GLOBAL validate_password_policy=LOW; bypass validation error 

=== CREATE USER ===
CREATE USER 'user'@'%' IDENTIFIED BY 'MyStrongPass.';

==== SHOW USER ====
SELECT user FROM mysql.user

=== check privileges ===
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"

=== SHOW PRIVILEGES FROM MYSQL ====
SHOW GRANTS FOR 'user_0d_1'@'localhost';

==== GRANT privileges ======
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost'
USE tyrell_corp; GRANT SELECT ON nexus6 TO 'holberton_user'@'localhost'; 
--> for replica user
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'user'@'user_host';

==============================================================================================
================================= conf mysql REPLICATION =====================================
==============================================================================================

sudo ufw allow from replica_server_ip to any port 3306

confi file set parametres

=== lock tables ===
FLUSH TABLES WITH READ LOCK;

=== get position ===
SHOW MASTER STATUS;
        
        Filename = mysql-bin.000530
        position = 154

=== export database ===
sudo mysqldump -u root tyrell_corp > tyrell_corp.sql


=== copying public key manually ===
getting pkey into local machine
    ssh ubuntu@34.148.38.180 "cat ~/.ssh/id_rsa.pub" >> publickey
appending data of local file to target server
    cat publickey | ssh ubuntu@35.172.200.220 "cat >> ~/.ssh/authorized_keys" 
this could have been done using two ssh from server to server

=== NOW, send snapshot of DB to replica server ===
    scp tyrell_corp.sql ubuntu@35.172.200.220:/tmp/

in my case, database already existed in both servers, but, if not, u can create database and import snapshot:
mysql> CREATE DATABASE db;
mysql> exit
$: sudo mysql db < /tmp/db.sql

====== CONFI OF REPLICA =====
=============================

set parameters in conf file in replica server

then, restart and run following commands in mysql prompt: 

THIS IS NOT WORKING:::BECAUSE IS FOR VERSION 8.0!!!!
mysql> CHANGE REPLICATION SOURCE TO
mysql> SOURCE_HOST='34.148.38.180',
mysql> SOURCE_USER='replica_user',
mysql> SOURCE_PASSWORD='replicauserwebserver012022',
mysql> SOURCE_LOG_FILE='mysql-bin.000530',
mysql> SOURCE_LOG_POS=154;
mysql> START REPLICA;

TRY THE FOLLOWING ::: MYSQL 5.7
mysql> CHANGE MASTER TO
mysql> MASTER_HOST='34.148.38.180',
mysql> MASTER_USER='replica_user',
mysql> MASTER_PASSWORD='replicauserwebserver012022',
mysql> MASTER_LOG_FILE='mysql-bin.000530',
mysql> MASTER_LOG_POS=154;
mysql> START SLAVE;
mysql> SHOW SLAVE STATUS\G;

==== check in main server ===
mysql> SHOW PROCESSLIST\G;

mysql> SHOW SLAVE HOSTS;

=== FINALLY, add a new record to table in wb-01 and see if it replicates on wb-02 ===


execute bash file in remote server:
    ssh ubuntu@34.148.38.180 'bash -s' < ./5-mysql_backup $passw for mysql

