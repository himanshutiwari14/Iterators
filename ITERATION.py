list1=[]
sum=0
count=0
avg=0


while True:
    try:
        value=int(input("Enter the number:  "))
        list1.append(value)
        print(list1)

        sum=sum+value
        print(f'Sum of inputs are {sum}')
        count+=1
        print(f'Count of inputs are {count}')
        avg=sum/count
        print(f'Avg is {avg}')

        if value=="stop":
            break
    except ValueError:
        print("Value error,please correct your input format")

