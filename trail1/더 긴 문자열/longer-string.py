vocab= input().split() #문자열이면 굳이 map을 쓸 필요가 없음


if len(vocab[0])> len(vocab[1]):
    print(vocab[0], len(vocab[0]), end= " ")
elif len(vocab[0]) < len(vocab[1]):
    print(vocab[1], len(vocab[1]), end= " ")
else:
    print("same")