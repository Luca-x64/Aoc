import re

def first():
    lines = ""
    with open('input.txt','r') as f:
        lines = f.readlines()

    sos = 0 #Sum of sums
    for line in lines:
        nums = re.findall("\d",line)
        sos += int(nums[0]+nums[len(nums)-1])

    print(sos)

def second():
    lines = ""
    with open('input.txt','r') as f:
        lines = f.readlines()

    sos = 0 #Sum of sums    
    for line in lines:
        line=line.replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9e")
        nums = re.findall("\d",line)
        sos += int(nums[0]+nums[len(nums)-1])

    print(sos)

second()
#first()
