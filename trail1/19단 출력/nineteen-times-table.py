
for i in range(1,20):
    for j in range(1,19,2):
        print(f"{i} * {j} = {i*j} / {i} * {j+1} = {i*(j+1)}")
    print(f"{i} * 19 = {19*i}")
