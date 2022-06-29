# intermediate_python_tasks
A few intermediate task to challenge my pythonic sense

# Infinite Monkey Theorem
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long would it take for a Python function to generate just one sentence?


# The substring dilemma
Given a string, find a substring based on the following conditions: 

The substring must be the longest one of all the possible substring in the given string. 
There must not be any repeating characters in the substring. 
If there is more than one substring satisfying the above two conditions, then print the substring which occurs first. 
If there is no substring satisfying all the aforementioned conditions then print -1. 



# Mastermind
A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# Direction Catastrophe
A man was given directions to go from point A to point B. The directions were: “SOUTH”, “NORTH”, “WEST”, “EAST”. Clearly “NORTH” and “SOUTH” are opposite, “WEST” and “EAST” too. Going to one direction and coming back in the opposite direction is a waste of time and energy. So, we need to help the man by writing a program that will eliminate the useless steps and will contain only the necessary directions. 
For example: The directions [“NORTH”, “SOUTH”, “SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”] should be reduced to [“WEST”]. This is because going “NORTH” and then immediately “SOUTH” means coming back to the same place. So we cancel them and we have [“SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”]. Next, we go “SOUTH”, take “EAST” and then immediately take “WEST”, which again means coming back to the same point. Hence we cancel “EAST” and “WEST” to giving us [“SOUTH”, “NORTH”, “WEST”]. It’s clear that “SOUTH” and “NORTH” are opposites hence canceled and finally we are left with [“WEST”].
