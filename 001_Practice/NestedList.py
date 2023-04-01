counter = int(input("Enter a Number"))
res_array = []
marks_list = []
for i in range(counter):
    name = input()
    marks = float(input())
    res_array.append([name, marks])
    marks_list.append(marks)

newList = sorted(set(marks_list))
runnerup_marks=newList[1]



result_name = []
for val in res_array:
    if runnerup_marks == val[1]:
        result_name.append(val[0])

result_name.sort()

for name in result_name:
    print(name)

