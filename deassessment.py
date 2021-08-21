import pandas as pd
from sqlalchemy import create_engine
import pymysql
import pandas as pd

# establishing connection pool for database "customer_country_info"
connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "",
                             database = "customer_country_info")

# getting cursor using connection object
cursor = connection.cursor()

# query for getting all the data
all_customers = "SELECT * FROM `customer_data`"

# execute the query using execute() method
cursor.execute(all_customers)

# fetch all records from table "customer data" 
# and converting it into pandas dataframe object
customer_data = pd.DataFrame(cursor.fetchall())
print(customer_data)

# find all the unique countries from customer records
all_countries = customer_data[3].unique()

print(all_countries)

# thil loop is to create table for all countries
# iterate n time where n=total unique countries
for country in all_countries:
    
    # prepare query for creating table 
    # this is dynamic query and change the table name according to the country
    create_table = "CREATE TABLE IF NOT EXISTS `{table}` (`id` int NOT NULL PRIMARY KEY, `cust_name` VARCHAR(50), `city` VARCHAR(50))".format(table = country)
    
    # execute query
    cursor.execute(create_table)
    
    # printing all the successful table creation
    print(country, " table created successfully")

# insert record in it's country table
# for loop will iterate n times where n=total unique countries
for country in all_countries:
    
    # filtering records with it's country name
    country_data = customer_data.loc[customer_data[3] == country]
    
    # selecting only id, customer name and city columns  
    country_data = country_data.iloc[:, 0:3]
    print(country_data)
    
    # query toget all data from it's respective country table
    countryQuery = "SELECT * FROM {table}".format(table = country)
    print(countryQuery)
    cursor.execute(countryQuery)
    old_country_data = pd.DataFrame(cursor.fetchall())
    print(old_country_data)
    
    # find distinguish data and storing them that are not present in old database
    distinct_data = country_data[~country_data.isin(old_country_data)].dropna()
    print(distinct_data)        
    

