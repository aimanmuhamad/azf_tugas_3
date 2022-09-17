from math_function import add, multiplication, division


def main():
    operator = input("masukkan operator :")
    
    if operator == "+":
        data_1 = int(input("masukkan input 1 :"))
        data_2 = int(input("masukkan input 2 :"))

        result = add(data_1, data_2)
    
    if operator == "*":
        data_1 = float(input("masukkan input 1 :"))
        data_2 = float(input("masukkan input 2 :"))
        
        result = multiplication(data_1, data_2)
    
    if operator == "/":
        data_1 = float(input("masukkan input 1 :"))
        data_2 = float(input("masukkan input 2 :"))
        
        result = division(data_1, data_2)
    
        
    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()