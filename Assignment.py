            
                                         Module – 2 (Fundamentals of python)
                                         
  Q. Write a Python program to check if a number is positive, negative or zero...
  Ans.  
       for i in range(1,6):
        num = int(input("Enter a number: "))
        if num > 0:
            print("It  is a positive number")
        elif num < 0:
            print("It is a negative number")
        elif num==0:
            print("It is neither a positive or negative")

 


 Q. Write a Python program to get the Factorial number of given number.
 Ans. 
     fact = lambda n: [1,0][n>1] or fact(n-1)*n
     print (fact(5))


 
 Q. Write a Python program to get the Fibonacci series of given range.
 Ans. 
 

 Q. How memory is managed in Python?
 Ans. 


 Q. What is the purpose continue statement in python?
 Ans. 


 Q. Write python program that swap two number with temp variable and without temp variable..
 Ans. 
     * With temp variable 
   swap_numbers_with_temp(a, b):
    t= a
    a = b
    b = t
    return a, b
   print(swap_numbers_with_temp(5,10))
 


  * Without Variable
  n1= 5
  n2= 10

  print("Before Swapping: n1= ",n1," n2= ",n2)

  n1,n2 = n2,n1

  print("After Swapping: n1= ",n1," n2= ",n2) 
 


 
 Q. Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user..
 Ans. 
      # find even or odd 
       for i in range (1,6):
       num = int (input("Enter a number:"))
    
        if num%2==0:
            print("It is even number")
        else:
            print("It is odd number")


 
 Q. Write a Python program to test whether a passed letter is a vowel or not..
 Ans. 
     
 

 Q. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
 Ans. 
      def sum_of_three(a,b,c):
               if a==b or b==c or  a==c:
                  return 0
               else:
                  return a+b+c
    
     print(sum_of_three(4,4,8))
              




 Q. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
 Ans.    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    if num1 == num2 or num1 + num2 == 5 or num1 - num2 ==5 :
      print ("True")
    else:
      print ("False")




 Q. Write a python program to sum of the first n positive integers.
 Ans. 
     def sum_of_positive_num(n):
    sum = 0
    for i in range (1 , n+1):
        sum += i
    return sum


    print (sum_of_positive_num(2))
    print (sum_of_positive_num(3))
    print (sum_of_positive_num(4))    


 

 Q. Write a Python program to calculate the length of a string.





















  
 




























    
  
