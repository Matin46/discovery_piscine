import sys
if len(sys.argv)<3:
    print('none',end='')
else:
    for i in sys.argv[-1:0:-1]:
        print(i)