#!/usr/bin/env python3

def summ(arrayNumbers):
    result = 0
    for number in arrayNumbers:
        result += number
    return result 

def lowest(arrayNumbers):
    result = arrayNumbers[0]
    for number in arrayNumbers:
        if result > number:
            result = number
        
    return result

def highest(arrayNumbers):
    result = arrayNumbers[0]
    for number in arrayNumbers:
        if result < number:
            result = number
        
    return result 

def main():
    array = []
    isTerminate = True
    try:
        while isTerminate:
            digit = input("enter a number or Enter to finish: ")
            if digit != "":
                array.append(int(digit))
            else:
                
                print(array)
                print("count: ", len(array))

                resultSum = summ(array)
                print("sum: ", resultSum)
                
                resultLowest = lowest(array)
                print("lowest: ", resultLowest)
                
                resultHighest = highest(array)
                print("highest: ", resultHighest)
                
                mean = sum(array) / len(array)
                print("mean: ", mean)
                
                isTerminate = False
    except ValueError as err:
        print(err, "in", digit)


main()