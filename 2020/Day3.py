##Author:   Bryan Sears
##Date:     12/01/2020
##Problem: 

##read input in
my_file = open("2020/Day3InputTesting.txt", "r")
testlist = my_file.read().splitlines()
my_file.close()
##read input in
my_file = open("2020/Day3Input.txt", "r")
lists = my_file.read().splitlines()
my_file.close()
##Part 1
print('-'*25)
print('Part 1')

def slopes(list):
    marker = 0
    trees = 0
    for x in list:
        while marker>=len(x):
            x+=x
        location = x[marker]
        if location == '#':
            trees+=1
        marker +=3
    return trees
            
testanswer = slopes(testlist) 
answer = slopes(lists) 
print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)
##Part 2

print('Part 2')

def slopes2(list,x,y):
    marker = 0
    trees = 0
    if y == 2:
        z = -1
        marker=1
        for i in list:
            
            if z == 1:
                while marker>=len(i):
                    i+=i
                location = i[marker]
                if location == '#':
                    trees+=1
                
                marker +=x
                z=0
            else:
                z+=1

    else:
        for i in list:
            while marker>=len(i):
                i+=i
            location = i[marker]
            if location == '#':
                trees+=1
            marker +=x
    return trees
##Test multiplied 
testanswer = (slopes2(testlist,1,1))
testanswer=testanswer*slopes2(testlist,3,1)
testanswer=testanswer*slopes2(testlist,5,1)
testanswer=testanswer*slopes2(testlist,7,1)
testanswer=testanswer*slopes2(testlist,1,2)

##Answers Multiplied
answer = (slopes2(lists,1,1))
answer=answer*slopes2(lists,3,1)
answer=answer*slopes2(lists,5,1)
answer=answer*slopes2(lists,7,1)
answer=answer*slopes2(lists,1,2)

print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)