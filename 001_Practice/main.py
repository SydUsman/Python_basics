n=5
arr=[2,3,6,6,5]

set_arr = set(arr)
print(set_arr)

set_List=list(set_arr)
set_List.remove(max(set_List))
print(set_List)
print(max(set_List))