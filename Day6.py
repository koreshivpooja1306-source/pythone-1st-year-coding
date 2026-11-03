# To perform string operation on string
#such as:upper,lower,Concatenation,Repetition,lenth,
#Reverse of string,show characters in string,Replace
#Slicing,Spliting,find,count

s1=str(input("Enter the first string:"))
s2=str(input("Enter the second string:"))

#To covert into uppercase and lowercase
print("uppercase of s1 string:",s1.upper())
print("lowercase of strings2:",s2.lower())

#Concentation,Repetition,lenght of string
print("concentation:",s1+""+s2)
print("Repetition:",s1*2)
print("length of s1 string:",len(s1))

#Reverse of string,character in string
print("Reverse of string s1:",s1[::-1])
print("first character in string 1:",s1[0])
print("Last character in string 1:",s1[-1])

#Slicing,spliting

print("string from 0 to 2 position:",s1[0:3])
print("string from 0 to 4 position:",s1[0:4])
print("spliting of sentence:",s1.split())

# Finding the word or letter
print("letter o in the second string:",s2.find("o"))

#Count the letter occurance
print("number that how many time a occurred in string 1:",s1.count("a"))

