# TON Givers Analytics
We have developed several scripts to analyze transactions sent from Givers contracts.


## QA
| Question | Answer 
|-|-
| What is the total amount of mining wallets? | 3278 
| How many wallets were used for Large Giver mining? | 248 
| How many wallets were used for Small Giver mining? | 3156 
| Total TON's amount from Small Givers | 127398100.0 
| Total TON's amount from Large Givers | 4800000000.0
| Total TON's amount from All Givers | 4927398100.0


## Installation

Download file **database.sqlite** and **mining_tx.csv** to folder data from [Google Drive](https://drive.google.com/drive/folders/1KZUKmjGqcGaNpKeDunBgg5Ixgz5qTQDW?usp=sharing)

```sh
# clone repository, run scripts from `scripts` folder
pip install -r requirements.txt
```


## Create files and folders

* data/
	* mining_tx.csv - raw data from TON Tech
	* database.sqlite - converted CSV to SQL
	* givers.json - list of all givers (provided by docs.ton.org)
	* queries.sql - all important queries to get data (described)
* out/
	* empty, there is response of some scripts
* scripts/
	* CSV2SQL.py - convert CSV to SQL DB
	* getGiversStats.py - get givers stats
	* getMinersStats.py - get miners stats

## Queries

#### Get amount of all Miners wallets
```sql
SELECT  COUNT(DISTINCT  to_wallet) as  wallets_amount  FROM  data;
```

#### Get amount of wallets, whos received TON's from giver
```sql
SELECT  COUNT(DISTINCT  to_wallet) as  wallets_amount  FROM  data  WHERE  from_wallet = "GIVER_ADDRESS_HERE";
```
  
#### Get amount of wallets, whos received TON's from Large Givers (all)
```sql
SELECT  COUNT(DISTINCT  to_wallet) as  wallets_amount  FROM  data  WHERE  from_wallet  in (
	"Ef8guqdIbY6kpMykR8WFeVGbZcP2iuBagXfnQuq0rGrxgPay",
	"Ef9CxReRyaGj0vpSH0gRZkOAitm_yDHvgiMGtmvG-ZTirgiI",
	"Ef-WXA4CX4lqyVlN4qItlQSWPFIy00NvO2BAydgC4CTeIfIU",
	"Ef8yF4oXfIj7BZgkqXM6VsmDEgCqWVSKECO1pC0LXWl39277",
	"Ef9nNY69S3_heBBSUtpHRhIzjjqY0ChugeqbWcQGtGj-gbfE",
	"Ef_wUXx-l1Ehw0kfQRgFtWKO07B6WhSqcUQZNyh4Jmj8RzdB",
	"Ef_6keW5RniwNQYeq3DNWGcohKOwI85p-V2MsPk4v23tyFZC",
	"Ef_NSPpF4ZQ7mrPylwk-8XQQ1qFD5evLnx5_oZVNywzOjZxr",
	"Ef-uNWj4JmTJefr7IfjBSYQhFbd3JqtQ6cxuNIsJqDQ8SpqK",
	"Ef8mO4l6ZB_eaMn1OqjLRrrkiBcSt7kYTvJC_dzJLdpEDBft"
);
```
  
#### Get amount of wallets, whos received TON's from Small Givers (all)
```sql
SELECT  COUNT(DISTINCT  to_wallet) as  wallets_amount  FROM  data  WHERE  from_wallet  in (
	"Ef-kkdY_B7p-77TLn2hUhM6QidWrrsl8FYWCIvBMpZKprKDH",
	"Ef8SYc83pm5JkGt0p3TQRkuiM58O9Cr3waUtR9OoFq716uj0",
	"Ef-FV4QTxLl-7Ct3E6MqOtMt-RGXMxi27g4I645lw6MTWg0f",
	"Ef_NSzfDJI1A3rOM0GQm7xsoUXHTgmdhN5-OrGD8uwL2JHBa",
	"Ef8gf1PQy4u2kURl-Gz4LbS29eaN4sVdrVQkPO-JL80VhFww",
	"Ef8kO6K6Qh6YM4ddjRYYlvVAK7IgyW8Zet-4ZvNrVsmQ4PgP",
	"Ef-P_TOdwcCh0AXHhBpICDMxStxHenWdLCDLNH5QcNpwMMn2",
	"Ef91o4NNTryJ-Cw3sDGt9OTiafmETdVFUMvylQdFPoOxInls",
	"Ef9iWhwk9GwAXjtwKG-vN7rmXT3hLIT23RBY6KhVaynRrDkx",
	"Ef8JfFUEJhhpRW80_jqD7zzQteH6EBHOzxiOhygRhBdt44YH"
);
```

#### Get total amount of TON's sent from giver
```sql 
SELECT  SUM(amount) as  total_amount  FROM  data  WHERE  from_wallet = ”GIVER_ADDRESS_HERE”; 
```

#### Get total amount of TON's sent from Large Givers (all)
```sql
SELECT  SUM(amount) as  total_amount  FROM  data  WHERE  from_wallet  in (
	"Ef8guqdIbY6kpMykR8WFeVGbZcP2iuBagXfnQuq0rGrxgPay",
	"Ef9CxReRyaGj0vpSH0gRZkOAitm_yDHvgiMGtmvG-ZTirgiI",
	"Ef-WXA4CX4lqyVlN4qItlQSWPFIy00NvO2BAydgC4CTeIfIU",
	"Ef8yF4oXfIj7BZgkqXM6VsmDEgCqWVSKECO1pC0LXWl39277",
	"Ef9nNY69S3_heBBSUtpHRhIzjjqY0ChugeqbWcQGtGj-gbfE",
	"Ef_wUXx-l1Ehw0kfQRgFtWKO07B6WhSqcUQZNyh4Jmj8RzdB",
	"Ef_6keW5RniwNQYeq3DNWGcohKOwI85p-V2MsPk4v23tyFZC",
	"Ef_NSPpF4ZQ7mrPylwk-8XQQ1qFD5evLnx5_oZVNywzOjZxr",
	"Ef-uNWj4JmTJefr7IfjBSYQhFbd3JqtQ6cxuNIsJqDQ8SpqK",
	"Ef8mO4l6ZB_eaMn1OqjLRrrkiBcSt7kYTvJC_dzJLdpEDBft"
);
```
  
  

#### Get total amount of TON's sent from Small Givers (all)
```sql
SELECT  SUM(amount) as  total_amount  FROM  data  WHERE  from_wallet  in (
	"Ef-kkdY_B7p-77TLn2hUhM6QidWrrsl8FYWCIvBMpZKprKDH",
	"Ef8SYc83pm5JkGt0p3TQRkuiM58O9Cr3waUtR9OoFq716uj0",
	"Ef-FV4QTxLl-7Ct3E6MqOtMt-RGXMxi27g4I645lw6MTWg0f",
	"Ef_NSzfDJI1A3rOM0GQm7xsoUXHTgmdhN5-OrGD8uwL2JHBa",
	"Ef8gf1PQy4u2kURl-Gz4LbS29eaN4sVdrVQkPO-JL80VhFww",
	"Ef8kO6K6Qh6YM4ddjRYYlvVAK7IgyW8Zet-4ZvNrVsmQ4PgP",
	"Ef-P_TOdwcCh0AXHhBpICDMxStxHenWdLCDLNH5QcNpwMMn2",
	"Ef91o4NNTryJ-Cw3sDGt9OTiafmETdVFUMvylQdFPoOxInls",
	"Ef9iWhwk9GwAXjtwKG-vN7rmXT3hLIT23RBY6KhVaynRrDkx",
	"Ef8JfFUEJhhpRW80_jqD7zzQteH6EBHOzxiOhygRhBdt44YH"
);
```
  
#### Get total amount of TON's sent from all givers
```sql
SELECT  SUM(amount) as  total_amount  FROM  data
```
  
#### Get amount of TON's mined per week
```sql
​​SELECT
strftime("%Y-%W", DATE(date, 'unixepoch')) as  week,
max(date(DATE(date, 'unixepoch'), 'weekday 0', '-7 day')) as  weekstart,
max(date(DATE(date, 'unixepoch'), 'weekday 0', '-0 day')) as  weekend,
SUM(amount)
from  data
GROUP  BY  week
```
  
#### Get amount of TON's mined per month
```sql
SELECT  SUM(amount), strftime("%Y-%m", DATE(date, 'unixepoch')) as  month  from  data
GROUP  BY  month
```
