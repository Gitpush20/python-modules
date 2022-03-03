# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 10:35:15 by mbel-bas          #+#    #+#              #
#    Updated: 2022/02/28 12:44:59 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages ={
    'python' : 'Guido van Rossum',
    'Ruby' : 'Yukihiro matsumoto',
    'PHP' : 'rasmus lerdorf',
}
for item in languages:
    print(f"{item} was created by {languages[item]}")