import requests,pprint

ip='10.0.0.49'
url="http://{}/admin/api.php".format(ip)
r = requests.get(url)
data = r.json()
pprint.pprint(data)
