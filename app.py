import tkinter as tk

HEIGHT = 300
WIDTH = 600




def newLocation():
    
    top = tk.Toplevel()
    

    entry = tk.Entry(top, bg='white')
    entry.grid(row=0, column=0)
    nLocation = tk.Button(top,bg='gray', text='add location', command=lambda: dataList(entry.get(),top))
    nLocation.grid(row=0, column=1)
    top.mainloop()


def dataList(text,top):
    print("Info was stored: %s", text)
    #use geonames for finding long, lat and insert that with the yr data
    #http://www.geonames.org/export/geonames-search.html
    #http://api.geonames.org/search?q=london&maxRows=10&username=demo
    #http://www.geonames.org/export/geonames-search.html

    #need accounts for both
    top.destroy()

#Main app start
root = tk.Tk()






canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()

#frame = tk.Frame(root, bg='gray')
#frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

btn_container = tk.Frame(root)
btn_container.place( relx=0.90, rely=0, relwidth=0.1, relheight=1)

weather_container = tk.Frame(root, bg='yellow')
weather_container.place(relx=0, rely = 0, relwidth=0.85,relheight=1)

#photoImage
icon_update = tk.PhotoImage(file='./icons/update.png')
icon_add = tk.PhotoImage(file='./icons/add.png')
button_update = tk.Button(btn_container, text="Update", bg='#80c1ff',image= icon_update)

button_update.grid(row=0, column=0)

button_add = tk.Button(btn_container, text="Add Location", bg='#80c1ff', image=icon_add, command=newLocation)

button_add.grid(row=1, column=0)

label = tk.Label(weather_container, text="This is temp", bg='pink')
label.place(relx=0, rely=0, relwidth=0.2, relheight=1)

label = tk.Label(weather_container, text="This icon", bg='purple')
label.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)

label = tk.Label(weather_container, text="This is the location", bg='blue')
label.place(relx=0.4, rely=0, relwidth=.6, relheight=1)


root.mainloop()
#Main app end