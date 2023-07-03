from tkinter import *
from tkinter import messagebox

window=Tk()

window.title("BMI calculator")
window.minsize(width=400,height=400)
window.config(padx=10,pady=10)

#label
lbl1=Label(text="Enter your weight(kg)")
lbl1.config(fg="black")
lbl1.place(x=140 ,y=10)

#entry
myentry=Entry(width=20)
myentry.place(x=140,y=40)

#label2
lbl2=Label(text="Enter your height(cm)")
lbl2.place(x=140,y=70)

#entry2
entry2=Entry(width=20)
entry2.place(x=140,y=100)

#def button
def clickbutton():
    ans = myentry.get()
    ans2 = entry2.get()

    try:
        ans = int(ans)
        ans2 = int(ans2)
        solve = ans / (ans2 / 100)**2
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
        return
    else:
        if solve <= 19:
            res="your bmi is"+str(solve)+"\n underweight"
            messagebox.showinfo("result",res)
        elif solve < 25 and solve > 19:
            """res="your bmi is"+str(solve)+"\n normal"
            messagebox.showinfo("result",res)"""
            lbl3=Label(text="normal")
            lbl3.place(x=140,y=300)
        elif solve < 30 and solve >= 25:
            res = "your bmi is" + str(solve) + "\n overweight"
            messagebox.showinfo("result", res)
        elif solve < 40 and solve >=30:
            res = "your bmi is" + str(solve) + "\n obese"
            messagebox.showinfo("result", res)
        else:
            res = "your bmi is" + str(solve) + "\n attention"
            messagebox.showinfo("result", res)


   # print(f"your IBM is: {solve}")






#button
buttonn=Button(text="Calculate",command=clickbutton)
buttonn.place(x=140,y=130)








window.mainloop()