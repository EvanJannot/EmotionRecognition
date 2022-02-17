import collections
import os, random, json
import PIL.Image
import PIL.ImageTk
import winsound
from tkinter import *

Name = input("What is the subject's name ?")
directory = Name
path = "D:\\ENSC\\Tohoku\\Experiment\\"+Name
duration=3000
number = 0 #Tell what photo to display
j=0
list_img = {} #Images à afficher
items = list_img.items()
noms_images = []
feelings = ("angry", "disgust", "happy", "neutral", "sad", "scared", "surprise") #Feeling to test

window = Tk()
window.title(number+1)
window.geometry("900x900")

def MakeJson(list_img):
    global Name
    with open(path+'\\'+Name+'ListImages.json', 'a') as fp:
        for j in list_img:
            list1_json = json.dumps(list_img[j], indent=2)
            json.dump(list_img[j], fp, indent=2)
            fp.write('\n')
    print(list1_json)

def JsonImages(noms_images,list_img):
    global Name
    indice=0
    for key in list_img.keys():
        emotion = list_img[items[indice][0]]
        noms_images.append("D:\\ENSC\\Tohoku\\Experiment\\"+emotion+"\\"+key)
        indice+=1
    with open(path+'\\'+Name+'NomImages.json', 'a') as fp:
        for j in noms_images:
            list1_json = json.dumps(j, indent=2)
            json.dump(j, fp, indent=2)
            fp.write('\n')
    print(list1_json)


def CreateWindow(): #Create a new window
    global window
    window = Tk()
    window.title(number+1)
    window.geometry("900x900")

def NewPhoto(): #We choose the new picture
    global number
    i=0
    for key in list_img.keys():
        if number == i :
            photo = key
            return photo
        else :
            i+=1


def changePhoto(): #Change the picture every x seconds
    global number
    global photo_displayed
    global window
    slides = []
    if number < len(list_img): #Stop when all the photos have been displayed
        emotion = list_img[items[number][0]] #Define the new picture that is displayed
        path = "D:\\ENSC\\Tohoku\\Experiment\\"+emotion+"\\"+photo_displayed
        image = PIL.Image.open(path)
        resized_image = image.resize((900, 900))
        if number != 0:
            window.destroy()
            CreateWindow()
        photo = PIL.ImageTk.PhotoImage(resized_image)
        label = Label(image=photo)
        label.image = photo
        label.pack()
        slides.append(photo)
        number+=1
        photo_displayed=NewPhoto()
        return slides
    else:
        number+=1
        return

def slideshow(): #Display the picture
    global number
    global list_img
    global duration
    winsound.Beep(560,1000)
    slides = changePhoto()
    if number < 36:
        window.after(duration, slideshow)
    else:
        window.destroy()

def Melange():
    global list_img
    global photo_displayed
    global items
    global nlist
    items = list_img.items() #We shuffle the pictures
    items = list(items)
    random.shuffle(items)
    list_img = collections.OrderedDict(items)
    MakeJson(list_img)
    for key in list_img.keys(): #We define the first picture to display
        photo_displayed= key
        break

for i in (feelings): #We select randomly te pictures among the repertories and clasify them inside a dictionary
    for j in range (0,5,1):
        img = random.choice(os.listdir("D:\\ENSC\\Tohoku\\Experiment\\"+i))
        list_img[img]=i
        j+=1

Melange()
JsonImages(noms_images,list_img)
print(list_img)
slideshow()
window.mainloop()
