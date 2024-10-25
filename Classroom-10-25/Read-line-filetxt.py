with open('test.txt', 'r', encoding='utf-8-sig') as file: 

    s = file.readline()

    while s:
        print(s.strip())

        s= file.readline()