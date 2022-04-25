menu1 = set(["된장찌개","피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2
menu4 = menu1 & menu2
menu5 = menu1 - menu2
print(menu3)
print(menu4)
print(menu5)