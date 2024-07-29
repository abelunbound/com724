# Error Log

#### 

**Code run:** `store_in_postgresql(test_data2, 'digital_assets')`
 
**Error:** `connection to server at "34.170.57.79", port 5432 failed: Connection timed out (0x0000274C/10060)
Is the server running on that host and accepting TCP/IP connections?`

**Solution:** resolved by enabling public access to the database from my home computer

----

**Code run:** `store_in_postgresql(test_data2, 'digital_assets')`

**Error:** `INSERT has more expressions than target columns
LINE 1: ...314.00299072265625, 314.2489929199219, 8036550, 0, 0, 'BTC')
sql = f"INSERT INTO {table_name} (crypto_date, Open, High, Low, Close, Volume, Dividends) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"`

**Solution:** resolved by putting the complete list of columns before the VALUES (%s...)... the last two column names were missing

----
**Code Run:** xxx

**Error:** `invalid input syntax for type double precision: "BTC"`
`LINE 1: ...314.00299072265625, 314.2489929199219, 8036550, 0, 0, 'BTC')`
`PostgreSQL connection is closed`

**Solution:** Resolved by making the column a VARCHAR (could have been TEXT?) 'BTC' column assigned datatype of float when a string was found in the dataframe

----
**Code Run:** 

**Error:**

**Solution:**

----
AttributeError: 'int' object has no attribute 'date'

----
**Code Run:** 

**Error:**

**Solution**

----

**Code Run:** 

**Error:**

**Solution**

----
