def append(list1, list2):
    return list1 + list2


def concat(lists):
    mergedList = []
    for list in lists:
        mergedList+= list
    return mergedList


def filter(function, list):
     return [ x for x in list if function(x)] 

def length(list):
    return sum([1 for _ in list])


def map(function, list):
    return [ function(x) for x in list ]


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