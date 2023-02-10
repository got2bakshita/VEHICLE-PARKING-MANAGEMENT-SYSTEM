import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from threading import Thread
import re
global main
main = Tk()
main.title('Vehicle Parking Management System')
main.config(bg = '#177DDC')
main.geometry("700x500")
import time
import pyttsx3
from datetime import date
from datetime import datetime
cur=time.localtime()
current_time=time.strftime("%H:%M%p",cur)
today=date.today()
current_date=today.strftime('%d-%m-%Y')
text_speech = pyttsx3.init()
Vehicle_Number=[]
Vehicle_Type=[]
vehicle_Name=[]
Owner_Name=[]
Date = []
Time = []

# Available Slots
bikes=100
cars=250
bicycles=78

# def inputData

def newWindow():
    b11 = Button(main, text = 'Please select an action to contiue', state=DISABLED, bg= '#49aa19',command=lambda:print("Hello World"), fg = '#fff').grid(row = 3, column = 1, stick = W+E+N+S, pady = 10)
    clicked.set("Select an option :)")

    def handleClick(event):
        global vehNum, vehType, vehName, vehDet, bikes, cars, bicycles
        vehNum = vehicle_number_entry.get().strip()
        vehDet = owner_name_entry.get().strip()
        vehType = vehicle_type_combo.get()
        vehName = vehicle_name_entry.get().strip()

        # pattern = re.compile("^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$")
        # match = pattern.match(vehNum)
        # print(match)
        if is_valid_vehicle_number(vehNum)==False:
            messagebox.showerror("Error", "Invalid vehicle number format")
            return
        
        if vehType=='Bike':
            if bikes>0:
                bikes-=1
                Vehicle_Number.append(vehNum)
                Vehicle_Type.append(vehType)
                vehicle_Name.append(vehName)
                Owner_Name.append(vehDet)
                Date.append(current_date)
                Time.append(current_time)
                messagebox.showinfo("Success", "Data Saved Successfully")
            else:
                messagebox.showerror("Failure", "Sorry, No bike slot available")
        elif vehType=='Car':
            if cars>0:
                cars-=1
                Vehicle_Number.append(vehNum)
                Vehicle_Type.append(vehType)
                vehicle_Name.append(vehName)
                Owner_Name.append(vehDet)
                Date.append(current_date)
                Time.append(current_time)
                messagebox.showinfo("Success", "Data Saved Successfully")
            else:
                messagebox.showerror("Failure", "Sorry, No car slot available")
        elif vehType=='Bicycle':
            if bicycles>0:
                bicycles-=1
                Vehicle_Number.append(vehNum)
                Vehicle_Type.append(vehType)
                vehicle_Name.append(vehName)
                Owner_Name.append(vehDet)
                Date.append(current_date)
                Time.append(current_time)
                messagebox.showinfo("Success", "Data Saved Successfully")
            else:
                messagebox.showerror("Failure", "Sorry, No bicycle slot available")




    # def onFocus(e):
    #     print("WORKING")
    details = Toplevel()
    details.title("Enter Details")
    details.config(bg = "#177DDC" )
    
    labelField = Label(details, text = "Enter the vehicle number: ", font = ("Arial Rounded MT Bold", 14), bg= "#177DDC", fg="#fff")
    labelField.grid(row = 1, column=0)
    vehicle_number_entry = Entry(details, width = 30, font = ("Times New Roman", 15),fg="gray")
    vehicle_number_entry.insert(0,"KA 51 AB 1234")
    vehicle_number_entry.grid(row = 1, column=1)
    vehicle_number_entry.bind("<FocusIn>", on_focus_in)
    vehicle_number_entry.bind("<FocusOut>", on_focus_out)

    labelField4 = Label(details, text = "Enter the owner name: ", font = ("Arial Rounded MT Bold", 14), bg= "#177DDC", fg="#fff")
    labelField4.grid(row = 2, column=0)
    owner_name_entry = Entry(details, width = 30, font = ("Times New Roman", 15))
    owner_name_entry.grid(row = 2, column=1)

    labelField3 = Label(details, text = "Enter the vehicle name: ", font = ("Arial Rounded MT Bold", 14), bg= "#177DDC", fg="#fff")
    labelField3.grid(row = 3, column=0)
    vehicle_name_entry = Entry(details, width = 30, font = ("Times New Roman", 15))
    vehicle_name_entry.grid(row = 3, column=1)

    vehicle_type_label = Label(details, text = "Select the vehicle type: ", font = ("Arial Rounded MT Bold", 14), bg= "#177DDC", fg="#fff")
    vehicle_type_label.grid(row = 4, column=0)
    vehicle_type_combo = ttk.Combobox(details, values=["Bike", "Car", "Bicycle"])
    vehicle_type_combo.current(0)
    vehicle_type_combo.grid(row = 4, column=1)

    # but1 = Button(details, text="Submit", command=handleClick, )
    global but1
    but1 = Button(details, text = 'Submit', bg= '#49aa19', fg = '#fff')
    but1.grid(row = 5, column = 0,  columnspan=2, stick = W+E+N+S, padx = 10, pady=20)
    but1.bind('<Button-1>', handleClick)
    details.mainloop()

