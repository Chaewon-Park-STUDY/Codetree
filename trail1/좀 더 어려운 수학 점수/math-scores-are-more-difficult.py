math_A, eng_A= map(int, input().split())
math_B, eng_B= map(int, input().split())

if math_A>math_B:
    print("A")
elif math_B>math_A:
    print("B")
else:
    if eng_A>eng_B:
        print("A")
    else:
        print("B")