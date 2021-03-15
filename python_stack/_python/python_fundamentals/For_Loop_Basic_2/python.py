#1
def biggie_size(a):
    for i in range (a):
        if a[i]>0:
            a[i]="big"
        elif a[i]<0:
            a[i]="small"
        else:
            a[i]="medium"
    print(a)
    return a            
biggie_size([0,-1,2,-3,4])

#2
def count_positives(a):
    z=0
    for i in range (len(a)):
        if a[i]>0:
            z=z+1
    a[len(a)-1]=z
    print(a)
    return a
count_positives([-1,2,-3,4,-5,6,-7,8])

#3
def sum_total(a):
    print(sum(a))
    return sum(a)
sum_total([1,2,3,4,-10])

#4
def average(a):
    print(sum(a)/len(a))
    return (sum(a)/len(a))
average([1,2,3,4,5,6,7])

#5
def length(a):
    print(len(a))
    return len(a)
length([1,2,3])

#6
def minimum(a):
    print(min(a))
    return min(a)
length([1,2,3,2,3,4,9,8,7,1,5,2])

#7
def maximum(a):
    print(max(a))
    return max(a)
length([1,2,3,2,3,4,9,8,7,1,5,2])

#8
def ultimate_analysis(a):
    print("sumTotal:", str(sum(a)) + ", average:", str(sum(a)/len(a)) + ", minimum:", str(min(a)) + ", maximum", str(max(a)) + ", length:", str(len(a)))
    return "sumTotal:", str(sum(a)) + ", average:", str(sum(a)/len(a)) + ", minimum:", str(min(a)) + ", maximum", str(max(a)) + ", length:", str(len(a))
ultimate_analysis([1,2,3,4,5,6,7,8,9,10])

#9
def reorder(a):
    list.reverse(a)
    print(a)
    return a
reorder([1,2,3,4,5,6,7,8,9])