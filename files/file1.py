import pandas as pd
import numpy  as np

def sum_funct(input_list):
    count = 0
    if type(input_list) != list:
        print( 'Error')
    else:
        if len(input_list) > 1:
            for element in input_list:
                count += element
            print (count)
        elif len(input_list) == 1:
            print(input_list[0])
        else:
            print('Empty list')
        
sum_funct([1, 2, 3])
sum_funct(3)
sum_funct([1])