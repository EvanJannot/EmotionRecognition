import json

Name = input("What is the subject's name ?")
path = "D:\\ENSC\\Tohoku\\Experiment\\"+Name

#Read json files
list1=[]
listObs=[]

#List with data cleaned
listImages1=[]
subject1=[]
noms=[]



def ExtractData(path,Name):
    global list1
    data1 = open(path + '\\' + Name + 'ListImages.json')
    for i in data1:
        list1.append(str(i))


def CleanDataPhoto():
    global list1, listImages1
    for j in list1:
        rep= j.replace("\"","")
        rep = rep.rstrip("\n")
        listImages1.append(rep)


def CleanDataObserver(path, Name):
    global noms
    for i in range(1, 36):
        with open(path + '\\' + Name + str(i) + '.json') as fp:
            dataObs = json.load(fp)
            dataStr = str(dataObs)
            # Balises
            pos1 = dataStr.find('\'dominant_emotion\': \'')
            pos2 = dataStr.find('\', \'region\'')
            emotion = dataStr[pos1 + 21:pos2]
            print(emotion)
            subject1.append(emotion)

def CleanDataNoms(path):
    global subject1, subject2
    for i in range(1, 36):
        with open(path + '\\' + 'Photo' + str(i) + '.json') as fp:
            dataNoms = json.load(fp)
            NomsStr = str(dataNoms)
            # Balises
            pos1 = NomsStr.find('\'dominant_emotion\': \'')
            pos2 = NomsStr.find('\', \'region\'')
            emotion = NomsStr[pos1 + 21:pos2]
            noms.append(emotion)


def CompareData(listImage, Observer):
    diff=0
    for i in range(0, len(listImage)):
        if listImage[i] != Observer[i]:
            diff+=1
            if listImage[i] =="scared" and Observer[i]=="fear":
                diff-=1
    return diff


def Percentage(diff):
    perc= 100-(diff/35)*100
    return perc


ExtractData(path,Name)
CleanDataPhoto()
CleanDataObserver(path, Name)
CleanDataNoms(path)
print(noms)
diff=CompareData(listImages1,noms)
rate=Percentage(diff)
diff1=CompareData(listImages1,subject1)
rate1=Percentage(diff1)
print("Percentage of correct DeepFace predictions from the displayed original photos: "+ str(rate) + "%")
print("Percentage of correct DeepFace predictions from the observer's face: "+ str(rate1)+ "%")