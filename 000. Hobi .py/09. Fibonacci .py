def generate_fibonacci_sum(limit):

    previous_num = 1
    current_num = 2
    even_sum = 0

    if previous_num % 2 == 0 :
        even_sum += previous_num
    
    if current_num % 2 == 0 :
        even_sum += current_num

    while current_num <= limit :

        next_num = previous_num + current_num
        
        if next_num % 2 == 0 :
            even_sum += next_num


        previous_num = current_num
        current_num = next_num

    return even_sum

limit = 4000000
result = generate_fibonacci_sum(limit)
print("4 Milyonun Altındaki Tüm Çift Fibonacci Sayılarının Toplamı :\n", result)