m_input = float(input("Enter a number less than 25:\n"))  
if m_input >= 25:  
    print("Error")
else:
    for i in range(int(m_input), 26):  
        print(f"Inside the loop, my variable is {i}")