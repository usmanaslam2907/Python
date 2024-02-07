# key values pairs (Dicttionary)
d1 = {"name": "usman", "city": "lahore", "gender": "Male"}
print(d1.values())
print(d1.items())
"""d1={} # () blank tuple and [] blank lists
print(type(d1))"""
david = d1.copy()
david["phone"] = "03424073856"
print(david.items())
print(david.get("city"))
dic = {"usman": "aslam", "nisar": "ahmad", "zeeshan": "javed",
       "khan": {"usman": "pizza", "nisar": "dahi bhale", "zeeshan": "no-food"}}
"""print(dic)
print("Father name is: ",dic["zeeshan"])
print(dic["khan"])"""
"""dic["rafey"]="burger"
print(dic)
del dic["zeeshan"]
print(dic)"""
david.update({"city": "karachi"})
d = dic.copy()
"""d["waqar"]="afzal"
print(d)

print(d.get("usman"))
d.update({"king":"is back"})
print(d)"""
# print(d.keys())
# print(d.items())
