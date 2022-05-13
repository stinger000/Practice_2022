# 3.2

leafe_symbol = "*"
bottom_symbol = "I"
top_height = int(input())
bottom_height = int(input())
bottom_wight = int(input())

screen_wight = top_height * 2 + 1

i = 0
while i < top_height:
    print((leafe_symbol * (1+i*2)).center(screen_wight))
    i += 1

i = 0
while i < bottom_height:
    print((bottom_symbol * (bottom_wight)).center(screen_wight))
    i += 1
