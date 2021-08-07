import json
average_prof = 0
count = 0
firm_dict = {}
list_info = []
average_profit = {}
with open('Firms', 'r', encoding="utf-8") as file_obj, open('JSON_Firms', 'w') as json_firm:
    for i in file_obj:
        name, *data = i.split()
        data = list(map(int, data[1:3]))
        profit = data[0]-data[1]
        if profit > 0:
            average_prof += profit
            count += 1
        firm_dict.update({name: profit})
    average_profit.update({"average_profit": (average_prof/count)})
    list_info = firm_dict, average_profit
    print(list_info)
    json.dump(list_info, json_firm)

