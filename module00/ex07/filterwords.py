# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbel-bas <mbel-bas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/01 10:48:47 by mbel-bas          #+#    #+#              #
#    Updated: 2022/03/01 14:31:15 by mbel-bas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys


def main():
    if len(sys.argv) == 3:
        lst = re.split(' |\n', sys.argv[1])
        f = filter(lambda x: len(x) > int(sys.argv[2]), lst)
        print(list(f))
    else:
        print("what are you doing")

if __name__ == "__main__":
    if sys.argv[2].isdigit() == True:
        main()
    else:
        print("ERROR")