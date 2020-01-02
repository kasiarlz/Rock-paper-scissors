import random
import simplegui


# Global variables that all functions know about.
# DO NOT EDIT THESE GLOBAL VARIABLES
# OR YOUR GAME WILL BREAK.
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

"""Convert choice to number."""
def choice_to_number(choice):
    return {"rock": 0, "paper": 1, "scissors": 2}
   

"""Convert number to choice."""
def number_to_choice(number):
    return {0: "rock", 1: "paper", 2: "scissors"}


"""Choose randomly for computer."""
def random_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


"""Return the result of who wins."""
def choice_result(human_choice, computer_choice):
    
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    computer_choice_number = choice_to_number(computer_choice)
    human_choice_number = choice_to_number(human_choice)
    
    if human_choice == computer_choice:
        print("Tie")
        
    elif (human_choice_number - computer_choice_number) % 3 == 1:
        print("Computer wins!")
        COMPUTER_SCORE += 1
        
    else:
        print("Human wins!")
        HUMAN_SCORE += 1


def test_choice_to_number():
    assert choice_to_number("rock") == 0
    assert choice_to_number("paper") == 1
    assert choice_to_number("scissors") == 2
    
def test_number_to_choice():
    assert number_to_choice(0) == "rock"
    assert number_to_choice(1) == "paper"
    assert number_to_choice(2) == "scissors"
    
def test_all():
    test_choice_to_number()
    test_number_to_choice()
    
# test_all()


# Handler for mouse click on rock button.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = "rock"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = "paper"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = "scissors"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        # Create a frame and assign callbacks to event handlers

    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 

play_rps()
 