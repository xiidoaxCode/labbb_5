from num2words import num2words

print ("Enter your number : ")
number = int(input())
words = num2words(number) 
print(f" {number} means : '{words}'.")
