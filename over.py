list=[104,20,306,40]
result=[ ]
for i in list:
    if i > 100:
        result.append('over')
    else:
        result.append(i)
print(result)
