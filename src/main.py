import os
import json

def init()->str:
    TARGET_PATH = input("Pls paste file path: ")
    TARGET_PATH = (
        TARGET_PATH[1:-1]
        if (TARGET_PATH[0] == '"' and TARGET_PATH[-1] == '"')
        else TARGET_PATH
    )
    # print(TARGET_PATH)
    print("\n"+"="*10+" END "+"="*10)

    return TARGET_PATH


def main(TARGET_PATH:str):
    with open(TARGET_PATH, "r", encoding="utf-8") as f:
        raw_data = list(filter(bool, f.read().split("\n")))
    raw_json = []
    THERSHOLD = 1000000
    counter = 0
    for single_raw_data in raw_data:
        if counter <= THERSHOLD:
            raw_json.append(json.loads(single_raw_data))
            counter += 1
        else:
            break

    data = []
    for single_raw_json in raw_json:
        temp_dict = {
            **{"coordinates": single_raw_json["geometry"]["coordinates"]},
            **single_raw_json["properties"],
        }

        data.append(
            {
                "id": temp_dict["id"],
                "postcode": temp_dict["postcode"],
                "region": temp_dict["region"],
                "district": temp_dict["district"],
                "city": temp_dict["city"],
                "street": temp_dict["street"],
                "number": temp_dict["number"],
                "unit": temp_dict["unit"],
                "coordinates": {
                    "lon": temp_dict["coordinates"][0],
                    "lat": temp_dict["coordinates"][1],
                },
            }
        )

    # from pprint import pprint
    # pprint(data[42])

    OUTPUT_TARGET="string" # string or osm

    str_buffer=[]
    for single_data in data:
        string=single_data["id"]+single_data["postcode"]+single_data["region"]+single_data["district"]+single_data["city"]+single_data["street"]+single_data["number"]+single_data["unit"] #+"("+single_data["coordinates"]["lon"]+","+single_data["coordinates"]["lat"]+")"
        str_buffer.append(string)
    with open(os.path.dirname(TARGET_PATH)+TARGET_PATH.replace(os.path.dirname(TARGET_PATH),"").replace(".geojson",".txt"),"w",encoding="utf-8") as f:
        f.write("\n".join(str_buffer))

    print("\n"+"="*10+"FINAL"+"="*10)

if __name__ == "__main__":
    main(init())
