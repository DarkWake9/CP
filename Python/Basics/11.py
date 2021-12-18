'''Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def symdiff(a,b):
        a = set(a)
        b = set(b)
        d1 = list(a.difference(b))
        d2 = list(b.difference(a))
        d1.extend(d2)
        d1.sort()
        return d1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    res = symdiff(a,b)
    for i in res:    
        print(i)