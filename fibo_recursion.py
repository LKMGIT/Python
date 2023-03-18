def fibo(n):
    if n == 1:   #비교 1
        return 1
    if n == 2:   #비교 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)  # 뺼셈 2 덧셈 1

print("fibo(3):", fibo(3))
print("fibo(10):", fibo(10))
print("fibo(20):", fibo(20))
print("fibo(35):", fibo(35))


