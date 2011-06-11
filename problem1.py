#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
class Natural:
    def isMultiple(self, number):
        return number % 3 == 0 or number % 5 == 0
    
    def sum(self, sequence):
        index = 0
        sum = 0
        while index < sequence:
            index += 1
            if self.isMultiple(index):
                sum += index
                
        return sum
    
if __name__ == '__main__':
    print Natural().sum(999)