import requests, pprint

ip='10.0.0.49'
url="http://{}/admin/api.php".format(ip)

def getApiData(url):
    ''' Query piHole API for data '''
    r = requests.get(url)
    return r

def makeDict():
    r = getApiData(url)
    data = r.json()

    dataDict = {'ads_blocked_today': data['ads_blocked_today'],
    'ads_percentage_today': data['ads_percentage_today'],
    'dns_queries_today': data['dns_queries_today'],
    'domains_being_blocked': data['domains_being_blocked'],
    'queries_cached': data['queries_cached'],
    'queries_forwarded': data['queries_forwarded'],
    'unique_clients': data['unique_clients'],
    'unique_domains': data['unique_domains']}

    return dataDict

for k,v in makeDict().items():
    print(k,v)

plugin_object_type=1581
plugin_id=10
indicator_type_id_domains_being_blocked = 12913
indicator_type_id_dns_being_blocked = 12914
