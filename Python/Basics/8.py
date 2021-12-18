
'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrs = list(arr)
    res = []
    [res.append(x) for x in arrs if not x in res ]
    res.sort(reverse=True)
    print(res[1])