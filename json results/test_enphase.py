import requests
import json

# System ID:2527105
# url auth? 1409622241421

params = (
    ('key', '33443540a4c162ed92df1c878e87867b'),  # 4d6a55794e7a55354d413d3d0a #
    ('user_id', '4d6a55794e7a55354d413d3d0a'),  # 4d6a55794e7a55354d413d3d0a
)

"""response = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=2527105',  params=params)  # 'https://api.enphaseenergy.com/api/v2/systems', # https://enlighten.enphaseenergy.com/app_user_auth/new?app_id=1409622241421 # https://api.enphaseenergy.com/api/v2/systems/[system_id]/stats
# https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=1409622241421
print(response)


response2 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime',  params=params).text
print('\n Lifetime Energy Daily Report \n' + response2)"""

# Customers Systems = system_id
# for loop looking at system id to add Systems
response3 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems',  params=params).text
#print( response3)
systemResponse = json.loads(response3)
print('\n System ID \n', systemResponse["systems"][0]["system_id"])
print('\n System Status \n', systemResponse["systems"][0]["status"])
print('\n System Country \n', systemResponse["systems"][0]["country"])
hellohere = systemResponse["systems"][0]

#print('\n Str Found \n {} sites'.format(hellohere))
# print(hellohere["system_id"])
#howlong = len(hellohere["system_id"])
# print(howlong)
for i in hellohere:
    print('\n', i,  hellohere[i])

    #'system_id' in hellohere.values()
    #print(i, hellohere[i])

"""response4 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/inventory',  params=params).text
print('\n Equipmet Inventory \n' + response4)

response5 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/stats?datetime_format=iso8601',  params=params).text
print('\n Equipment Stats \n' + response5)

response6 = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/inverters_summary_by_envoy_or_site?site_id=2527105',  params=params).text  # for loop for solar array
print('\n Inverters \n' + response6)"""

response = requests.get(
    'https://api.enphaseenergy.com/api/v2/systems/2527105/summary',  params=params)
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
#    print(value)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api.enphaseenergy.com/api/v2/systems/67/summary?key=APPLICATION-API-KEY&user_id=ENLIGHTEN-USERID')
