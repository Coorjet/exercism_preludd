def append(list1, list2):
    return list1 + list2


def concat(lists):
    mergedList = []
    for list in lists:
        mergedList+= list
    return mergedList


def filter(function, list):
    filteredList = []
    for element in list:
        if( function(element) == True ):
            filteredList.append(element)
    return filteredList

def length(list):
    count = 0 ;
    for element in list:
        count +=1
    return count


def map(function, list):
    mappedList = []
    for element in list:
        mappedList.append(function(element))
    return mappedList


def foldl(function, list, initial):
   folded = initial
   for element in list:
    folded = function(folded, element)
   return folded

def foldr(function, list, initial):
    folded = initial
    for element in list[::-1]:
     folded = function(element, folded)
    return folded


def reverse(list):
    return list [::-1]