MY_intructions={
"add"	:1,
"adc"	:1,
"adiw"	:2,
"sub"	:1,
"subi"	:1,
"sbc"	:1,
"sbci"	:1,
"sbiw"	:2,
"and"	:1,
"andi"	:1,
"or"	:1,
"ori"	:1,
"eor"	:1,	
"com"	:1,
"neg"	:1,
"sbr"	:1,
"cbr"	:1,
"inc"	:1,
"dec"	:1,
"tst"	:1,
"clr"	:1,
"ser"	:1,
"mul"	:2,
"muls"	:2,
"mulsu"	:2,
"fmul"	:2,
"fmuls"	:2,
"fmulsu":2,
"rjmp"	:2,
"ijmp"	:2,
"jmp"	:3,
"rcall"	:3,
"icall"	:3,
"call"	:4,
"ret"	:4,
"reti"	:4,
"cpse"	:3,
"cp"	:1,
"cpc"	:1,	
"cpi"	:1,
"sbrc"	:3,
"sbrs"	:3,
"sbic"	:3,
"sbis"	:3,
"brbs"	:2,
"brbc"	:2,
"breq"	:2,
"brne"	:2,
"brcs"	:2,
"brcc"	:2,
"brsh"	:2,
"brlo"	:2,
"brmi"	:2,
"brpl"	:2,
"brge"	:2,
"brlt"	:2,
"brhs"	:2,
"brhc"	:2,
"brts"	:2,
"brtc"	:2,
"brvs"	:2,
"brvc"	:2,
"brie"	:2,
"brid"	:2,
"mov"	:1,
"movw"	:1,
"ldi"	:1,
"ld"	:2,
"ldd"	:2,
"lds"	:2,
"st"	:2,
"std"	:2,
"sts"	:2,
"lpm"	:3,
"in"	:1,
"out"	:1,
"push"	:2,
"pop"	:2,
"sbi"	:2,
"cbi"	:2,
"lsl"	:1,
"lsr"	:1,
"rol"	:1,
"ror"	:1,
"asr"	:1,
"swap"	:1,
"bset"	:1,
"bclr"	:1,
"bst"	:1,
"bld"	:1,
"sec"	:1,
"clc"	:1,
"sen"	:1,
"cln"	:1,
"sez"	:1,
"clz"	:1,
"sei"	:1,
"cli"	:1,
"ses"	:1,
"cls"	:1,
"sev"	:1,
"clv"	:1,
"set"	:1,
"clt"	:1,
"seh"	:1,
"clh"	:1,
"nop"	:1,
"sleep"	:1,
"wdr"	:1
}

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.lss*"),("all files","*.*")))
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	open_file(filename)
# Create the root window
window = Tk()
label_start=Label(window,text="please enter the No.of start line")
label_start.place(x = 0, y = 50)
Start_line=Entry(window,width=10)
Start_line.place(x = 175, y = 50)
label_end_line=Label(window,text="please enter the NO.of End line")
label_end_line.place(x = 0, y = 80)
END_line=Entry(window,width=10)
END_line.place(x = 175, y = 80)

def open_file(file_name):
		lss_file=open(file_name,'r')	
		calculate_time(lss_file)	
		lss_file.close()	
Result=0
clk=1/8000000
def calculate_time(f):
	start=int(Start_line.get())-1
	end=int(END_line.get())
	for iter in range(start):
		next(f)
	while start < end:
		x=(f.readline()).split("\t")
		print(x)
		for li in MY_intructions.keys():
			if  li in x:
				print(li)
				global Result
				Result= Result+(MY_intructions[li]*clk*1000000)
		start=start+1		
		if start==end:
			break
def submit():
	label_res_t=Label(window,text="the execution time is: " )
	label_res_t.place(x = 0, y = 200)
	label_res_tt=Label(window,text="Micro second" )
	label_res_tt.place(x = 200, y = 200)
	label_res=Label(window,text=Result )
	label_res.place(x = 150, y = 200)
# Set window title
window.title('Execustion time tool')
# Set window size
window.geometry("500x250")
#Create a File Explorer label
# bg= PhotoImage(file="back.png")
# my_bg=Label(window,image=bg)
# my_bg.place(x=0,y=0,relwidth=1,relheight=1)

label_file_explorer = Label(window,text = "File Explorer using Tkinter",width = 50, height = 2,fg = "blue")
button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_exit = Button(window,text = "Exit",command = exit)
button_Submit = Button(window,text = "Submit",command = submit)
label_file_explorer.place(x = 0, y = 0)
button_explore.place(x = 200, y = 150)
button_exit.place(x = 300, y = 150)
button_Submit.place(x=400,y=150)
# Let the window wait for any events
window.mainloop()

