import pandas as pd
import numpy as np
import sqlite3

with sqlite3.connect('lesson-17/homework/data/chinook.db') as connection:
        customers_df = pd.read_sql_query("SELECT * FROM customers", 
                                         conn=connection)
                                    

with sqlite3.connect('lesson-17/homework/data/chinook.db') as connection:
       invoices_df = pd.read_sql_query("SELECT * FROM invoices", 
                                       conn=connection)  



customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

joined_df=pd.merge(customers_df,invoices_df,on='CustomerId',how='inner')

invoices_count=customers_df.groupby(['CustomerId','FirstName','LastName']).size().reset_index

print(invoices_count.head())