#printing a matrix

def func1():
    n=int(input())
    row=[]
    str1=' '
    if n%2==0:
        for i in range(n):
            row.append('-1')
        for j in range(n):
            print(str1.join(row))
    else:
        for i in range(n):
            row.append('1')
        for k in range(n):
            row[k]='-1'
            print(str1.join(row))
            row[k]='1'
t=int(input())
while t>0:
    func1()
    t=t-1