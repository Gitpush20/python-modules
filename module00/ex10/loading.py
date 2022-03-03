# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/01 16:58:02 by mbel-bas          #+#    #+#              #
#    Updated: 2022/03/01 18:07:23 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from time import sleep

def ft_progress(listy):
    l = len(listy)
    N = 100
    for i,elem in enumerate(listy):
        ind = int(((i)/l) * N)        
        s = '['
        s += '=' * (ind)
        s += '>'
        s += ' ' * (N - ind)
        s += ']'
        s += f" {str(i + 1)}/{l}"
        print(s, end="\r")
        yield elem

listy = range(1000)
ret = 000
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
# values = range(0, 101)
# for i in values:
#     sleep(0.01)
#     print("Complete: ", i, "%", end="\r")
# print()