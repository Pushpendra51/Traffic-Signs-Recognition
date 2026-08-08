import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy as np
#load the trained model to classify sign
from keras.models import load_model
model = load_model('src/my_model.h5')

#dictionary to label all traffic signs class.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',      
            3:'Speed limit (50km/h)',       
            4:'Speed limit (60km/h)',      
            5:'Speed limit (70km/h)',    
            6:'Speed limit (80km/h)',      
            7:'End of speed limit (80km/h)',     
            8:'Speed limit (100km/h)',    
            9:'Speed limit (120km/h)',     
           10:'No passing',   
           11:'No passing veh over 3.5 tons',     
           12:'Right-of-way at intersection',     
           13:'Priority road',    
           14:'Yield',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Turn right ahead',     
           35:'Turn left ahead',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Roundabout mandatory',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
                 
#INITIALISE GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign Recognition')
top.configure(background='#CDCDCD')

# top = tk.Tk()
# top.geometry('800x600')
# top.title('Traffic Sign Recognition')
# top.configure(background='#F4F6F8')

# label=Label(top,text="🚦Know Your Traffic Sign",background='#F4F6F8', foreground='#1F2937', font=('Arial',19,'bold'))

# label = Label(top, background='#CDCDCD', font=('arial',15,'bold'))
# sign_image = Label(top,bg='#CDCDCD');

header = Frame(top, bg='#CDCDCD')
header.pack(pady=25)

traffic_img = Image.open('traffic_light_image.png')
traffic_img = traffic_img.resize((26, 50))
traffic_img = ImageTk.PhotoImage(traffic_img)
traffic_label = Label(header, image=traffic_img, bg='#CDCDCD')
traffic_label.pack(side=LEFT, padx=10)

label = Label(
    header,
    text="Know Your Traffic Sign",
    bg='#CDCDCD',
    fg='#1F2937',
    font=('Arial', 25, 'bold')
)
label.pack(side=LEFT)


result_label = Label(
    top,
    text="",
    bg='#CDCDCD',
    fg='#1F2937',
    font=('Arial', 20, 'bold')
)
result_label.pack(pady=20)
sign_image = Label(top, bg='#CDCDCD')

def classify(file_path):
    # global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    print(image.shape)
    pred = np.argmax(model.predict(image), axis=1)[0]
    sign = classes[pred+1]
    print(sign)
    result_label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        # uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        uploaded = uploaded.resize((135, 135))
        im=ImageTk.PhotoImage(uploaded)
        
        
        sign_image.configure(image=im)
        sign_image.image=im
        # label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="📤 Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
# label.pack(side=BOTTOM,expand=True)
label.pack(side=LEFT)
# heading = Label(top, text="Know Your Traffic Sign",pady=20, font=('arial',22,'bold'))
# heading.configure(background='#CDCDCD',foreground='#364156')
# heading.pack()
top.mainloop()
