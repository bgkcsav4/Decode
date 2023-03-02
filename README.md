# Decode

in function decode_XKCD_tuple, in the first for loop, i create a new array,
 where I add all the values that I convert to actual numbers using the decode_value function.
 then i have double loop, which helps me do a bubble sort algorithm. 
 range(len(primary_list)-1,0,-1) - this code helps me sort the values in a decreasing
 order, since -1 means the list goes in a reversed way.
 i use variable temp to "save" a smaller value to then add it to the list (after the bigger value).
 and then i return the first k number of values, as requested.
 
 in the third function xkcd_to_list_of_weights,
 i add a character "." because as seen in the code, the loop stops right before the 
 last character, so i thought this was an easy solution to the problem. i create two
 lists. I check if the character is "0", it means that the new number has not
 started yet, so the number 0 is a part of the previous numbers. for example, 1+0+0 
 is 100 and not 1, 0, 0 or 10,0. So I add this 0 to the seperate_number variable, which
 at first it was 1, after the first loop it was 10, then 100. then I check if the upcoming 
 character is anything other than 0, it means that the new number has started, so I add the
 seperate_number to the numbers_list, and I change seperate_number to what the next character
 is, in this case 1. and so that's hot the loop goes. when it reaches the last character, it
 stops and doesn't add the last number to the list, which is why i had to add any single symbol
 to the string. Doesn't matter if it's . , 1 , or even an empty character.
 then I convert all of the strings to integers and return the array of ints.
 
 the function list_of_weights_to_number is a common algorithm of summing up values of a list,
 you create a variable that is 0 and and every single value of the array to the variable.
 
lastly, the function decode_value checks if i+1 <len(weigths), so it's not out of bounds.
then it checks if the number is smaller than the next number in the list. if it is, I wrote count 
minus the value, as it is done in roman numbers, if the number is not smaller than the next one, then 
it just sums them up until the end of all the numbers.
