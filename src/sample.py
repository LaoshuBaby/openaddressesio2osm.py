import os

with open("openaddressesio.jp.tokyo.geojson", "r", encoding="utf-8") as f:
    content = f.read().split("\n")

data = []


for i in range(len(content)):
    if i % 100 == 0:
        data.append(content[i])

with open("lite.geojson", "w", encoding="utf-8") as f:
    f.write("\n".join(data))
