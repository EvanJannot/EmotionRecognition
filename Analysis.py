import json
from deepface import DeepFace
import os

number=1

Name = input("What is the subject's name ?")
path = "D:\\ENSC\\Tohoku\\Experiment\\"+Name
images=[]
listnoms=[]
noms=[]

for file in os.listdir(path):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".png"):
        images.append(filename)

for i in images:
    demography = DeepFace.analyze(path+"\\"+i,actions=['emotion'], detector_backend='mtcnn')
    print(demography)
    demography_json = json.dumps(demography,indent = 1)
    with open(path+'\\'+Name+str(number)+'.json', 'w') as fp:
        json.dump(demography, fp)
    number+=1
    print(demography_json)

data = open(path + '\\' + Name + 'NomImages.json')
for i in data:
    listnoms.append(str(i))

for j in listnoms:
    rep= j.replace("\"","")
    rep = rep.rstrip("\n")
    noms.append(rep)

number=1
for k in noms:
    demography = DeepFace.analyze(k, actions=['emotion'], enforce_detection=False, detector_backend='mtcnn')
    demography_json = json.dumps(demography, indent=1)
    with open(path+'\\'+'Photo'+str(number)+'.json', 'w') as fp:
        json.dump(demography, fp)
    number+=1