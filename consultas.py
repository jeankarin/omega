#!/usr/bin/python
#-*-coding:latin-1-*-

def InsertNum(num):
	sql = ("""CALL PA_INSERT_NUMERO (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % (num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9],num[10],num[11]))
	return sql