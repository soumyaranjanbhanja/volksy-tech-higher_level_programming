#!/usr/bin/python3
my_list=[1,2,3,4,5]
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return (my_list)
