# https://www.interviewcake.com/question/product-of-other-numbers
# Greedy
# Time complexity O(n)
# Space complexity O(n)

def print_products(array):
    products_of_all_ints = [1] * len(array)

    product_so_far = 1
    for i in xrange(len(array)):
        products_of_all_ints[i] = product_so_far
        product_so_far *= array[i]
        
    product_so_far = 1
    for i in xrange(len(array)-1, -1, -1):
        products_of_all_ints[i] *= product_so_far
        product_so_far *= array[i]

    return products_of_all_ints


print print_products([1,2,6,5,9]), [540, 270, 90, 108, 60]
print print_products([1,2,6,5,0]), [540, 270, 90, 108, 60]
