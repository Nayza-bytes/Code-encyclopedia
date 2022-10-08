#Created by Nayza-bytes
#Bubble sorting algorithm

from ast import Expression


list_to_sort = [325, 78, 550, 4, 18, 76, 75, 45] #This is the list that we would sort


#We're defining a function here for the algorithm
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
                already_sorted = False #if we sorted value, we dont escape the algo because there are maybe more value to sort

            if already_sorted:
                break
    
    return items #We are returning the sorted list

if __name__ == '__main__':
    sorting(list_to_sort)
