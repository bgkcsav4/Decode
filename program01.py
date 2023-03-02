# -*- coding: utf-8 -*-

""""
The standard encoding for Roman numerals follows the rules:
- there is no zero
- only the chars 'IVXLCDM' are used, which correspond to the decimal values
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- numbers are written from left to right, starting with higher values letters
  (thousands, hundreds, tens, units)
- the value of a Roman numeral is obtained by adding the values of the characters,
  EXCEPT when a character is followed by a higher-value character;
  in that case, the lower-value char is subtracted from instead of summed to
  the higher-value char
- at most, 3 equal symbols can be used together, only for the 'IXCM' ones
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- to represent numbers containing digit 4 and/or 9, we use the subtraction from the
  symbol that follows
  e.g.: 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

The XKCD encoding

Let us now consider the Roman numerals encoding suggested by Randall Munroe in his XKCD blog.
He encodes each Roman symbol with the corresponding value and then joins all digits together.
E.g.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Let call this encoding "XKCD format".
To go back to our example, the XKCD sequence '10010010010100511' corresponds to 397.

The goal of this homework is to decode a list of strings representing Roman numerals
in the XKCD format, and return the K maximum corresponding values, in decreasing order.

Design and implement the following functions:

NOTICE: no other libraries are allowed.
"""

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Receives as arguments a list of strings representing values in the
    XKCD format, and a positive integer k <= len(xkcd_values).
    Decodes all XKCD formatted values and return the k higher values
    sorted in decreasing order.

    Parameters
    xkcd_values : list[str]     list of strings (values) in XKCD format
    k : int                     how many values to return
    Returns
    list[int]                   k maximum values in decreasing order
    '''
    
    primary_list = []
    for each in xkcd_values:
        primary_list.append(decode_value(each))
    
    primary_list.sort(reverse = True)
    
    return primary_list[0:k]
    pass


def decode_value(xkcd : str ) -> int:
    '''
    Decode a string representing a value in XKCD format
    and returns the corresponding decimal value (integer).

    Parameters
    xkcd : str                  string in XKCD format
    Returns
    int                         the corresponding value
    
    E.g.: '10010010010100511' -> 397
    '''    
          
    res = list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))
    return res
    
    pass


def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Splits an XKCD formatted string into the corresponding
    list of weights, each corresponding to one of the original roman 
    numeral symbols the encoding is based on.

    Parameters
    xkcd : str              XKCD formatted string
    Returns
    list[int]               list of 'weights' corresponding to roman symbols

    E.g.: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,] 
    '''
    xkcd = xkcd +"."
    separate_number = xkcd[0]
    numbers_list = []
    for each in range(1, len(xkcd)):
        if xkcd[each] == "0":
            separate_number = separate_number + xkcd[each]
        else:
            numbers_list.append(int(separate_number))
            separate_number = xkcd[each]
            
   
    return numbers_list
    pass


def list_of_weights_to_number(weigths : list[int] ) -> int:
    '''
    Transforms a list of weights obtained from the XKCD format
    to the corresponding decimal value, by using the 'sum/subtract' rules.

    Parameters
    weights : list[int]    list of 'weights' of Roman numerals
    Returns
    int                    corresponding integer value
    
    E.g.: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397

    '''
    sum = 0
    for i in range(0,len(weigths)):
        if i+1 <len(weigths) and weigths[i] < weigths[i+1]:
            sum-=weigths[i]
        else:
            sum+=weigths[i]
    return sum
    pass




###################################################################################
if __name__ == '__main__':
    print(decode_value('50010010050101015'))
    print(xkcd_to_list_of_weights("1000100100010100110"))
    print(decode_XKCD_tuple(['150', '1050110', '100100010100110', '11000', '1500', '10050010100110'], 6))
                              
    print('10010010010100511', decode_value('10010010010100511'), '(397?)')
