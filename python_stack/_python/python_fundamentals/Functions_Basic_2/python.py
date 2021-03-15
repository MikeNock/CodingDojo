#1
def countdown (a):
    for i in range (a,-1,-1):
        print(i)
countdown(5)

#2
def print_and_return (a):
    print(a[0])
    return (a[1])
print_and_return ([2,3])

#3
def first_plus_length (a):
    sum=a[0]+len(a)
    print(sum)
    return(sum)
first_plus_length ([1,2,3,4,5])

#4
def values_greater_than_second (a):
    new_list=[]
    if len(a)<2:
        return "False"
    else: 
        for i in range (0,len(a),1):
            if a[i]>a[1]:
                new_list.append(a[i])
    print(len(new_list))
    return new_list
values_greater_than_second ([1,2,3,12,8,6])

#5
def this_length_that_value (a,b):
    new_list=[]
    for i in range (a):
        new_list.append(b)
    return new_list
this_length_that_value(3,4)