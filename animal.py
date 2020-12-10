import csv
import tkinter as tk
import random

#A program to print a bingo sheet full of random animal crossing villagers

animals = {}

def createdict(animals,):
	with open('acnh.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		global line_count
		line_count = 0
		for row in csv_reader:
			animals[line_count+1] = row
			line_count += 1
	print(line_count)

def selectbingo(animals,line_count):
	number = 0
	global bingo 
	bingo = []
	used = []
	i = 0
	while i < 25:
		number = random.randint(1, line_count)
		
		if number not in used:
			bingo.append(animals[number]['Name'])
			used.append(number)
			i += 1
			
		else:
			pass
	print(len(bingo))

def makegrid(bingo):
	window = tk.Tk()
	for i in range(5):
		for j in range(5):
			frame = tk.Frame(
				master=window, relief=tk.RAISED, borderwidth=1)
			frame.grid(row=i, column=j)
			if i == 2 and j == 2:
				label = tk.Label(master=frame, text="FREE", width=15, height=7)
				label.pack()
			elif i == 0:
				label = tk.Label(master=frame, text=bingo[j], width=15, height=7)
				label.pack()
			elif i == 1:
				label = tk.Label(master=frame, text=bingo[j+5], width=15, height=7)
				label.pack()
			elif i == 2:
				label = tk.Label(master=frame, text=bingo[j+10], width=15, height=7)
				label.pack()
			elif i == 3:
				label = tk.Label(master=frame, text=bingo[j+15], width=15, height=7)
				label.pack()
			elif i == 4:
				label = tk.Label(master=frame, text=bingo[j+20], width=15, height=7)
				label.pack()

	window.mainloop()
createdict(animals)


selectbingo(animals,line_count)

makegrid(bingo)

