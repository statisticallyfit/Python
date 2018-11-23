
for i in range(10):
    print(i)
    for j in range(10):
        print(j)
        break # here continue would act the same as break.


for i in range(10):
    print(i)
    for j in range(10):
        print(j)
    break # here continue would continue this outer loop but break stops it.