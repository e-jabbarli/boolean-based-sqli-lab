# Setup of Lab

Make sure that you have installed PHP and MySQL.

## MySQL Configuration

Login to MySQL and create a database:

```sql
CREATE DATABASE databasename;
```

Create a table:

```sql
USE databasename;
CREATE TABLE my_table (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);
```

Insert data into the table:

```sql
INSERT INTO my_table (name) VALUES ('test1');
```

## PHP Configuration

Go to the PHP folder and run this command:

```bash
php -S 0.0.0.0:80
```

## Log all queries in MySQL

```
SET global log_output = 'FILE';
SET global general_log_file='/tmp/mysql_general.log';
SET global general_log = 1;
```

See logs as a live

```
tail -f /tmp/mysql_general.log