global clicked
clicked = StringVar()
clicked.set('Select an action :)')

def showParkedVehicle():
    parked_vehicle_details = ""
    for i in range(len(Vehicle_Number)):
        parked_vehicle_details += "Vehicle Number: " + Vehicle_Number[i] + "\nVehicle Type: " + Vehicle_Type[i] + "\nVehicle Name: " + vehicle_Name[i] + "\nOwner Name: " + Owner_Name[i] + "\nDate: " + Date[i] + "\nTime: " + Time[i] + "\n\n"
    show_vehicle = Toplevel()
    show_vehicle.title("Parked Vehicle Details")
    show_vehicle.config(bg = "#177DDC")
    label = Label(show_vehicle, text = parked_vehicle_details, font  = ('Arial Rounded MT Bold', 14), width = 30, padx = 20, pady = 10 ,bg = '#177DDC', fg = '#fff')
    label.pack()

def removeParkedVehicle():
    remove_vehicle_num = tkinter.simpledialog.askstring("Remove Vehicle", "Enter the vehicle number:", parent=main)
    if remove_vehicle_num in Vehicle_Number:
        index = Vehicle_Number.index(remove_vehicle_num)
        Vehicle_Number.pop(index)
        Vehicle_Type.pop(index)
        vehicle_Name.pop(index)
        Owner_Name.pop(index)
        Date.pop(index)
        Time.pop(index)
        messagebox.showinfo("Success", "Vehicle removed successfully")
    else:
        messagebox.showerror("Failure", "Vehicle Number not found")

def viewLeftSpace():
    messagebox.showinfo("Remaining Parking Space", "Bikes: " + str(bikes) + "\nCars: " + str(cars) + "\nBicycles: " + str(bicycles))

def exitcode(exit):
    text_speech.say("Thank you")
    text_speech.runAndWait()
    exit(0)

def on_focus_in(event):
    if event.widget["state"] == "normal":
        event.widget.delete(0, tkinter.END)
        event.widget["fg"] = "black"
        
def on_focus_out(event):
    if event.widget.get() == "":
        event.widget.insert(0, "KA 51 AB 1234")
        event.widget["fg"] = "gray"


def is_valid_vehicle_number(number):
    pattern = re.compile(r"^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$")
    print(number,bool(pattern.match(number)))
    return bool(pattern.match(number))

