def mergedDict(resp, merged):
    for key in resp.keys():
        if isinstance(resp[key],dict):
            if key not in merged:
                merged[key] = {}
            mergedDict(resp[key],merged[key])
        else:
            merged[key] = resp[key]
        
    print(merged)
    return merged

def main():
    resp_1 = {"clusters":{"10.1.1.1":{"networks":{"vlan0":"Pass"}}}}
    resp_2 = {"clusters":{"10.1.1.1":{"image":{"centOS" : "Fail"}}}}
    resp_3 = {"clusters":{"10.1.1.2":{"image":{"centOS" : "Pass"}}}}
    result = {'clusters': {'10.1.1.1': {'image': {'centos': 'fail'}, 'networks': {'vlan0': 'pass'}}}}
    merged = {}
    mergedDict(resp_1,merged)
    mergedDict(resp_2,merged)
    mergedDict(resp_3,merged)

main()
