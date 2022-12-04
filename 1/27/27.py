def odd_ball(arr):
    return arr.index('odd') in arr

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"]))
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"]))
print(odd_ball(["even",10,"odd",2,"even"])) 

def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

print(find_sum(5))
print(find_sum(10)) 

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]

def get_names(names):
    res = []
    for i in names:
        if len(i) == 4:
            res.append(i)
    return(res)

print(get_names(names))