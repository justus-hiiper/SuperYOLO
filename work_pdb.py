import os

import regex as re


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

def fold_to_100_VEDAI():
    """
    This function removes all of the pathnames from fold01_w.txt that have an image number higher than 100
    """
    with open("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI1\\VEDAI\\fold01_w.txt", "r") as f:
        file = f.readlines()
        with open("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI1\\VEDAI\\fold01_w2.txt", "w") as f2:
            for i in file:
                i_copy = i[:-1] #remove \n
                i_copy = i_copy.split("\\")
                if int(i_copy[-1]) <= 100:
                    f2.write(i)

# print(os.listdir("C:\\Users\\gsvpk\\VScode\\Own_Projects\\SuperYOLO\\data\\VEDAI\\images"))

    