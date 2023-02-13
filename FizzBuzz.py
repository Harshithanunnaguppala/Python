#FizzBuzzGame
#For all multiples of 3, say Fizz and for all multiples of 5 , say buzz. 
#For all multiples of 3 and 5 say FizzBuzz.
for i in range (51):
    if(i%3==0 and i%5==0):
        print(str(i)+"=FizzBuzz")
    elif(i%3==0):
        print(str(i)+"=Fizz")
    elif(i%5==0):
        print(str(i)+"=Buzz")
    else:
        print(str(i))
    

