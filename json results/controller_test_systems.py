import json

f = open("/Users/stevenbailey/UDI Development PG3/Nodeservers/udi-enphase-poly-master-v3/json results/owners-systems.txt", "r")
# print(f.read())  # str
data = f.read()
# js = json.loads(data)
systemResponse = json.loads(data)

print('\n System ID \n', systemResponse["systems"][0]["system_id"])
#print('\n System Status \n', systemResponse["systems"][0]["status"])
#print('\n System Country \n', systemResponse["systems"][0]["country"])
print('\n System ID \n', systemResponse["systems"][1]["system_id"])
#print('\n System Status \n', systemResponse["systems"][1]["status"])
#print('\n System Country \n', systemResponse["systems"][1]["country"])
hellohere = systemResponse["systems"][0]
print(hellohere)
num_sites = (print('\n System One \n', systemResponse["systems"][0]))
num_sites = (print('\n System Two \n', systemResponse["systems"][1]))
