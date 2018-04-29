# coding=utf-8
import math
def is_prime(n): #判断整数是不是质数
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def PrimeFactorsListGenerator(n):  #因数分解
    k = n
    l = []
    while not is_prime(k):
         for i in range(2, int(math.sqrt(k) + 1)):
              if k % i == 0:
                  l.append(i)
                  k = k // i
                  break
    else:
        l.append(k)
    return l


def gcd(n1,n2):   # 最大公约数
    if(n1%n2 == 0):
        return n2
    return gcd(n2,n1%n2)

def lcm(n1,n2):  #最小公倍数
    """lowest common multiple  function"""
    return n1 * n2 // gcd(n1, n2)