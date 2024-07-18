#0x0E. SQL - More queries
## Resources

### Read or watch:

* How To Create a New User and Grant Permissions in MySQL
* How To Use MySQL GRANT Statement To Grant Privileges To a User
* MySQL constraints
* SQL technique: subqueries
* Basic query operation: the join
* SQL technique: multiple joins and the distinct keyword
* SQL technique: join types
* SQL technique: union and minus
* MySQL Cheat Sheet
* The Seven Types of SQL Joins
* MySQL Tutorial
* SQL Style Guide
* MySQL 8.0 SQL Statement Syntax

### Extra resources around relational database model design:

* Design
* Normalization
* ER Modeling

## Learning Objectives

By the end of this project, you should be able to explain:

* **General**
    * How to create and manage MySQL users and their privileges.
    * Concepts of PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE constraints.
    * How to retrieve data from multiple tables using JOINs.
    * Subqueries, JOINs, and UNIONs.

## Copyright - Plagiarism

* **You are expected to create your own solutions.**
* **Do not copy and paste others' work.**
* **Do not publish this project's content.**
* **Plagiarism is strictly forbidden.**

## Requirements

* **Editors:** vi, vim, emacs
* **Environment:** Ubuntu 20.04 LTS, MySQL 8.0 (version 8.0.25)
* **Formatting:**
    * End files with a new line.
    * Comment SQL queries.
    * Start files with a task description comment.
    * Use uppercase for SQL keywords.
* **README:** A README.md file is mandatory at the project root.
* **File Length:** Will be checked using `wc`.

## More Info

### Comments in SQL Files:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```
##Tasks
###0. My privileges!
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0E-SQL_more_queries
    File: 0-privileges.sql

### Root user
Write a script that creates the MySQL server user user_0d_1.

    user_0d_1 should have all privileges on your MySQL server
    The user_0d_1 password should be set to user_0d_1_pwd
    If the user user_0d_1 already exists, your script should not fail

guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0E-SQL_more_queries
    File: 1-create_user.sql


