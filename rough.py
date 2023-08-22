N = int(input())
term_num = '1'
sum = 0
for i in range(1,(N+1)):
    term = term_num*i
    sum = sum+int(term)
print(sum)

#While Loop
N = int(input())
term_num = '1'
i = 1
sum = 0
while(i<(N+1)):
    term = term_num*i
    sum = sum+int(term)
    i+=1
print(sum)