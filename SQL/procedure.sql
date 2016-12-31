CREATE DEFINER=`euromillon_user`@`%` PROCEDURE `PA_INSERT_NUMERO`(
nuevo_NUM01 INT(11),
nuevo_NUM02 INT(11),
nuevo_NUM03 INT(11),
nuevo_NUM04 INT(11),
nuevo_NUM05 INT(11),
nuevo_STAR01 INT(11),
nuevo_STAR02 INT(11),
nuevo_DIASEM varchar(8),
nuevo_DIA INT(11),
nuevo_MES varchar(45),
nuevo_ANYO INT(11),
nuevo_MILLON varchar(10)
)
INSERT INTO NUMEROS (ID,NUM01,NUM02,NUM03,NUM04,NUM05,STAR01,STAR02,DIASEM,DIA,MES,ANYO,MILLON) 
VALUES (NULL,nuevo_NUM01,nuevo_NUM02,nuevo_NUM03,nuevo_NUM04,nuevo_NUM05,nuevo_STAR01,nuevo_STAR02,nuevo_DIASEM,nuevo_DIA,nuevo_MES,nuevo_ANYO,nuevo_MILLON)
