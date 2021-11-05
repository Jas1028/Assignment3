
def GetMoney():
    MoneyFunc = int(input("How much money do you have? "))
    return MoneyFunc


def GetPriceOfAnApple():
    PriceFunc = int(input("What is the price of an apple? "))
    return PriceFunc


def GetMaxNumberOfAnApple(AmountOfMoneyYouHaveF, PriceOfAnAppleF):
    MaximumNumberFunc = int(AmountOfMoneyYouHaveF) // (PriceOfAnAppleF)
    return MaximumNumberFunc


def GetRemainingMoney(AmountOfMoneyYouHaveF, PriceOfAnAppleF, MaximumNumberOfAnAppleF):
    RemainingMoneyFunc = int(AmountOfMoneyYouHaveF - (PriceOfAnAppleF * MaximumNumberOfAnAppleF))
    return RemainingMoneyFunc


def DisplayOutput(MaximumNumberOfAnAppleF, RemainingMoneyYouWillHaveF):
    print(f"You can buy {MaximumNumberOfAnAppleF} apples and your change is {RemainingMoneyYouWillHaveF} pesos. ")




# STEPS

# enter the amount of money you have and save the variable
AmountOfMoneyYouHave = GetMoney()

# ask for the price of an apple and save the variable
PriceOfAnApple = GetPriceOfAnApple()

# display the maximum number of apples that you can buy
MaximumNumberOfAnApple = GetMaxNumberOfAnApple(AmountOfMoneyYouHave, PriceOfAnApple)

# display the remaining money that you will have
RemainingMoneyYouWillHave = GetRemainingMoney(AmountOfMoneyYouHave, PriceOfAnApple, MaximumNumberOfAnApple)

# display the output
DisplayOutput(MaximumNumberOfAnApple, RemainingMoneyYouWillHave)