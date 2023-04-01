import datetime

user_input=input("Enter your goal and Deadline seperated by :")
input=user_input.split(":")
goal=input[0]
deadline=input[1]

deadline_conv_dateType=datetime.datetime.strptime(deadline,"%d.%m.%y")
today=datetime.datetime.today()

remaining=deadline_conv_dateType-today
print(f"Your Goal is {goal} and this is remaining time {remaining}")