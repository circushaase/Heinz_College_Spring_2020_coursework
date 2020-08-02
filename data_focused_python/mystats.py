
# File: mystats.py

import numpy as np

# define the mean function here
def mean(*nums):
    total = 0
    length = 0
    
    def is_iter(v):
        v_is_iter = True
        try:
            iter(v)
        except:
            v_is_iter = False
        return v_is_iter
    
    for n in nums:
        try:
            is_iter(n)
            total+= sum(n)
            length += len(n)
        except:
            total += n
            length += 1
    return total/length

# define the stddev function here
def stddev(*nums):
    total = 0
    length = 0
    
    def is_iter(v):
        v_is_iter = True
        try:
            iter(v)
        except:
            v_is_iter = False
        return v_is_iter
    
    for n in nums:
        try:
            is_iter(n)
            total+= sum(n)
            length += len(n)
        except:
            total += n
            length += 1
    
    mean = total/length
    diff = 0
    for n in nums:
        try:
            is_iter(n)
            for i in n:
              diff += (mean - i)*2
            
        except:
            diff += (mean - n)*2
    
    return diff/length

# define the median function here
def median(*nums):
    numlist = []
    
    def is_iter(v):
        v_is_iter = True
        try:
            iter(v)
        except:
            v_is_iter = False
        return v_is_iter
    
    for n in nums:
        try:
            is_iter(n)
            for i in n:
                numlist.append(i)
        except:
            numlist.append(n)
    numlist = sorted(numlist)
    if len(numlist)%2 == 1:
        sub = len(numlist)//2
        return numlist[sub]
    else:
        sub = len(numlist)//2
        med = (numlist[sub] + numlist[sub-1])/2
        return med
            
    
# define the mode function here
def mode(*nums):
    d = dict()
    
    def is_iter(v):
        v_is_iter = True
        try:
            iter(v)
        except:
            v_is_iter = False
        return v_is_iter
    
    for n in nums:
        try:
            is_iter(n)
            for i in n:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        except:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
    mod = [k for k, v in d.items() if v == max(d.values())]
    return tuple(mod)
    

if __name__ == '__main__':
   
# part (a)
    print('The current module is:', __name__)
# Prints the statement "The current module is: __main__"

# part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:', mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:', mean(2.4,3.1))
    print('mean() should FAIL:', mean())

# part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:', mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' + 'and is:', mean((1,), 2, 3, [4,6]))

# part (d)
    for i in range(10):
        print("Draw", i, "from Norm(0,1):", np.random.randn())

#ls50 = [i for i in np.random.randn(50)]
    print("Mean of", len(ls50), "values from Norm(0,1):", mean(ls50))

#ls10000 = [i for i in np.random.randn(10000)]
    print("Mean of", len(ls10000), "values from " + "Norm(0,1):", mean(ls10000))


# part (e)
    np.random.seed(0)
    a1 = np.random.randn(10)
    print("a1:", a1)    
    print("the mean of a1 is:", mean(a1))

# part (f)
    print("the stddev of a1 is:", stddev(a1))

# part (g)
    print("the median of a1 is:", median(a1))
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))

# part (h)
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))

else:
    print('imported module name is:', __name__)
    
    
    
    
    
    
    