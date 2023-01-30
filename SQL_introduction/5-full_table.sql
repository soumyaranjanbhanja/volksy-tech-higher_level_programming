-- script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
SHOW CREATE TABLE first_table`(
`id`intNOTNULLAUTO_INCREMENT,
`name`varchar(128)DEFAULTNULL,
`c`char(1)DEFAULTNULL,
`created_at`dateDEFAULTNULL,
PRIMARYKEY(`id`)
)
