def highest_product_of_three(array):
    
    lowest = min(array[0], array[1])
    highest = max(array[0], array[1])

    highest_product_of_2 = array[0]*array[1]
    lowest_product_of_2 = array[0]*array[1]
    highest_product_of_three = array[0]*array[1]*array[2]

    for current in array[2:]:
        highest_product_of_three = max(highest_product_of_three, highest_product_of_2*current, lowest_product_of_2*current)

        highest_product_of_2 = max(highest_product_of_2, highest*current, lowest *current)

        lowest_product_of_2 = min(lowest_product_of_2, highest*current, lowest*current)

        lowest = min(current, lowest)
        highest = max(current, highest)

    return highest_product_of_three
    

print highest_product_of_three([1,2,3]), 6
print highest_product_of_three([1,2,3,4,5,6]), 4*5*6
print highest_product_of_three([1,2,3,4,5,-1]), 3*4*5
print highest_product_of_three([-1,-2,-1,-1]), -1
print highest_product_of_three([-10,-10,1,2,3]), 300


