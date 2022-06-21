from sqlite3 import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt


# TO OPEN THE ADD WINDOW AND WITHDRAW(CLOSE) THE MAIN WINDOW

def f1():
	add_window.deiconify()
	main_window.withdraw()

# TO GO BACK FROM ADD WINDOW TO MAIN WINDOW
	
def f2():
	main_window.deiconify()
	add_window.withdraw()

# TO ENTER DATA IN DATABASE

def f3():
	con = None
	try:
		con = connect("Jv.db")
		cursor = con.cursor()
		sql = "insert into employee values ('%d','%s','%f')"
		if len(aw_ent_id.get()) != 0:
			id = int(aw_ent_id.get())
			if id == int(aw_ent_id.get()):
				if id > 0:
					if len(aw_ent_name.get()) != 0:
						name = aw_ent_name.get()
						if name.isalpha():
							if len(name) >= 2:

								try:
									if len(aw_ent_salary.get()):
										salary = float(aw_ent_salary.get())
										if salary > 0:
											if salary >= 8000:
												cursor.execute(sql %(id, name, salary))
												con.commit()
												showinfo("Succes", "Record Added")
												aw_ent_id.delete(0, END)
												aw_ent_name.delete(0, END)
												aw_ent_salary.delete(0, END)
												aw_ent_id.focus()
											else:
												showerror("Salary Error","Salary should be Minimum 8000")
										else:
											showerror("Salary Error","Salary should be a Positive Number")
									else:
										showerror("Salary Error", "Salary should not be empty")
								except ValueError:
									showerror("Salary Error","Salary should be number only, not letter")
									con.rollback()

								finally:
									if con is not None:
										con.close
							else:
								showerror("Name Error", "Minimum two char are required for name")
						else:
							showerror("Name Error", "Name should required letter only")
					else:
						showerror("Name Error", "Name should not be empty")
				else:
					showerror("ID Error", "Enter Valid ID ")
			else:
				showerror("ID Error", "ID should not be empty")
		else:
			showerror("ID error", "Same ID")

	except ValueError:
		showerror("ID Error", "Check ID, it should be number only")
		con.rollback()
	except IntegrityError:
		showerror("ID Error", "Id alredy exists")
	except Exception as e:
		showerror("Insertion Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

	

# TO OPEN VIEW WINDOW AND WITHDRAW THE MAIN WINDOW
	
def f4():
	view_window.deiconify()
	main_window.withdraw()
	vw_em_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect("Jv.db")
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " id : " + str(d[0]) + " | name : " + str(d[1]) + " | salary: " + str(d[2]) + "\n"
		vw_em_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()

# TO GO BACK TO MAIN WINDOW FROM THE VIEW  

def f5():
	main_window.deiconify()
	view_window.withdraw()

# TO OPEN UPDATE WINDOW AND WITHDRAW FROM MAIN WINDOW

def f6():
	update_window.deiconify()
	main_window.withdraw()

# TO GO BACK TO MAIN WINDOW FROM UPDATE WINDOW
	
def f7():
	main_window.deiconify()
	update_window.withdraw()

# TO UPDATE THE DATA

def f8():
	con = None
	try:
		con = connect("Jv.db")
		cursor = con.cursor()
		sql="update employee set name = '%s', salary = '%f' where id = '%d' "
		if len(uw_ent_id.get()) != 0:
			id = int(uw_ent_id.get())
			if id > 0:
				if len(uw_ent_name.get()) != 0:
					name=uw_ent_name.get()
					if name.isalpha():
						if len(name) >= 2:

							try:
								if len(uw_ent_salary.get()):
									salary = float(uw_ent_salary.get())
									if salary > 0:
										if salary >= 8000:
											cursor.execute(sql %(name, salary, id))
											if cursor.rowcount == 1:
												con.commit()
												showinfo("Success", "Record Updated")
											else:
												showerror("Failure", " Failed To Update record")

											uw_ent_id.delete(0, END)
											uw_ent_name.delete(0, END)
											uw_ent_salary.delete(0, END)
											uw_ent_id.focus()
										else:
											showerror("Salary Error","Salary should be Minimum 8000")
									else:
										showerror("Salary Error","Salary should be a Positive Number")
								else:
									showerror("Salary Error", "Salary should not be empty")
							except ValueError:
								showerror("Salary Error","Salary should be number only, not letter")
								con.rollback()

							finally:
								if con is not None:
									con.close
						else:
							showerror("Name Error", "Minimum two char are required for Name")
					else:
						showerror("Name Error", "Name should required letter only")
				else:
					showerror("Name Error", "Name should not be empty")
			else:
				showerror("ID Error", "Enter Valid ID ")
		else:
			showerror("ID Error", "ID should not be empty")

	except ValueError:
		showerror("ID Error", "Check ID, it should be number only")
		con.rollback()
	except Exception as e:
		showerror("ID error","Employee Id already exists",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

# TO OPEN DELETE WINDOW AND WITHDRAW THE MAIN WINDOW

def f9():
	delete_window.deiconify()
	main_window.withdraw()

# TO GO BACK TO MAIN WINDOW FROM THE DELETE WINDOW
	
def f10():
	main_window.deiconify()
	delete_window.withdraw()

# TO DELETE THE DATA

def f11():
	con = None
	try:
		con = connect("Jv.db")
		cursor = con.cursor()
		sql = "delete from employee where id='%d'"
		if len(dw_ent_id.get()) != 0:
			id = int(dw_ent_id.get())
			cursor.execute(sql % (id) )
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success", "Record deleted")
				dw_ent_id.delete(0, END)
				dw_ent_id.focus()
			else:
				showerror("failure", "Record does not exists")
		else:
			print(id, "does not exists")
	except ValueError:
		showerror("IDError", "One id at a time")
		con.rollback()
	except Exception as e:
		print("issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("closed")

# TO PLOT THE GRAPH

def f12():
	con = None
	try:
		con = connect("Jv.db")
		cursor = con.cursor()
		data = pd.read_sql_query("select name, salary from employee",con)
		employee = data['name'].tolist()
		salary = data['salary'].tolist()

		res = {}
		for key in employee:
			for value in salary:
				res[key] = value
				salary.remove(value)
				break
		sort_order = sorted(res.items(), key=lambda x:x[1], reverse=True)
		max = sort_order[0:5]

		a,b = [],[]
		for i in max:
			a.append(i[0])
			b.append(i[1])

		employee = a
		salary = b

		plt.bar(employee, salary, width = 0.5, color=["red","green","yellow","blue","orange"])
		plt.xlabel("Employee")
		plt.ylabel("Salary")
		plt.grid()
		plt.title("Top Five Highest Earning Salary Employee")
		plt.show()
	except Exception as e:
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()

# MAIN WINDOW

main_window = Tk()
main_window.title("Employee Management System")
main_window.geometry("500x500+100+100")
main_window["background"] = "#B9D9EB"

bg = "bg_color"
f = ("Franklin Gothic", 15, "bold")
q = ("Franklin Gothic", 12, "bold", "italic")

# CODE FOR QUOTE

try:
	wa = "https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(wa)
	data = bs4.BeautifulSoup(res.text, "html.parser")
	info = data.find("img", {"class":"p-qotd"})
	quote = info["alt"]
	print("QOTD = ", quote)
except Exception as e:
	print("issue", e)

mw_btn_add = Button(main_window, text="Add", font=f, width=10, bg="#B9D9EB", command=f1)
mw_btn_view = Button(main_window, text="View", font=f, width=10, bg="#B9D9EB", command=f4)
mw_btn_update = Button(main_window, text="Update", font=f, width=10, bg="#B9D9EB", command=f6)
mw_btn_delete = Button(main_window, text="Delete", font=f, width=10, bg="#B9D9EB", command=f9)
mw_btn_chart = Button(main_window, text="Chart", font=f, width=10, bg="#B9D9EB", command=f12)
mw_lab_qotd = Label(main_window, text="QOTD", bg="#B9D9EB", width = 450, font=q, borderwidth=2, relief='solid')

mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_chart.pack(pady=10)
mw_lab_qotd.pack(pady=10)


# ADD WINDOW

add_window = Toplevel(main_window)
add_window.title("Add Em.")
add_window.geometry("500x500+100+100")
add_window["background"] = "#8FBC8F"
add_window.withdraw()

aw_lbl_id = Label(add_window, text="Enter Id:", font=f, bg="#8FBC8F")
aw_ent_id = Entry(add_window, font=f, bd=2)
aw_lbl_name = Label(add_window, text="Enter Name:", font=f, bg="#8FBC8F")
aw_ent_name = Entry(add_window, font=f, bd=2)
aw_lbl_salary = Label(add_window, text="Enter Salary:", font=f, bg="#8FBC8F")
aw_ent_salary = Entry(add_window, font=f, bd=2)
aw_btn_save = Button(add_window, text="Save", font=f, bg="#8FBC8F", command=f3)
aw_btn_back = Button(add_window, text="Back", font=f, bg="#8FBC8F", command=f2)

aw_lbl_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lbl_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lbl_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)

# VIEW WINDOW

view_window = Toplevel(main_window)
view_window.title("View Em.")
view_window.geometry("500x500+100+100")
view_window["background"] = "#F7E7CE"
view_window.withdraw()

vw_em_data = ScrolledText(view_window, width=40, height=18, font=f, bg="#F7E7CE")
vw_btn_back = Button(view_window, text="Back", font=f, bg="#F7E7CE", command=f5)
vw_em_data.pack(pady=10)
vw_btn_back.pack(pady=10)

# UPDATE WINDOW

update_window = Toplevel(main_window)
update_window.title("Update Em.")
update_window.geometry("500x500+100+100")
update_window["background"] = "#FFB7C5"
update_window.withdraw()

uw_lbl_id = Label(update_window, text="Enter Id to be updated:", font=f, bg="#FFB7C5")
uw_ent_id = Entry(update_window, font=f, bd=2)
uw_lbl_name = Label(update_window, text="Enter name:", font=f, bg="#FFB7C5")
uw_ent_name = Entry(update_window, font=f, bd=2)
uw_lbl_salary = Label(update_window, text="Enter Salary:", font=f, bg="#FFB7C5")
uw_ent_salary = Entry(update_window, font=f, bd=2)
uw_btn_save = Button(update_window, text="Save", font=f, bg="#FFB7C5", command=f8)
uw_btn_back = Button(update_window, text="Back", font=f, bg="#FFB7C5", command=f7)

uw_lbl_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lbl_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lbl_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)

# DELETE WINDOW

delete_window = Toplevel(main_window)
delete_window.title("Delete Em.")
delete_window.geometry("500x500+100+100")
delete_window["background"] = "#6D9BC3"
delete_window.withdraw()

dw_lbl_id = Label(delete_window, text="Enter Id to be deleted:", font=f, bg="#6D9BC3")
dw_ent_id = Entry(delete_window, font=f, bd=2)
dw_btn_delete = Button(delete_window, text="Delete", font=f, bg="#6D9BC3", command=f11)
dw_btn_back = Button(delete_window, text="Back", font=f, bg="#6D9BC3", command=f10)

dw_lbl_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_delete.pack(pady=10)
dw_btn_back.pack(pady=10)

main_window.mainloop()
