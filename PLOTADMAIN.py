import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
#import seaborn as sns
#import statsmodels as sm
#conn = sqlite3.connect("flights.db")
# df = pd.read_sql_query("select * from airlines limit 5;", conn)
# df
wsql = ''
wsql = '{}'. format('select ')
wsql = wsql + '{}\n'.format('nu_r1 B01, nu_r2 B02,   nu_r3 B03,   nu_r4 B04, nu_r5  B05, ')
wsql = wsql + '{}\n'.format('nu_r6 B06, nu_r7 B07,   nu_r8 B08,   nu_r9 B09, nu_r10 B10, ')
wsql = wsql + '{}\n'.format('nu_r11 B11, nu_r12 B12, nu_r13 B13, nu_r14 B14, nu_r15 B15, ')  
wsql = wsql + '{}\n'.format('nu_r16 B16, nu_r17 B17, nu_r18 B18, nu_r19 B19, nu_r20 B20, ') 
wsql = wsql + '{}\n'.format('nu_r21 B21, nu_r22 B22, nu_r23 B23, nu_r24 B24, nu_r25 B25 ')     
wsql = wsql + '{}'.format('from tlotdeze01; ')

conn = sqlite3.connect("DLOT0000.db")
df = pd.read_sql_query(wsql, conn)
df
print(df)
a = 1

print('linhas, colunas         ', df.shape) 
print('Descreve o índice       ', df.index) 
print('Descreve as colunas     ', df.columns)
print('Info sobre o dataframe  ', df.info()) 
print('Número de valores não-NA', df.count())
print('   RESUMOS   ')
print('Soma de valores          ', df.sum()) 
print('Soma acumulada           ', df.cumsum()) 
print('Valores max e min        ', df.min/df.max())
print('Sumário estatístico      ', df.describe() )
print('Média dos valores        ', df.mean() )
print('Mediana dos valores      ', df.median())

