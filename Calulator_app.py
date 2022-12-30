#!/usr/bin/env python3
from tkinter import *


#application body
def run():

	#setting up logic variables
	valid = set('1234567890().+-%')
	invalid = {'x':'*','÷':'/','X^2':'**2','X^Y':'**'}
	expression = ['\n']
	evaluated = [False]
	
	#evaluation function on '=' button press
	def evaluate(scr):
		try:
			res = str(eval(''.join(expression)))
		except: res = 'Error'
		return res

	#main input handling function 
	def enter(v,scr):
		#enable programmatic and user editing of screem widget
		scr['state'] = 'normal'
		
		#resetting screen after evaluation
		if evaluated.pop():
			expression.clear() ; expression.append('\n')
		evaluated.append(False)

		#case of buttons with text that doesnt need to be altered
		if v in valid:
			expression.append(v)
			scr.delete('1.0',END)
			scr.insert('1.0',''.join(expression))
		
		#case of buttons with text that needs to be altered
		elif v in invalid:
			expression.append(invalid[v])
			scr.delete('1.0',END)
			scr.insert('1.0',''.join(expression))
		
		#case of button is to evaluate
		elif v == '=':
			if len(expression) == 1: res = ''
			else:res = evaluate(scr)
			expression.clear() ; expression.append('\n')
			expression.append(res)
			scr.delete('1.0',END)
			scr.insert('1.0',''.join(expression))
			evaluated.append(evaluated.pop()^True)
		
		#clearing the screen
		elif v == 'AC':
			expression.clear() ; expression.append('\n')
			scr.delete('1.0',END)
			scr.insert('1.0',''.join(expression))
		
		#Deleting one token from the right of the screen  
		elif v == 'DEL' and len(expression)>1:
			expression.pop()
			scr.delete('1.0',END)
			scr.insert('1.0',''.join(expression))
		#disbale programmatic and user editing of screem widget
		scr['state'] = 'disabled'


	class HoverButton(Button):
		def __init__(self,master,scr,**kw):
			Button.__init__(self,master=master,**kw,highlightbackground='#6589ab',highlightthickness=1,highlightcolor='#6589ab',bd=0)
			self.config(command=lambda: enter(self['text'],scr))
			self.defaultBackground = self["background"]
			self.bind("<Enter>", self.on_enter)
			self.bind("<Leave>", self.on_leave)
		def on_enter(self, e):
			self['background'] = self['activebackground']
		def on_leave(self, e):
			self['background'] = self.defaultBackground
	
	#main window config
	root = Tk()
	root.title('Calculator')
	root.resizable(False,False)
	root.geometry('500x550')
	root.config(background='#0a141e')

	#Output Screen
	screen = Text(bg = '#3c566e',height=3,font=('Arial',15),fg = '#03141a',bd = 0)
	screen.pack(pady=(50,30))
	screen.config(highlightbackground='#6589ab',highlightthickness=1,highlightcolor='#6589ab')
	screen.config(state='disabled')
	
	#Buttons Frame for Grid Geometry
	buttons = Frame(master=root,bg = '#0a141e',height='300')
	buttons.pack(fill='x')
	
	#this next section is for creating buttons
	count = 0
	for token in ['AC','DEL','.']:
		color = '#03141a' if token not in ['AC','DEL'] else '#a7bccf'
		symb = HoverButton(buttons,screen,bg=color,text = token,fg = 'white',activebackground = '#253544')
		symb.config(height=2,width=5)
		symb.grid(row = 0 , column = count, padx=(20,3),pady=13) ; count+=1

	count = 0
	for token in ['x','÷','%','X^2']:
		symb = HoverButton(buttons,screen,bg='#03141a',text = token,fg = 'white',activebackground = '#253544')
		symb.config(height=2,width=5)
		symb.grid(row = count , column = 3, padx=(20,3),pady=13) ; count+=1
	
	#Minus Button
	minus = HoverButton(buttons,screen,bg='#03141a',text = '-',fg = 'white',activebackground = '#253544')
	minus.config(height=2,width=8)
	minus.grid(row = 0 , column = 4, padx=(20,3)) ; count+=1

	#Plus Button
	plus = HoverButton(buttons,screen,bg='#03141a',text = '+',fg = 'white',activebackground = '#253544')
	plus.config(height=7,width=8)
	plus.grid(row = 1 , column = 4, padx=(20,3),rowspan=2,pady=(7,0)) ; count+=1
	
	#evaluate Button
	equal = HoverButton(buttons,screen,bg='#a7bccf',text = '=',fg = 'white',activebackground = '#253544')
	equal.config(height=8,width=8)
	equal.grid(row = 3 , column = 4, padx=(20,3),rowspan=2,pady=(7,5)) ; count+=1
	
	#Number Buttons [1-9]
	start = 9
	for i in range(3):
		for j in range(3):
			num = HoverButton(buttons,screen,bg='#03141a',text = str(start),fg = 'white',activebackground = '#253544')
			num.config(height=2,width=5)
			num.grid(column=2-j,row=i+1,padx=(20,3),pady=13,)
			start-=1
	
	count = 0
	for token in ['0','(',')','X^Y']:
		symb = HoverButton(buttons,screen,bg='#03141a',text = token,fg = 'white',activebackground = '#253544')
		symb.config(height=4,width=5)
		symb.grid(row = 4 , column = count, padx=(20,3),pady=(0,5)) ; count+=1
		

	#mainloop of the app
	root.mainloop()

# start of the application
if __name__ =='__main__':
	run()

