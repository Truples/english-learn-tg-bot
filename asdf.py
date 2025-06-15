import json


# dct = {312094781: {"cat": "кошка","dog": "собака"}, 7864766999: {"pen": "ручка","table": "стол", "Ben": "Бен"}}
# id786 = dct[7864766999]
# id786["jam"] = "варенье"   
# print(dct)
# dct[91281284] = {"better": "лучше"}
# print(dct)
# wordt = id786["table"]
# file = open("ttr.json", "w", encoding="UTF-8")
# json.dump(dct,file,ensure_ascii=False,indent=4)
# file.close()




file = open("ttr.json", "r", encoding="UTF-8")
dct = json.load(file)
print(dct)