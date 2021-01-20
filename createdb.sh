#!/bin/bash

#get the database name
read -p "Database name: " name

#get the database password with default
read -p "Password [dbpass]: " pass
pass=${pass:-dbpass}

#get the database creator with default
read -p "Database creator [root]: " user
user=${user:-root}

# create the database table
read -p "Table name: " tablename



#execute sql commands with the user
mysql -u $user -p -e "CREATE DATABASE $name;CREATE USER $name @localhost identified by '$pass';GRANT ALL ON $name.* to $name@localhost WITH GRANT OPTION;
USE $name;CREATE TABLE $tablename (ID varchar(255),UserID int,name varchar(255));
ALTER TABLE $tablename ADD lastEdited TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;ALTER TABLE $tablename ADD lastEditedBy varchar(255);
ALTER TABLE $tablename ADD createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE $tablename ADD createdBy varchar(255);"

#confirmation message
echo "Created database  and user: $name and table $tablename"



