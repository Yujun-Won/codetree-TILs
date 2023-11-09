string = input()
cmd = input()

L, R = cmd.count('L'), cmd.count('R')


# L에 대한 반영
stepL = ''
stepL = string[L:len(string)] + string[:4]

# R에 대한 반영
stepR = ''
stepR = stepL[-R::] + stepL[:len(stepL)-R]

print(stepR)