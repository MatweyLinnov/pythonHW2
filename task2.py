# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input("Первое число "))
y = int(input("Второе число "))
sum = x + y
pro = x*y

for i in range (x +1):
    for j in range (y+1):
        if  sum == i+j and pro== i*j:   
            print(i,j) 
                         
