import requests

# System ID:2527105

params = (
    ('key', '33443540a4c162ed92df1c878e87867b'),  # 4d6a55794e7a55354d413d3d0a #
    ('user_id', '4d6a55794e7a55354d413d3d0a'),  # 4d6a55794e7a55354d413d3d0a
)

response = requests.get(
    'https://enlighten.enphaseenergy.com/app_user_auth/new?app_id=1409622241421',  params=params)  # 'https://api.enphaseenergy.com/api/v2/systems', # https://enlighten.enphaseenergy.com/app_user_auth/new?app_id=1409622241421 # https://api.enphaseenergy.com/api/v2/systems/[system_id]/stats

print(response)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api.enphaseenergy.com/api/v2/systems/67/summary?key=APPLICATION-API-KEY&user_id=ENLIGHTEN-USERID')
