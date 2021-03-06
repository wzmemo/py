"""The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-8. 
The Lo Shu Magic Square has the following properties:
The grid contains the numbers 1 through 9 exactly.
The sum of each row, each column, and each diagonal all add up to the same number.

Write a function that accepts a two-dimensional list as an argument
and determines whether the list is a Lo Shu Magic Square. Test the function in a program."""


lst = [
    [4,9,2],
    [3,5,7],
    [8,1,6]
]

flag_h = True
flag_v = True
flag_d = True
def magic_square(lis):
    sumline = 15
    flag_h = hori(lis)
    flag_v = vert(lis)
    flag_d = dia(lis)
    #print (flag_h)
    #print (flag_v)
    #print (flag_d)
    if flag_h == True and flag_v == True and flag_d == True:
        print ('Congratz! Your square is a magic square!!! :D ')
    else:
        print ('Sorry, not a magic square... ')
        
def hori(ls):   
    for i in ls:
        current1 = 0
        for k in i:
            current1+=k
        #print(flag_checkh(current1))
        if flag_checkh(current1) == False:
            return False
    return True
                
def vert(ls):
    current3=0
    for key,line in enumerate(ls):
        if key == 0:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 1:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 2:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
    #print (current3)
    if flag_checkd(current3) == True:
        current3=0
        for key,line in enumerate(ls):
            if key == 0:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 1:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 2:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
        #print(current3)
        if flag_checkd(current3) == True:
            current3=0
            for key,line in enumerate(ls):
                if key == 0:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
                if key == 1:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
                if key == 2:
                    for each,value in enumerate(line):
                        if each == 2:
                            current3+=value
            #print (current3)
            return True
        else:
            return False
    else: 
        return False

#diagonal 
def dia(ls):
    current3=0
    for key,line in enumerate(ls):
        if key == 0:
            for each,value in enumerate(line):
                if each == 0:
                    current3+=value
        if key == 1:
            for each,value in enumerate(line):
                if each == 1:
                    current3+=value
        if key == 2:
            for each,value in enumerate(line):
                if each == 2:
                    current3+=value
    #print (current3)
    if flag_checkd(current3) == True:
        current3=0
        for key,line in enumerate(ls):
            if key == 0:
                for each,value in enumerate(line):
                    if each == 2:
                        current3+=value
            if key == 1:
                for each,value in enumerate(line):
                    if each == 1:
                        current3+=value
            if key == 2:
                for each,value in enumerate(line):
                    if each == 0:
                        current3+=value
        return True
        #print(current3)
    else:
        return False               

def flag_checkh(n):
    if n == 15:
        flag_h = True
    else:
        flag_h = False
    return flag_h
def flag_checkv(n):
    if n == 15:
        flag_v = True
    else:
        flag_v = False
    return flag_v
def flag_checkd(n):
    if n == 15:
        flag_d = True
    else:
        flag_d = False
    return flag_d

magic_square(lst)
