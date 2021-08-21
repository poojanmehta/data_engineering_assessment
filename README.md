# data_engineering_assessment

This is the project for an assessment

### install pandas
```bash
pip install pandas
```

### install pymysql
```bash
pip install pymysql
```

### enter custom parameters to run it in your machine

```python
connection = pymysql.connect(host = "localhost",  
                             user = "root",  
                             password = "PASSWORD",  
                             database = "DB")
```
### create table customer_data using below script

```sql
CREATE TABLE `customer_data` (
  `id` int PRIMARY KEY,
  `cust_name` varchar(50) NOT NULL,
  `cust_city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `shop_amount` decimal(15,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 
```
### you can use this values for demo purpose also
```sql
INSERT INTO `customer_data` (`id`, `cust_name`, `cust_city`, `country`, `shop_amount`) VALUES
(21, 'Mayank Shah', 'Ahmedabad', 'INDIA', '2000'),
(22, 'Poojan Mehta', 'Ahmedabad', 'INDIA', '5000'),
(23, 'Jack Ryan', 'New York', 'USA', '10000'),
(24, 'Will Smith', 'Sydney', 'Australia', '5500'),
(25, 'Tanaka Suzuki', 'Tokyo', 'JAPAN', '2000'),
(26, 'Paul', 'London', 'UK', '12000');
COMMIT;
```

### after checking connection run the program  
it will create tables for each unique country available in `customer_data`  
and insert records for all countries in it's respective country table  
you do not need to explicitly enter any other inforamtion

### you can check all newly created tables from above data by using this statement
```sql
SHOW TABLES
```

 
