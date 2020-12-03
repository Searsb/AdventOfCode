##Author:   Bryan Sears
##Date:     12/01/2020
##Problem: 
"""
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?"""
##read input in
my_file = open("2020/Day2Input.txt", "r")
lists = my_file.read().splitlines()
my_file.close()


##Part 1
print('-'*25)
print('Part 1')
testlist = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
def PasswordPolicy(list):
    validpassword =0
    for x in list:
        line = x.split(':')
        policy= line[0]
        password = line[1]
        lettercount = password.count(policy[-1:])
        length=policy.split('-')
        minchar = int(length[0])
        maxchar = length[1].lstrip().split()
        if lettercount >= minchar:
            
            if lettercount <= int(maxchar[0]):
                validpassword+=1
         
        #print(lettercount)
    return validpassword
testanswer = PasswordPolicy(testlist) 
answer = PasswordPolicy(lists) 
print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)
##Part 2
"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""

def PasswordPolicy2(list):
    validpassword =0
    invalidpassword=0
    for x in list:
        line = x.split(':')#splits policies and passwords
        policy= line[0] #sets policy to a string
        password = line[1] #sets password to string
        letter = (policy[-1:])# sets key letter to string
        length=policy.split('-')#splits the 2 numbers in the policy
        firstpos = int(length[0])
        lastpos = length[1].lstrip().split()
        if password[firstpos]==letter and password[int(lastpos[0])]==letter:
            invalidpassword+=1
        elif password[firstpos]==letter or password[int(lastpos[0])]==letter:
            validpassword+=1
    return validpassword
testanswer = PasswordPolicy2(testlist) 
answer = PasswordPolicy2(lists) 
print('Test:  '+str(testanswer))
print('Final: '+str(answer))
print('-'*25)