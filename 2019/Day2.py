##Author:   Bryan Sears
##Date:     12/01/2020
##Problem: 
"""
--- Part Two ---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)


"""
ModuleSize =[125517,140694,65516,98562,75660,133603,114499,81732,119081,50911,96650,98330,145164,64851,67455,108208,102674,147581,112059,62456,132006,88738,72139,121074,103936,65149,82081,90168,134670,79142,83296,109983,60250,61982,136326,52980,79969,66851,77049,59720,73494,115708,109326,136399,72950,82041,105467,112321,125019,79213,107186,148340,112833,125646,112509,52396,59446,93967,73179,88725,98256,143303,57503,120314,147921,130856,95561,145857,54976,100605,77961,143120,84127,130389,131848,109542,119653,61660,124800,61498,149675,143906,120361,68328,104473,54279,119945,122511,109410,135350,112070,88822,149086,64594,118788,102569,61721,89170,83581,58722]
testsize = [14,12,1969,100756]
totalcalc = 0
def FuelCalc(Size):
    calc = (Size//3)-2
    if calc >= 0:
        FuelCalc(calc)
    return calc

for x in ModuleSize:
    calc = SizeCalc(x)
    totalcalc=calc+totalcalc

print (totalcalc)
