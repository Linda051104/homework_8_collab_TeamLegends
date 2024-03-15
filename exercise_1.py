def replace_last(numbers):
    if len(numbers) <= 1:  # check if the list has no element or has 1 element
        return numbers     # return the same list  
    else:      
        return numbers[-1:] + numbers[:-1] # move the last element to first position then all the elements after(except the last one)
    
print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))




