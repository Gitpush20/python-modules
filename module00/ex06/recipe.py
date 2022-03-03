# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 14:51:07 by mbel-bas          #+#    #+#              #
#    Updated: 2022/02/28 18:55:17 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_recipe():
    x =str(input("please enter the recipe's name to get its details\n"))
    
x= str(input("please select an option by typing the corresponding number:\n1: Add a recipe\n2: delete a recipe\n3: print a recipe\n4\
: print the cookbook\n4: quit\n"))
switcher ={
    3:print_recipe
}
cookbook = {
    'sandwich' : {1:{'1':'ham','2':'bread','3':'cheese','4':'tomatoes'}, '--meal--' : 'lunch','--prep_time--' : '10 minutes'},
    'cake' : {2 :{'1' : 'flour','2' : 'sugar' , '3':'eggs'}, '--meal--' : 'desert' , '--prep_time--' : '60 minutes'},
    'salad' : {3:{'1' : 'avocado', '2' : 'arugula' , '3' : 'tomatoes', '4' : 'spinach'} , '--meal--' : 'lunch', '--prep_time--' : '15 minutes'}}
#print(cookbook['sandwich'][1])
#print(cookbook['sandwich'].keys())