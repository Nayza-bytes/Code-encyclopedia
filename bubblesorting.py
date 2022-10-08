#Created by Nayza-bytes
#Bubble sorting algorithm

import time
import random

list_to_sort = [random.randint(1, 100) for i in range(1000)] #This is the list that we would sort

#this decorator return the runtime of any functions taken in parameters
def timed_func(func_to_time): #Take a function into parameter
    def timed(*args, **kwargs):
        start = time.perf_counter() #start a counter
        res = func_to_time(*args, **kwargs) #execute the function takne in parameters
        print(time.perf_counter() - start) #Subtract the end counter to the star counter and print it
        return res
    return timed

#We're defining a function here for the algorithm
@timed_func
def sorting(items):
    #Going to loop over all of the items list
    for i in range(len(items)):
        already_sorted = True #This is useful to break out of the programm after the algorithm is done sorting
        #We are going to loop again on all of the list but with substracting i because some elements could be already sorted
        for j in range(len(items) - i - 1):
            #Check if the item we're checking is greater than the next item in the list
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j] #this expression is useful to swap values
                print(items)

    return items #We are returning the sorted list

if __name__ == '__main__':
    print(sorting(list_to_sort))
