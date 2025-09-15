def main():
    table = 0
    while table <= 10:  
        print(f"Table de {table}:", end=" ")

        num = 0
        while num <= 10:  
            print(table * num, end=" ")
            num += 1

        print()  
        table += 1

if __name__ == "__main__":
    main()