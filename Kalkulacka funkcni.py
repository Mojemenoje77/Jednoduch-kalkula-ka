
print("""  _   _   _   _   _     _     _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \   / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( V | i | t | a | j ) ( v ) ( k | a | l | k | u | l | a | c | k | e )
 \_/ \_/ \_/ \_/ \_/   \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ """)




while True:
    num1 = float(input("Zadejte první číslo\n"))
    operation =input("Zadejte operaci kteru chcete provést +,-,*,/ ")
    num2 =float(input("zadejte druhý číslo\n"))


    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2


    if operation == "+":
        print(f"Váš výsledek je {num1}+{num2}={a}")
        
    elif operation =="-":
        print(f"Váš výsledek je {num1}-{num2}={b}")
        
    elif operation =="*":
        print(f"Váš výsledek je {num1}*{num2}={c}")
        
    elif operation =="/":
        print(f"Váš výsledek je {num1}/{num2}={d}")
        
    else:
        print("Neplatná operace!")
            
    w= input("Chcete vykonat ďalší operaci?").lower
    if w == "ano":
        input()