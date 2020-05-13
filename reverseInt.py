import sys

class Solution:
    # O(1) notation
    def reverse(self, x: int) -> int:
        # checks if our interger is too big to process
        if x >= sys.maxsize/10: #sys.maxsize is an outdated int checker when ints used to have a processing limit.
            return 0 
        
        x = str(x) # turns our int into str for easier opperations
        
        if x[0] == "-":
            x = x[1:] # removes the first letter of the string
            x = x[::-1] # reverses our string
            x = int(x) * -1 # turns our str into a negative int
            
        else:
            x = x[::-1] # reverses our string
            x = int(x) # turns our str into an int
        
        # hopefully gives us the correct sollution
        return x