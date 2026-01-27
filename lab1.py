#problem 1
def numsIncreasing():
    nums= []
    while True:
       userInput= input("Please enter a number: ")

       if userInput== "":
           break
        
       nums.append(float(userInput))

    if len(nums)== 0:
       print("No numbers were entered")
       return

    if nums == sorted(nums):
      print("Numbers were entered in increasing order.")
    else:
      print("Numbers were not entered in increasing order.")


#problem 2

def avgWordLength(filename):
    file= open(filename, 'r')
    words= file.read().split()
    file.close
    if len(words)== 0:
        return 0.0
    total_characters= sum(len(word) for word in words)
    return total_characters/ len(words)


#problem 3
def wordCounts(words):
    counts = {}
    for word in words:
        if word =="":
            continue
        firstLetter= word[0].upper()
        if firstLetter in counts:
            counts[firstLetter] +=1
        else:
            counts[firstLetter]=1
    return counts


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab1TEST.py' ))

                   
    
    
    
