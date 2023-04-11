# import pdb

# if input("test input work in db: ") == "yes":
#     print("Niceee")

import os


def remove_ir():
    """
    Removes all of the infrared data files from the VEDAI dataset
    """
    IMG_DIR = "C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\images\\"
    img_names = os.listdir(IMG_DIR)
    # print(img_names)
    
    for name in img_names:
        if "ir" in name:
            print("hollup bish" + f": {name}")
            os.remove(IMG_DIR + name)
        new_name = name.replace("_co", "")
        os.rename(f"{IMG_DIR}{name}", f"{IMG_DIR}{new_name}")

def add_path_fold():
    IMG_DIR = "C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\images\\"
    img_names = os.listdir(IMG_DIR)

    with open("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\fold01.txt", "r") as f:
        contents = f.readlines()
        for c, file in enumerate(contents):
            contents[c] = "C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\images\\" + contents[c]

    with open("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\fold01_w.txt", "w") as f:
        for line in contents:
            f.write(line)
    
    print("Done")

add_path_fold()

# print(os.listdir("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\images"))

    