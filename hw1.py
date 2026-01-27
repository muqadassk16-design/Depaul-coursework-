#Problem 1

def hideShow(input_string, mask_string):
    result = ""
    for letter, num in zip(input_string, mask_string):
        if num == '0':
            result += '#'
        else:
            result += letter
    return result

#problem 2

def moreOdds(nums):
    odd_num = 0
    even_num = 0
    
    for n in nums:
        if n % 2 == 1:
            odd_num += 1
        else:
            even_num += 1
            
    return odd_num > even_num

#problem 3

def flipSwitches(sequence):
    on_switches = set()
    
    for letter in sequence:
        if letter.isupper():
            on_switches.add(letter)
        else:
            on_switches.discard(letter.upper())
    
    return on_switches

#problem 4

def numPairs(target, nums):
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                count += 1
                
    return count


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw0TEST.py'))


