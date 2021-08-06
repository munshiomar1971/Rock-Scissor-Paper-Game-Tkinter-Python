import tkinter
import random

root = tkinter.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("500x600")

random_num = random.randint(1, 3)

# logic

if random_num == 1:
	comp_choice = "R"
elif random_num == 2:
	comp_choice = "P"
elif random_num == 3:
	comp_choice = "S"

# functions
def rock():
	label_user_choice['text'] = "ROCK"


	if comp_choice == "R":
		label_result['text'] = "Tie"
		label_comp_choice['text'] = "Rock"
	elif comp_choice == "P":
		label_result['text'] = "Computer Wins"
		label_comp_choice['text'] = "Paper"
	elif comp_choice == "S":
		label_result['text'] = "You Win"
		label_comp_choice['text'] = "Scissors"



def paper():
	label_user_choice['text'] = "Paper"


	if comp_choice == "R":
		label_result['text'] = "You Win"
		label_comp_choice['text'] = "Rock"
	elif comp_choice == "P":
		label_result['text'] = "Tie"
		label_comp_choice['text'] = "Paper"
	elif comp_choice == "S":
		label_result['text'] = "Computer Wins"
		label_comp_choice['text'] = "Scissors"



def sci():
	label_user_choice['text'] = "Scissors"


	if comp_choice == "R":
		label_result['text'] = "You Lose"
		label_comp_choice['text'] = "Rock"
	elif comp_choice == "P":
		label_result['text'] = "You Win"
		label_comp_choice['text'] = "Paper"
	elif comp_choice == "S":
		label_result['text'] = "Tie"
		label_comp_choice['text'] = "Scissors"



def reset():
	global comp_choice
	random_num = random.randint(1, 3)

	if random_num == 1:
		comp_choice = "R"
	elif random_num == 2:
		comp_choice = "P"
	elif random_num == 3:
		comp_choice = "S"






# Create Widgets
label_result = tkinter.Label(root, text="Choose...")
label_result.pack()

button_rock = tkinter.Button(root, text="Rock", command=rock)
button_rock.pack()

button_paper = tkinter.Button(root, text="Paper", command=paper)
button_paper.pack()


button_sci = tkinter.Button(root, text="Scissors", command=sci)
button_sci.pack()


label_comp_choice = tkinter.Label(root, text=" ")
label_comp_choice.pack()


label_user_choice = tkinter.Label(root, text=" ")
label_user_choice.pack()

button_reset = tkinter.Button(root, text="Reset", command=reset)
button_reset.pack()




root.mainloop()