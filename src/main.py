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
    data = []
    THERSHOLD = 1000000
    counter = 0
    for single_raw_data in raw_data:
        if counter <= THERSHOLD:
            if counter == 42:
                print(single_raw_data)
            data.append(json.loads(single_raw_data))
            counter += 1
        else:
            break

    print(data[42])


if __name__ == "__main__":
    main()
