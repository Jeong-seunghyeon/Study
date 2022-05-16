def sieve(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*2, n+1, p):
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    for i in range(n+1):
        if prime[i]:
            print(i,end=' ')

if __name__=='__main__':
    while True:
        n = int(input('20 이상의 숫자를 입력하세요. : '))
        if n > 20:
            sieve(n)
            break
        else:
            print('20이하의 숫자가 입력되었습니다.')
