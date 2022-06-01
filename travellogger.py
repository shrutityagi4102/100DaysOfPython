travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def addcountry(cname, cvisit, ccity):
    c={}
    c["country"] = cname
    c["visits"] = cvisit
    c["cities"] = ccity
    travel_log.append(c)

addcountry("India","19",["Mumbai","Bangalore","Nagpur","Pune"])
print(travel_log)

