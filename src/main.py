import os
import json

TARGET_PATH = input("Pls paste file path: ")
TARGET_PATH = (
    TARGET_PATH[1:-1]
    if (TARGET_PATH[0] == '"' and TARGET_PATH[-1] == '"')
    else TARGET_PATH
)


def main():
    # print(TARGET_PATH)

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
    
    data=[]
    for single_raw_json in raw_json:
        temp_dict={**{
            "coordinates":single_raw_json["geometry"]["coordinates"]
        },**single_raw_json["properties"]}

        data.append({
            "id":temp_dict["coordinates"],
            "postcode":temp_dict["postcode"],
            "region":temp_dict["region"],
            "district":temp_dict["district"],
            "city":temp_dict["city"],"street":temp_dict["street"],
            "number":temp_dict["number"],
            
            "unit":temp_dict["unit"],
            "coordinates":{
                "lon":temp_dict["coordinates"][0],"lat":temp_dict["coordinates"][1]
            }
        })

    print(data[42])

    



if __name__ == "__main__":
    main()
