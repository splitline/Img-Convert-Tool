import os
import json
from PIL import Image
import codecs

def listDir(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        print("[dir] " + root)
        for f in files:
            if f == "texture.png":
                print ("[file] " + os.path.join(root, f))
                img = Image.open(root + "/texture.png")
                with codecs.open(root + "/texture.json", 'r', 'utf-8-sig') as data_file:
                    data = json.load(data_file)
                    for i in range(len(data["SubTexture"])):
                        crop_img = img.crop((data["SubTexture"][i]["x"], data["SubTexture"][i]["y"], data["SubTexture"][i]["x"]+data["SubTexture"][i]["width"], data["SubTexture"][i]["y"]+data["SubTexture"][i]["height"]))
                        file_name = data["SubTexture"][i]["name"]
                        crop_img.save(root + "/" + file_name[file_name.rfind('/'):], "PNG")
listDir("./")
