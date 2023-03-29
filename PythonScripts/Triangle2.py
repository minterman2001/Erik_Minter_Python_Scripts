def triangle(n):
    line = 1
    star = 0
        while line <= n:
            while star < line:
                print('*', end = '')
                star += 1
            print('\n')
            line += 1
            star = 0
