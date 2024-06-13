"""test = {}

lines = ['one', 'two', 'three']

i = 0
k =0
while i < len(lines):
    test[lines[i]] = k
    i += 1
    k += 1


print(test)


    """


import sys

def checkFile(file)-> bool:
        
    try:
        f = open(file, 'r')
        lines = f.readlines()
    except:
        Exception(f'file: {file} fucking up')
    counts = {}

    i =0
    
    while i < len(lines):
        if lines[i] in counts:
            counts[lines[i]] +=1
        else:
            counts[lines[i]] =1

        i +=1

    
    repeated = False
    for key, value in counts.items():
        if value > 1:
            print(f'{key.strip()} repeated {value} times in file {file}')
            repeated = True

    if repeated == False:
        print(f'no reapted lines found in file {file}')




def main():
    i = 1
    """while i < len(sys.argv) -1:
        checkFile(sys.argv[i])
        i +=1"""
    for i in range(1, len(sys.argv)):
        checkFile(sys.argv[i])

    
    
    
    #checkFile(sys.argv[2])
    #print(sys.argv)
    

if __name__ =='__main__':
    main()