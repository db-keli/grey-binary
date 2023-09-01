def gray_to_binary(gray_code):
    binary_code = gray_code[0]
    for i in range(1, len(gray_code)):
        if gray_code[i] == '0':
            binary_code += binary_code[i - 1]
        else:
            binary_code += '0' if binary_code[i - 1] == '1' else '1'
    return binary_code


def binary_to_gray(binary):
    gray = ""
    gray += binary[0]
    for i in range(1, len(binary)):
        gray += str(int(binary[i]) ^ int(binary[i - 1]))
    return gray


def main():
    gray_code = input("Enter Gray code (in the form of a string of 0s and 1s): ")
    
    if not gray_code:
        print("Error: Empty input! Please enter a valid Gray code.")
        return
    
    binary_code = gray_to_binary(gray_code)
    print("Binary code:", binary_code)


if __name__ == "__main__":
    main()
