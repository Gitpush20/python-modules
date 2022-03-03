# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/01 15:36:21 by mbel-bas          #+#    #+#              #
#    Updated: 2022/03/01 16:56:58 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

print("This is an interactive guessing game!\
You have to enter a number between 1 and 99 to find out the secret number.\
Type 'exit' to end the game.\
Good luck!\n")
print()
count = 0
while (True):
    t = (input("What's your guess between 1 and 99?\n>>"))
    print(t)
    if t.isdigit:
        t = int(t)
        if t == 42:
            if count == 0:
                print("The answer to the ultimate question of life,the universe and everything is 42.\nCongratulations! You got it on your first try!")
                quit()
            else:
                print("Congratulations, you've got it!")
                print(f"You won in {count} attempts!")
                quit()
        elif t > 42:
            print("too high")
            count += 1
        elif t < 42:
            print("too low")
            count += 1
    else: 
        if t  == "exit":
            t = str(t)
            print("Goodbye!")
            quit()
        else:
            print("sir t9awd")
    
    