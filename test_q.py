import time

# cin = raw_input()
# n = cin.split()[0]
# k = cin.split()[1]

# s1 = raw_input().split()
# s2 = raw_input().split()
# s3 = raw_input().split()
n = 10000000
k = 200000
s1,s2,s3 =[],[],[]
for i in range(n):
    s1.append(10000000000 + i)
    s2.append(100000000001 + i)
    s3.append(1000000002 + i)
begin_time = time.time()
i = 0
j = 0
l = 0
m = 0
result = [0] * int(n) *3
count = int(n) -1
while i < count and j < count and l < count:
    if s1[i] <= s2[j] and s1[i]<= s3[l]:
        result[m] = s1[i]
        i += 1
        m += 1
    if s2[j] <= s1[i] and s2[j] <= s3[l]:
        result[m] = s2[j]
        j += 1
        m += 1
    if s3[l] <= s1[i] and s3[l] <= s2[j]:
        result[m] = s3[l]
        l += 1
        m += 1
while i < len(s1):
    result[m] = s1[i]
    i += 1
    m += 1

while j < len(s2):
    result[m] = s2[j]
    j += 1
    m += 1
while l < len(s3):
    result[m] = s3[l]
    l += 1
    m += 1

print(result[int(k) - 1])
