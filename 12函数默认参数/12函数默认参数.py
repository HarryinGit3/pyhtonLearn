def sale_car(price,colour='red',brand='carmy',is_second_hand=True):
    print('price:',price,
          'colour:',colour,
          'brand:',brand,
          'is_second_hand:',is_second_hand
          )
sale_car(1001,'blue')
# 如果参数要被默认，那么后面参数全都要被默认。