import csv
from pprint import pprint

user_req = input("Enter SKU: ")

total, cols = 0, []
with open('TRANS.csv', "r+") as data_file:
    data = csv.reader(data_file, delimiter=',')
    for datum in data:
        cols.append(datum)


# converts the data to json
def jsonify_custom(data_to_convert):
    return [{"STORE": d[0], "SKU": d[1], "KSH": int(d[2].replace(" KSH", ""))} for d in data_to_convert[1:]]


# filters the data to obtain the total cash
def filter_data(data_in):
    data_out = {"Total KSH": 0, "Largest": ""}
    filter_by_sku = []
    for j in data_in:
        if j.get("SKU") == user_req.upper():
            data_out["Total KSH"] += j.get("KSH")
            filter_by_sku.append({"STORE": j.get("STORE"), "SKU": j.get("SKU"), "KSH": j.get("KSH")})
    town = max(obtain_high(filter_by_sku))[1]
    data_out["Largest"] = town
    return data_out


# sieves the store with the highest sales per item, returns the
def obtain_high(data_to_filter):
    stores, total, curated, largest = [], 0, [], ""
    for s in data_to_filter:
        stores.append(s.get("STORE"))
    unique = list(set(stores))
    for st in unique:
        for t in data_to_filter:
            if t.get("STORE") == st:
                total += t.get("KSH")
        curated.append((total, st))
    return curated


pprint(filter_data(jsonify_custom(cols)))
