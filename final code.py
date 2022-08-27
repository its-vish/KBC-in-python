



question_list = [
    "How many continents are there?",             
    "What is the capital of India?",           
    "NG mei kaun se course padhaya jaata hai?" 
]

options_list = [

    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigadh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]


solution_list = [3, 4, 1] 
answer_list=[
    ["1.four","3.seven"],
    ["2.Bhopal","4.Delhi"],
    ["1.Software Engineering","4.Agricultue"]
]
print("kaun Banega codepati (KBC)")
i=0
s=0
count=0
while i<len(question_list[i]):
    print(question_list[i])
    j=0
    k=1
    m=0
    while j<len(options_list[i]):
        print(k,".",options_list[i][j])
        k=k+1
        j=j+1
    num1=input("do you want 50 50 lifeline=")
    if num1=="yes":
        print("50 50 lifeline")
        if count==0:
            print(answer_list[i])
            numo=int(input("enter your answer"))
            if numo==solution_list[i]:
                s+=10000
                print("your answer is correct")
                print("you win Rs/",s)
                

            
            else:
                print("incorrect answer")
                print("you can,t play again")
                
                break
            count+=1
            # print()

        else:
            print("you already use lifeline :")
            
            num3=int(input("enter your answer :"))
            if num3==solution_list[i]:
                print("congrats your answer is right")
                s+=10000
                print("you win Rs/",s+1000)
            else:
                print("No chance")
                print("youe answer is wrong")
                print("you win",s+1000)
                break
    else:
        k=int(input("enter your answer"))
        if k==solution_list[i]:
            print("right answer")
            s=s+12000
            print("you win Rs/",s+1000)
            print("congratulations")

        else:
            print("no chance")
            print("your answer is wrong")
            break
    m+=1
    i=i+1
