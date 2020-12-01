##Author:   Bryan Sears
##Date:     12/01/2020
##Problem: 
"""
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""
##read input in
my_file = open("2020/Day1Input.txt", "r")
lists = my_file.read().splitlines()
my_file.close()


##Part 1
print('-'*25)
print('Part 1')
testlist = [1721,979,366,299,675,1456]
def search_2_2020(list):
    for x in list:
        for y in list:
            sum = int(x)+int(y)
            if sum == 2020:
                ans=int(x)*int(y)
                return ans
            
testanswer = search_2_2020(testlist) 
answer = search_2_2020(lists) 
print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)
##Part 2
"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
print('Part 2')
testlist = [1721,979,366,299,675,1456]
def search_3_2020(list):
    for x in list:
        for y in list:
            for z in list:
                sum = int(x)+int(y)+int(z)
                if sum == 2020:
                    ans=int(x)*int(y)*int(z)
                    return ans
            
testanswer = search_3_2020(testlist) 
answer = search_3_2020(lists) 
print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)
