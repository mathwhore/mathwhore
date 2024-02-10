def month(a):
    months=["Jan","Feb","Mar","Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return months[a-1]


month_no=int(input("Enter the no. of the month"))
print(month(month_no))
