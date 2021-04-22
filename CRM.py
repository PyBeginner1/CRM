from tkinter import *
#for treeview we're using ttk
from tkinter import ttk

root= Tk()
root.title("CRM DB")
root.geometry('1000x500')

#add style
style=ttk.Style()
#pick a theme
style.theme_use('default')

#configure treeview colours
style.configure("Treeview", bg = 'black', fg='#D3D3D3', rowheight=25, fieldbackground='#D3D3D3')

#change colour of items we click
style.map("Treeview", background =[('selected','#EC5E3D')])

#create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

#create scrollbar in frame
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)    #fill moves scroll in Y axis

#create Treeview
my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
my_tree.pack()

#configure scroll bar
tree_scroll.config(command=my_tree.yview)

#create columns
my_tree['columns']=('First Name', 'Last Name', 'Age', 'Address', 'City', 'State','Zipcode')

#format columns
my_tree.column('#0', stretch=NO, width=0)           #without this column wont come out properly
my_tree.column('First Name', width=140)
my_tree.column('Last Name', width=140)
my_tree.column('Age', width=100)
my_tree.column('Address', width=140)
my_tree.column('City', width=140)
my_tree.column('State', width=140)
my_tree.column('Zipcode', width=140)

#create heading now, above we successfully created frame with columns
my_tree.heading('#0', text='')
my_tree.heading('First Name', text='First Name', anchor =W)      #anchor is the place where u put text, with W text will be placed at left corner
my_tree.heading('Last Name', text='Last Name',anchor =W)
my_tree.heading('Age', text='Age',anchor=CENTER)
my_tree.heading('Address', text='Address',anchor=CENTER)
my_tree.heading('City', text='City',anchor=CENTER)
my_tree.heading('State', text='State',anchor=CENTER)
my_tree.heading('Zipcode', text='Zipcode',anchor=CENTER)

#add fake data into frame
data =[
    ["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
    ["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
    ["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
    ["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
    ["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
    ["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
    ["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
    ["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
    ["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
    ["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
    ["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
    ["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
    ["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
    ["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
    ["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
    ["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
    ["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
    ["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
    ["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
    ["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
]

#create striped rows
my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')

#add data
global count
count =0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values =(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='',
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                       tags=('oddrow',))
    count += 1

#add record entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label =Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10,pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10,pady=10)

ln_label =Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10,pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10,pady=10)

age_label =Label(data_frame, text="Age")
age_label.grid(row=0, column=4, padx=10,pady=10)
age_entry = Entry(data_frame)
age_entry.grid(row=0, column=5, padx=10,pady=10)

add_label =Label(data_frame, text="Address")
add_label.grid(row=1, column=0, padx=10,pady=10)
add_entry = Entry(data_frame)
add_entry.grid(row=1, column=1, padx=10,pady=10)

city_label =Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10,pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10,pady=10)

state_label =Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10,pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10,pady=10)

zipcode_label =Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=10,pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10,pady=10)


#update record
def update_record():
    #grab the record
    selected=my_tree.focus()
    #update that record
    my_tree.item(selected, text='', values=(fn_entry.get(),ln_entry.get(),age_entry.get(),add_entry.get(),city_entry.get(),state_entry.get(),zipcode_entry.get()))

    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    age_entry.delete(0, END)
    add_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


#move up the record
def move_up():
    rows=my_tree.selection()        #selection-whatever row is selected
    for row in rows:
        my_tree.move(row, my_tree.parent(row),my_tree.index(row)-1)

#move down the record
def move_down():
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)


#remove 1 record
def remove_one():
    x=my_tree.selection()[0]            #call the 0th item
    my_tree.delete(x)


#remove many records
def remove_many():
    x=my_tree.selection()
    for record in x:
        my_tree.delete(record)


#remove all  records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


#Select Record
def select_record(e):       #e is for the event that we created by binding with <ButtonRelease-1>
    #first we empty the entry boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0, END)
    age_entry.delete(0, END)
    add_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    #record the number we click
    selected=my_tree.focus()
    #grab the record values
    values=my_tree.item(selected,'values')      #values from the for loop above

    #input the values into entry frame
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    age_entry.insert(0, values[2])
    add_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])


#clear entry boxes
def clear_entries():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    age_entry.delete(0, END)
    add_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)



#create buttons
button_frame=LabelFrame(root, text="Commands")
button_frame.pack(fill='x', expand='yes',padx=20)

update_button = Button(button_frame, text="Update Record",command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button=Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button=Button(button_frame, text="Remove all Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button=Button(button_frame, text="Remove one record",command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button=Button(button_frame, text="Remove many records",command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button=Button(button_frame, text="Move Up",command=move_up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button=Button(button_frame, text="Move Down",command=move_down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_button=Button(button_frame, text="Clear Entry Boxes",command=clear_entries)
select_button.grid(row=0, column=7, padx=10, pady=10)

#bind treeview
my_tree.bind("<<TreeviewSelect>>",select_record)        #seelect a row &display contents by a click.Virtual Event




root.mainloop()

