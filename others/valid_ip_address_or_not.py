
# checking whether a given ip is valid or not 
def check_ip(ip):
    test = []
    nums = range(0,255) 
    list_ip = ip.split('.')
    if len(list_ip)!=4:
        test.append(False)
    for i in list_ip:
        try:
            if len(i)>3:
                test.append(False) 
            for j in i:
                if int(j) not in nums:
                    test.append(False)
        except:
            test.append(False)
    if False in test:
        return False 
    else:
        return True