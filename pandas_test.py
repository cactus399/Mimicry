import pandas
import psycopg2
import numpy

df = pandas.DataFrame({
    "col1":[1,2,3,4,5],
    "col2":["this", "is", "acolumn", "stupid", "fifth"],
    "valcol":[0.1,0.2,0.3,0.4,0.5],
    "binary":[True,False,True,False,True]
})

print(df)
