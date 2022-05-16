# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/27 21:20:11 by mbel-bas          #+#    #+#              #
#    Updated: 2022/03/03 11:07:27 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def text_analyzer(*args,**kwargs):
    """
    ana belbassi 
    """
    if len(args) > 1:
        print("ERROR")
    else:
        s=str(args[0])
        if not s:
            s = str(input("give me a string:  "))
        upper=0
        lower=0
        space=0
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        punctuation =0
        count = 0
        for i in s:
            count += 1 
            if (i >= 'A' and i<= 'Z'):
                upper +=  1
                continue
            elif (i >= 'a' and i<= 'z'):
                lower += 1
                continue
            elif i == ' ':
                space += 1
                continue
            elif i in punctuations:
                punctuation += 1
                continue
            else:
                continue
        l = str(lower)
        u = str(upper)
        s = str(space)
        p = str(punctuation)
        c = str(count)
        print("the text contains " + c + " characters")
        print("- "+ u + " upper letters")
        print("- "+ l + " lower letters")
        print("- "+ p +" punctuation marks")
        print("- "+ s + " spaces")
    
    
