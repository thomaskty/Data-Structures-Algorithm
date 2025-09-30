

# checking whether an year is leap year or not 
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 ==0: 
        leap = True 
    if year%100 !=0 and year%4 ==0:  
        leap = True
    return leap
