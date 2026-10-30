print("-------------Welcome to the Functional Treat-------------")


array=[]  

#i define Array here because of we have to store values untill we exit the program.
#if i put array variable in while loop so it removes all values after every iteration

while True:
    choise=int(input("""\n
Main Menu:
1.Input data
2.Display data summury(Usinng Built in function)
3.Calculate Factorial(Recursion)
4.Filter Data By threshold(Lambda)
5.sort data
6.Display data set statistic(It return multiple values)
7.Exit program
\n Enter your choise(1-7): """))

    
    
    if choise==1:
        a=input("\nEnter Data for 1D Array(Seprated by space):\n")
        a=a.split(sep=" ")
        for i in a:
            array.append(int(i))
        print(f"Your Input Data in Array:{array}\n")
    

    elif choise==2:

        if len(array)==0:
            print("Plz first Enter Data.")
        else:
            print(f"""\n-------Data Summary:
                -Total Element: {len(array)}
                -Minimum Value: {min(array)}
                -Maximum Values: {max(array)}
                -Sum of all values: {sum(array)}
                -Average of all values: {sum(array)/len(array)}""")
            
    elif choise==3:
            def factorial(n):
                if n==1 or n==0:
                    return 1
                else:
                    return n*factorial(n-1)
            num=int(input("\nEnter a number for Calculate Factorial: "))

            print(f"\nFactorial of {num}: {factorial(num)}")


    elif choise==4:
        if len(array)==0:
            print("Plz first Enter Data.")

        else:
            threshold=int(input("\nEnter a threshold Value for filter above this value: "))

            threshold_list=list(filter(lambda x:x>threshold , array))

            print(f"Filtered Data (Values>{threshold}): {threshold_list}")

        
    elif choise==5:
        def asending():
            print("Assending: ",sorted(array))

        def decending():
             print("Decending: ",sorted(array,reverse=True))

        if len(array)==0:
            print("Plz first Enter Data.")


        else:
            while True:
                choise_2=int(input("""\nChoose Sorting:
                1.Assending ordered
                2.Decending Ordered
            
                Enter your Choise: """))

                if choise_2==1:
                    asending()
                    break
                elif choise_2==2:
                    decending()
                    break
                else:
                    print("Enter Valid Chooise.")


    elif choise==6:
        def statistics(array):
            a=min(array)
            b=max(array)
            c=sum(array)
            d=sum(array)/len(array)

            return a,b,c,d
        
        if len(array)==0:
            print("Plz first Enter Data.")

        else:
            minimum,maximumx,total,avg=statistics(array)

            print(f"""
Dataset Statistics:
-Minimum: {minimum}
-Maximum: {maximumx}
-Total Sum: {total}
-Average: {avg} """)

    elif choise==7:
        print("\n-------------Thank You For Using Functional Treat-------------")
        break
    else:
        print("\nEnter the valid choise!!!! Between 1 to 7!!!!!")