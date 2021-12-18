'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    for i in range(0,len(records)):
        mini = i
        for j in range(i+1, len(records)):
            if records[mini][1] > records[j][1]:
                mini = j
        records[mini] , records[i] = records[i] , records[mini]
    r = records[0][1]
    l,i = len(records),0 
    while i < l:
        if records[0][1] == r:
            records.pop(0)
        else:
            i+=1
        l = len(records)
    res = []
    r = records[0][1]
    for i in range(0,len(records)):
        if records[i][1] == r:
            res.append(records[i])
    res.sort()
    for i in range(len(res)):
        print(res[i][0])