import sys
def downcase_it(text:str) -> str:
    return text.lower()

if len(sys.argv)<2:
    print('none',end='')
else:
    for i in sys.argv[1:]:
        print(downcase_it(i))