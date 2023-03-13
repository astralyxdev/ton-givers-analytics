import pandas as pd
import sqlite3


# Read data from TON Tech
df = pd.read_csv('./data/mining_tx.csv')

# Open connection to database
db = sqlite3.connect('./data/database.sqlite')
cur = db.cursor()

# Create table similiar to csv file columns
cur.execute("""CREATE TABLE IF NOT EXISTS data (
    date TIMESTAMP,
    to_wallet VARCHAR(256),
    from_wallet VARCHAR(256),
    tx_id VARCHAR(256),
    msg_type VARCHAR(256),
    amount FLOAT
)""")
db.commit()


for index, row in df.iterrows():
    
    # get data from CSV
    created_at = int(row['created_at'])
    to_wallet = str(row['dst'])
    from_wallet = str(row['src'])
    id_ = str(row['id'])
    msg_type = str(row['msg_type'])
    amount = float(row['value'])/(10**9)
    
    if amount != float(row['amount']):
        print("[panic] different values of amount in CSV")
    
    # write to SQL
    cur.execute(f"""INSERT INTO data (date, to_wallet, from_wallet, tx_id, msg_type, amount) VALUES ({created_at}, '{to_wallet}', '{from_wallet}', '{id_}', '{msg_type}', {amount})""")

# write to SQL DB
db.commit()
print("Database file created: <./data/database.sqlite>")