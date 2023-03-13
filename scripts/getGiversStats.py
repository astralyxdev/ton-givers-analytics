import json
import sqlite3

# Read file with all Givers list (grouped by amount - large & small)
with open('./data/givers.json', 'r') as f:
    givers = json.load(f)

# Read SQL DB
db = sqlite3.connect('./data/database.sqlite')
cur = db.cursor()

# SQL Query to get amount of wallets, what received TON's from giver (param: giver)
get_count_query = lambda giver: cur.execute(f"SELECT COUNT(DISTINCT to_wallet) as total_wallets  FROM data WHERE from_wallet = '{giver}';").fetchall()[0][0]

# Count stats for givers
response = {
   "small_givers_stats": {
        giver: get_count_query(giver)
        for giver in givers['small_givers']
    },
   "large_givers_stats": {
        giver: get_count_query(giver)
        for giver in givers['large_givers']
    }
}

# Print result
print(json.dumps(response, indent=4))