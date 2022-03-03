# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/27 20:19:44 by mbel-bas          #+#    #+#              #
#    Updated: 2022/02/27 21:18:55 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
while True:
        try:
            num = int(sys.argv[1])
            break
        except:
            print("That's not a valid option!")
            quit()
if len(sys.argv) == 2:
    if num == 0:
        print("i'm zero")
        quit()
    if num % 2 == 0:
        print("i'am even")
        quit()
    if num % 2 == 1:
        print("i'm odd")
else:
    print("sir t9awd")