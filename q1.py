import copy

def xor(a,b):
    ans=''
    for i in range(len(a)):
        ans = ans + chr((ord(a[i])- ord('0')) ^ (ord(b[i])-ord('0'))+ord('0'))
    return ans

def divide(data,divisor):
    for i in range(len(data)-len(divisor)+1):
        if i>=0:
            prev = data[:i]
        else:
            prev=""
        
        nxt = data[i+len(divisor):]
        curr = data[i:i+len(divisor)]

        curr = xor(curr,divisor)
        data = prev+curr+nxt
        # print(prev,curr,nxt)
    return data[-len(divisor)+1:]

data = "11010011101100"
divisor = "10111"
cpy = copy.copy(data)

padd_zeros = '0' * (len(divisor)-1)
data+=padd_zeros

rem = divide(data,divisor)
print(rem)
cpy+=rem
ze = divide(cpy,divisor)
print(ze)