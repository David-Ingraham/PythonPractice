#repeat aliqout sum until finding a loop of at most 10 --> this is more involved than just finding a loop
#aliqout sume is the sum of a numbers perfect divisors. the aliqout sequence would be the repeated act of taking aliqout sum.
#for example, divisors of 12 not including itself ar 1,2,3,4,6. these sum to 16. the next numberin the aliqout sequence starting at 12 would then be
#1,2,4,8. you then sum that and find thenext set of divisors
#need to keep a dictionary of each number in the sequence and its corespogning value as the number of times wehave seen it. if that key exceeds 1 then we have a loop
#evetually p will plot it
from math import floor
import sys


def getDivis(num: int) -> 'list[int]':

    if type(num) != int:
        msg = f'Input must be type integer not type {type(num)}'
        raise ValueError(msg)
    
    divis: list[int] = []
    
    for i in range(1, num):
        if num % i == 0:
            divis.append(int(i))

    
    if len(divis) > 1:
        #return f'divisors of {num} are {divis} \n --- \n'
        return divis
    
    else:
        print(f'{num} is prime')
        return divis
    
loop_tracker ={int: int}
def aliqout(num: int):
    original_num: int = num
    divis: list[int] = getDivis(num)
    next_num: int = sum(divis)

    if next_num in loop_tracker.keys():
        loop_tracker[next_num] +=1

    else:
        loop_tracker[next_num] =1

    #loop_tracker.pop('<class \'int\'>')        
    print(divis)
    print(loop_tracker)
 

    """"""
    
    values: list[int] = []

    for val in loop_tracker.values():
        values.append(val)
        #print(f'values list: {values}')

    for val in values:
        #print(type(val))
        #print(val)

        if type(val) ==int:
            if val > 1:
                return f'\n{sys.argv[1]} entered a loop after {len(loop_tracker)-2} itterations'
        else: 
            continue


    res = aliqout(next_num)

    return res





        


def main():
    #for i in range(30):
     #   print(getDivis(i))

    print(aliqout(int(sys.argv[1])))
    
    #print(getDivis(6))
     
    #print([type(item) for item in getDivis(6)])

    #print(getDivis(12161))

    #print(getDivis(3))

     





if __name__ == '__main__':
    main()





