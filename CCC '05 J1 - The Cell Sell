import math

daytime = float(input())
evening = float(input())
weekend = float(input())

def cellrate():
    Adaytimerate = max(0, daytime - 100) * 0.25
    Aeveningtimerate = evening * 0.15
    Aweekendrate = weekend * 0.20
    Bdaytimerate = max(0, daytime - 250) * 0.45
    Beveningtimerate = evening * 0.35
    Bweekendrate = weekend * 0.25
    return Adaytimerate, Aeveningtimerate, Aweekendrate, Bdaytimerate, Beveningtimerate, Bweekendrate

def compare():
    Adaytimerate, Aeveningtimerate, Aweekendrate, Bdaytimerate, Beveningtimerate, Bweekendrate = cellrate()
    Atotal = round(Adaytimerate + Aeveningtimerate + Aweekendrate, 2)
    Btotal = round(Bdaytimerate + Beveningtimerate + Bweekendrate, 2)
    print(f"Plan A costs {Atotal:.2f}")
    print(f"Plan B costs {Btotal:.2f}")
    if Atotal < Btotal:
        print("Plan A is cheapest.")
    elif Btotal < Atotal:
        print("Plan B is cheapest.")
    else:
        print("Plan A and B are the same price.")

compare()




