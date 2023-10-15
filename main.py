def getInps() -> dict[str,int] :
    num1 = int(input("\nenter 1st number\t"))
    num2 = int(input("\nenter 2nd number\t"))
    operation = input("\nwhich operation you want to perform ?\nAddition\nSubtraction\nMultiplication\nDivision\nchoose one :\t").lower()
    
    return {"num1":num1,"num2":num2,"operation":operation}

class Calculator :
    def __init__(self,num1:int,num2:int) :
        self.num1 = num1
        self.num2 = num2
    add = lambda self : self.num1 + self.num2
    sub = lambda self : self.num1 - self.num2
    mult = lambda self : self.num1 * self.num2
    div = lambda self : self.num1 / self.num2



def main() :
    inps = getInps()
    calc = Calculator(inps["num1"],inps["num2"])
    play = 1
    while play :
        if inps["operation"] == "1" or inps["operation"] == "addition" :
            out = calc.add()
            print(f"your result is {out}")
        elif inps["operation"] == "2" or inps["operation"] == "subtraction" :
            out = calc.sub()
            print(f"your result is {out}")
        elif inps["operation"] == "3" or inps["operation"] == "multiplication" :
            out = calc.mult()
            print(f"your result is {out}")
        elif inps["operation"] == "4" or inps["operation"] == "division" :
            out = calc.div()
            print(f"your result is {out}")
        play = int(input("do you want to play again? (1(yes) / 0(no))"))
        exit(not play)

main()