def generate_bill():
    global Vehicle_Number, Vehicle_Type, vehicle_Name, Owner_Name, Date, Time
    bill_window = Toplevel()
    bill_window.title("Generate Bill")
    bill_window.config(bg = "#177DDC")

    bill_number_label = Label(bill_window, text = "Enter the Vehicle Number: ", font = ("Arial Rounded MT Bold", 14), bg= "#177DDC", fg="#fff")
    bill_number_label.grid(row = 0, column = 0)
    bill_number_entry = Entry(bill_window, width = 30, font = ("Times New Roman", 15))
    bill_number_entry.grid(row = 0, column = 1)

    def get_bill():
        bill_num = bill_number_entry.get().strip()
        if bill_num in Vehicle_Number:
            index = Vehicle_Number.index(bill_num)
            vehicle_type = Vehicle_Type[index]
            if vehicle_type == 'Bike':
                charge = 50
            elif vehicle_type == 'Car':
                charge = 100
            else:
                charge = 20
            
            bill_details = "Vehicle Number: " + bill_num + "\n"
            bill_details += "Vehicle Type: " + vehicle_type + "\n"
            bill_details += "Vehicle Name: " + vehicle_Name[index] + "\n"
            bill_details += "Owner Name: " + Owner_Name[index] + "\n"
            bill_details += "Date: " + Date[index] + "\n"
            bill_details += "Time: " + Time[index] + "\n"
            bill_details += "Charge: " + str(charge) + " INR"

            bill_text = Text(bill_window, height = 10, width = 50)
            bill_text.insert(END, bill_details)
            bill_text.grid(row = 2, column = 0, columnspan = 2)
        else:
            messagebox.showerror("Error", "Invalid Vehicle Number")

    generate_bill_button = Button(bill_window, text = "Generate Bill", font = ("Arial Rounded MT Bold", 14), bg = "#49aa19", fg = "#fff", command = get_bill)
    generate_bill_button.grid(row = 1, column = 0, columnspan = 2, pady = 10)


def checkInput(e):
    global b11
    if e == 'Vehicle Entry':
        b11 = Button(main, text = 'Continue', command = newWindow, bg = '#49aa19', fg = '#fff').grid(row = 3, column = 1, stick = W+E+N+S, pady = 10)
    elif e ==  'Remove Entry':
        b11 = Button(main, text = 'Continue', command = removeParkedVehicle, bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady = 10)
    elif e ==  'View parked vehicles':
        b11 = Button(main, text = 'Continue', command = showParkedVehicle, bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady=10)
    elif e ==  'View left parking space':
        b11 = Button(main, text = 'Continue', command = viewLeftSpace, bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady = 10)
    # elif e ==  'Amount details':
    #     b11 = Button(main, text = 'Continue', command = generate_bill, bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady = 10)
    elif e ==  "Bill":
        b11 = Button(main, text = 'Continue', command = generate_bill, bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady = 10)
    elif e ==  "Close Program":
        b11 = Button(main, text = 'Continue', command = lambda: exitcode(exit), bg = '#49aa19', fg = '#fff').grid(row =3, column = 1, stick = W+E+N+S, pady = 10)
    else:
        b11 = Button(main, text = 'Please select an action to contiue', state = DISABLED, bg = '#49aa19', fg = '#fff').grid(row = 3, column = 1, stick = W+E+N+S, pady = 10)
    
    text_speech.say(e);
    text_speech.runAndWait();

lab1 = Label(main, text = 'Vehicle Parking Management System', font  = ('Arial Rounded MT Bold', 22), width = 30, padx = 20, pady = 10 ,bg = '#177DDC', fg = '#fff').grid(row = 0, column = 0, pady = 5, columnspan=2)
lab2 = Label(main, text = 'AMOUNT DETAILS 1.BIKE-50 INR\n2.CAR-200 INR\n3.BICYCLE-20 INR', font =('Times New Roman', 10), relief = 'sunken', justify = 'right', width = 35, borderwidth  = 0, bg = '#177DDC', fg = '#fff').grid(row = 1, column = 0, stick = W, columnspan=2)
drop = OptionMenu(main, clicked, "Vehicle Entry", "Remove Entry", "View parked vehicles", "View left parking space","Bill","Close Program", command=checkInput)
drop.config(bg = '#49aa19', fg = '#fff', borderwidth=0, border=0)
drop.grid(row = 2, column = 0,columnspan=2, pady=15)
b11 = Button(main, text = 'Please select an action to contiue', state=DISABLED, bg= '#49aa19',command=lambda:print("Hello World"), fg = '#fff').grid(row = 3, column = 1, stick = W+E+N+S, pady = 10)
text_speech.say("Welcome to our service")
text_speech.runAndWait()
main.mainloop()