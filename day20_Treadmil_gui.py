import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk  
from PIL import ImageTk,Image

data=pd.read_csv('treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title('Treadmil Users Analysis')

graphs = ttk.Variable(app)
values ={
    'Pair Plot':'sns.pairplot(data=data)',
    'Joint Plot':"sns.jointplot(data = data, x='{col1}', y ='{col2}')",
    'Bar Plot': "sns.barplot(data=  data, x='{col1}',y='{col2}')"
}
graphs.set(values['Pair Plot'])
y = 10
for key, value in values.items():
    ttk.Radiobutton(app, text = key,variable=graphs, value =value).place(x =10,y=y)
    y+=20
##Option Menu 1
col1 = ttk.Variable(app)
values = ['Select']+list(data.columns)
col1.set(values[0])  
ttk.Label(app,text = 'Column 1').place(x =100,y=10)  
ttk.OptionMenu(app, col1,*values ).place(x=100,y=40)

#Option Menu 2
col2 = ttk.Variable(app)
col2.set(values[0])  
ttk.Label(app,text = 'Column 2').place(x =150,y=80)  
ttk.OptionMenu(app, col1,*values).place(x=150,y=110)

#Option Menu 3
col3 = ttk.Variable(app)
col3.set(values[0])  
ttk.Label(app,text = 'Column 3').place(x =150,y=150)  
ttk.OptionMenu(app, col1,*values).place(x=150,y=180)

#Canvas
cnv = ttk.Canvas(app, width=250, height=200)
cnv.place(x=300,y=60)

def show():
    global img
    global cnv


    column1=col1.get()
    column2=col2.get()
    column3=col3.get()

    fig = plt.figure(figsize=(5,2))
    eval(graphs.get().format(col1=column1,col2=column2,col3=column3))
    fig.savefig('graph.png')
    img = ImageTk.PhotoImage(Image.open('graph.png').resize((250,200))
    )

    global cnv
    cnv.create_image(0,0,anchor = ttk.NW, image = img)
   # plt.show()
    #print(col1.get())
    #print(col2.get())
    #print(col3.get())


ttk.Button(app, text='Show',command= show).place(x=400,y=10)        

app.mainloop()