
def GetHowManyApplesYouWantToBuy():
    NumberOfAppleFunc = int(input("An apple cost 20 pesos each. How many apple/s do you prefer to buy? "))
    return NumberOfAppleFunc


def GetTotalAmountOfApplesYouNeedToPay(PreferredAppleF, PriceOfAppleF):
    AmountOfAppleFunc = int(PreferredAppleF*PriceOfAppleF)
    return AmountOfAppleFunc


def GetHowManyOrangesYouWantToBuy():
    NumberOfOrangeFunc = int(input("An orange cost 25 pesos. How many orange/s do you prefer to buy? "))
    return NumberOfOrangeFunc

def GetTotalAmountOfOrangesYouNeedToPay(PreferredOrangeF, PriceOfOrangeF):
    AmountOfOrangeFunc = int(PreferredOrangeF*PriceOfOrangeF)
    return AmountOfOrangeFunc


def GetTotalAmountOfApplesAndOranges(TotalOfAppleF, TotalOfOrangeF):
    GeneralTotal = int(TotalOfAppleF) + (TotalOfOrangeF)
    return GeneralTotal
    

def DisplayOutput(TotalOfAppleF, TotalOfOrangeF, TotalAmountF):
    print(f"The amount of apple is {TotalOfAppleF} and the amount of orange is {TotalOfOrangeF}. ")
    print(f"The total amount is {TotalAmountF}.")
    
    
# STEPS

# ask how many apples you want to buy and save to variable.
PreferredApple = GetHowManyApplesYouWantToBuy()

# display the amount of apple and save to variable
PriceOfApple = 20
TotalOfApple = GetTotalAmountOfApplesYouNeedToPay(PreferredApple, PriceOfApple)

# ask how many oranges you want and save to variable
PreferredOrange = GetHowManyOrangesYouWantToBuy()

# dispay the amount of orange and save to variable
PriceOfOrange = 25
TotalOfOrange = GetTotalAmountOfOrangesYouNeedToPay(PreferredOrange, PriceOfOrange)

# display the total amount and save the variable
TotalAmount = GetTotalAmountOfApplesAndOranges(TotalOfApple, TotalOfOrange)

# display the output
DisplayOutput(TotalOfApple, TotalOfOrange, TotalAmount)
