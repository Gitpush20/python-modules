# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 09:52:22 by mbel-bas          #+#    #+#              #
#    Updated: 2022/02/28 10:31:53 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def operation(arg1,arg2):
    if len(sys.argv) == 3:
        sum = str(arg1+arg2)
        difference = str(arg1-arg2)
        product = str(arg1*arg2)
        print("sum          :" + sum)
        print("difference   :" + difference)
        print("Product      :" + product)
        if int(sys.argv[2]) == 0:
            print("ERROR (div by zero) ")
            print("ERROR (modulo by zero) ")
            return
        Quotient = str(arg1/arg2)
        remainder = str(arg1%arg2)
        print("Quotient     :" + Quotient)
        print("Remainder    :" + remainder)
if __name__ == "__main__":
    while True:
        try:
            num = int(sys.argv[1])
            num2 = int(sys.argv[2])
            break
        except:
            print("That's not a valid number!")
            quit()
    operation(int(sys.argv[1]) ,int(sys.argv[2]))