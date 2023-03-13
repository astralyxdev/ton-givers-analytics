import sqlite3
import json

# Connect to DB
db = sqlite3.connect('./data/database.sqlite')
cur = db.cursor()

# Get miners wallets and amounts
data = cur.execute(f"SELECT to_wallet, amount FROM data").fetchall()

wallets = {}
total_tons = 0

for wallet_data in data:
    address = wallet_data[0]
    amount = wallet_data[1]
    
    total_tons += amount
    
    if address in wallets.keys():
        wallets[address] += amount
    else:
        wallets[address] = amount


print("Unique miners: ", len(list(wallets.keys())))
print("Total mined TON's: ", total_tons)


with open('./out/all_miners.json', 'w') as f:
    f.write(json.dumps(wallets, indent=4))
    f.close()
print("\nTotal list of unique miners was written to <./out/all_miners.json>")
