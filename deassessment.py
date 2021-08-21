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