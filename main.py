import requests
import time

def get_data(wallet_address):
	api_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}/balance"
	res = requests.get(api_url)

	if res.status_code == 200:
		wallet_data = dict()
		data = res.json()
		wallet_data['balance'] = data['balance'] / 100_000_000
		wallet_data['total_received'] = data['total_received'] / 100_000_000
		wallet_data['total_sent'] = data['total_sent'] / 100_000_000
		time.sleep(1)
		return wallet_data


f_in = open('in.txt', 'r')
f_out = open('out.txt', 'w')

f_out.write("wallet_address\ttotal_received\ttotal_sent\tbalance\n")

for ligne in f_in:
	address = ligne.strip()
	res = get_data(address)
	print(address, res['total_received'], res['total_sent'], res['balance'])
	f_out.write(address + "\t" + str(res['total_received']) + "\t" + str(res['total_sent']) + "\t" + str(res['balance']) + "\n")

f_in.close()
f_out.close()
