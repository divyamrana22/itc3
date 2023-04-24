input_str = "Python is a case sensitive language"

#a.
print("a. Length of input string =",len(input_str))

#b. 
reverse_str = input_str[-1:-35:-1]  
print("b. reverse order of string =",reverse_str)

#c.
new_str = input_str[11:25:1]
print("c. ",input_str[10:25:1])

#d.
new_string = input_str.replace("a case sensitive","object oriented")
print("d.",new_string)

#e. 
_new_str = input_str.find("a")
print('e. Poistion of the substring "a" in the given input string is',_new_str)

#f
_new_string = input_str.replace(" ","")
print("f. After removing the white spaces we get:",_new_string)