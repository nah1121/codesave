def calculator():
    
    print('''Calculations available are: \n\nAddition: +\n
          Subtraction: -\nMultiplication: *\nDivision: /\n
          Exponents: **\nRoot: //\nResciprocal: 1/\n
          Scientific Notation: sn''')
    
    
    
    op = str(input("Enter what kind of calculation you want: "))
    print(op)
    try:
        if op == '+':
            nums = list(map(int, input('Enter the numbers separated by space: ').split()))
            sum = 0
            
            for i in nums:
                sum += i
            print(sum)
        elif op == '*':
            nums = list(map(int, input('Enter the numbers to multiply separated by space: ').split()))
            
            res = 0
            
            for i in nums:
                res *= i
            
            return res
        
        elif op == '-':
            nums = list(map(int, input('Enter the numbers to multiply separated by space: ').split()))
            
            res = 0
            
            for i in nums:
                res -= i
            
            return res
        
        elif op == '/':
            nums = list(map(int, input('Enter the numbers to multiply separated by space: ').split()))
            
            res = 0
            
            for i in nums:
                res /= i
            
            return res
        
        elif op == '**':
            

            nums = list(map(int, input('Enter the two numbers: ').split()))
            
            res = 0
            
            for i in nums:
                res /= i
            
            return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    except:
        print('d')
    
calculator()


