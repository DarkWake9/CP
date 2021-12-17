if __name__ == '__main__':
    n = int(input())
    if n in range(1,151):
        res=0
        if n>=1:
            for i in range(1,min(n,10)):
                res += i * (10**(n-i))
            
            if n>=10:    
                for i in range(10,min(n,100)):
                        res *= 10
                        res += i * (10**(n-i))
                
                if n>=100 and n <=150:
                    for i in range(100,min(n,150)):
                        res *= 100
                        res += i * (10**(n-i))
                    if i == n-1 : print(str(res*100 + n))
                else: print(str(res*10 + n))
            
            else: print(str(res+n))