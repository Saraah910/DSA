def compression(sample, res = ""):
    i = 0
    j = i+1
    count = 1
    while j < len(sample):
        if sample[i] == sample[j]:
            count += 1
            j+=1
        else:
            res += sample[i] + str(count)
            i = j
            j = i+1
            count = 1
    res += sample[i] + str(count)

    if res.endswith('1'):
        res = res.replace('1',"")
        return res
    return res
    
def decompression(output, res=""):
    i = 1
    while i < len(output):
        if output[i-1].isalpha():
            
            if output[i].isdigit():
                res += output[i-1]*int(output[i])
            else:
                res += output[i-1]
        i+=1
    if output[-1].isalpha():
        return res+output[-1]
    return res

def main():
    sample = 'abcddde'
    output = 'a2b2c2z' #O(n)
    result = compression(sample)
    print(result)
    print(decompression(result))
    #compression decompression should be in O(n)
main()
