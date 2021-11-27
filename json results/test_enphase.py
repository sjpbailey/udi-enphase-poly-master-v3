import requests
import json
from datetime import datetime, timedelta

# System ID:2527105
# url auth? 1409622241421

key = '33443540a4c162ed92df1c878e87867b'
user_id = '4d6a55794e7a55354d413d3d0a'

params = (('key', key), ('user_id', user_id))
#('key', '33443540a4c162ed92df1c878e87867b'),  # 4d6a55794e7a55354d413d3d0a #
# ('user_id', '4d6a55794e7a55354d413d3d0a'),  # 4d6a55794e7a55354d413d3d0a
# )

"""response = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=2527105',  params=params)  # 'https://api.enphaseenergy.com/api/v2/systems', # https://enlighten.enphaseenergy.com/app_user_auth/new?app_id=1409622241421 # https://api.enphaseenergy.com/api/v2/systems/[system_id]/stats
# https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=1409622241421
print(response)

presentday = datetime.now()
yesterday = presentday - timedelta(1)
second = presentday - timedelta(2)
third = presentday - timedelta(3)

start_date = yesterday.strftime('%Y-%m-%d')
end_date = presentday.strftime('%Y-%m-%d')
end_scnd = second.strftime('%Y-%m-%d')
end_tird = third.strftime('%Y-%m-%d')

# print(start_date)
# print(end_date)
# print(end_scnd)
# print(end_tird)


# 'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date=2021-11-10&end_date=2021-11-25'
# 'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?+start_date+end_date'
response2 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date='+start_date+'&end_date='+end_date,  params=params).text
#print('\n Lifetime Energy Daily Report \n' + response2)
response3 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date='+end_scnd+'&end_date='+end_scnd,  params=params).text
#print('\n Lifetime Energy Daily Report \n' + response3)
response4 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date='+end_tird+'&end_date='+end_tird,  params=params).text
#print('\n Lifetime Energy Daily Report \n' + response4)

# gives 401 is no consumption meter
response8 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/consumption_lifetimeconsumption_lifetime',  params=params).text
print('\n rgm \n' + response8)

# Customers Systems = system_id
# for loop looking at system id to add Systems
response3 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems', params=params).text  # params=params
# print(response3)
systemResponse = json.loads(response3)
print(systemResponse["systems"][0]["status"])
print('\n System ID \n', systemResponse["systems"][0]["system_id"])
#print('\n System Status \n', systemResponse["systems"][0]["status"])
#print('\n System Country \n', systemResponse["systems"][0]["country"])
hellohere = systemResponse["systems"][0]

#print('\n Str Found \n {} sites'.format(hellohere))
# print(hellohere["system_id"])
#howlong = len(hellohere["system_id"])
# print(howlong)
# for i in hellohere:
#    print('\n', i,  hellohere[i])

#'system_id' in hellohere.values()
#print(i, hellohere[i])"""

# energy_lifetime?start_date=2013-01-01&end_date=2013-01-06

"""response4 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/inventory',  params=params).text
print('\n Equipmet Inventory \n' + response4)"""

"""response5 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/stats?datetime_format=iso8601',  params=params).text
print('\n Equipment Stats \n' + response5)"""

response6 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=2527105',  params=params).text  # for loop for solar array
print('\n Inverters \n' + response6)
for i in response6["micro_inverters"]:  # inverter_summary
    inverters = str(["micro_inverters"])
    print(inverters)    # inverter

system_id = '2527105'
response = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/' + system_id + '/summary',  params=params)
#print('\n Summary \n' + response)
jsonResponse = json.loads(response.text)

# print(response.text.encode('utf8'))
print('\n System kW \n', jsonResponse["current_power"])
print('\n System kWh \n', jsonResponse["energy_today"]/1000)
print('\n System Status \n', jsonResponse["status"])
print('\n System kWh Today\n', jsonResponse["energy_today"]/1000)
print('\n System kWh Life Time\n', jsonResponse["energy_lifetime"]/1000)

# print(int(jsonResponse["current_power"]))

# print(response3["system_id"])
# for key, value in response7:
#    print(value)"""


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api.enphaseenergy.com/api/v2/systems/67/summary?key=APPLICATION-API-KEY&user_id=ENLIGHTEN-USERID')
