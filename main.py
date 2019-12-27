debug = False

#function to put guesses into the debugger
def get_next_roman_num():
  next_roman_num_list = ["I", "II", "III", "IV", "V",
                        "VI", "VII", "VIII", "IX", "X",
                     "a", "A", "apple", "1", "2",
                     "XM", "CX", "CLXV", "XL",
                     "XC", "XCIV"]
  return next_roman_num_list

#function to check if roman numerals are entered correctly
def check_for_roman_numerals(roman_num):
  is_roman_num = True
  roman_num = list(roman_num)
  for i in range(len(roman_num)):
    if roman_num[i] == "I":
      continue
    if roman_num[i] == "V":
      continue
    if roman_num[i] == "X":
      continue
    if roman_num[i] == "L":
      continue
    if roman_num[i] == "C":
      continue
    if roman_num[i] == "D":
      continue
    if roman_num[i] == "M":
      continue
    else:
      is_roman_num = False
  return is_roman_num

#function to convert roman numerals to numbers
def convert_roman_num_to_num(roman_num):
  roman_num = list(roman_num)
  for i in range(len(roman_num)):
    if roman_num[i] == "I":
      roman_num[i] = 1
    if roman_num[i] == "V":
      roman_num[i] = 5
    if roman_num[i] == "X":
      roman_num[i] = 10
    if roman_num[i] == "L":
      roman_num[i] = 50
    if roman_num[i] == "C":
      roman_num[i] = 100
    if roman_num[i] == "D":
      roman_num[i] = 500
    if roman_num[i] == "M":
      roman_num[i] = 1000
  return roman_num

#function to check if B = 10^x, then A < 10^(x+1), or A >= 10^x
def check_for_tens(num_list):
  tens = True
  for i in range(len(num_list) - 1):
    if num_list[i + 1] == 10:
      if num_list[i] < 100:
        continue
      if num_list[i] >= 10:
        continue
      else:
        tens = False
    if num_list[i + 1] == 100:
      if num_list[i] < 1000:
        continue
      if num_list[i] >= 100:
        continue
      else:
        tens = False
    if num_list[i + 1] == 1000:
      if num_list[i] >= 1000:
        continue
      else:
        tens = False
  return tens

#function to subtract numbers
def subtract_num(A, B):
  C = B - A
  return C

#function to find if A < B, and create a new list with new values
def subtract_and_simplify(num_list):
  new_num_list = list()
  for i in range(len(num_list) - 1):
    if num_list[i] < num_list[i + 1]: #if A < B
      new_num_list.append(subtract_num(num_list[i], num_list[i + 1]))
      #add subtracted total to new_num_list
    if num_list[i] == num_list[i + 1]: #if A = B
      new_num_list.append(num_list[i])  #add A to new_num_list
      if (i + 1) == (len(num_list) - 1):  #if B is the last num in num_list
        new_num_list.append(num_list[i + 1])  #add B to new_num_list
    if num_list[i] > num_list[i + 1]: #if A > B
      if i == 0:  #if A is the first num in num_list
        new_num_list.append(num_list[i])  #add A to new_num_list
        if (i + 1) == (len(num_list) - 1): #if B is the last num in num_list
          new_num_list.append(num_list[i + 1])  #add B to new_num_list
      if num_list[i] > num_list[i - 1]: #if A > num before A
        continue  #don't add A
      else: #otherwise
        new_num_list.append(num_list[i])  #add A to new_num_list
        if (i + 1) == (len(num_list) - 1):  #if B is last num in num_list
          new_num_list.append(num_list[i + 1])  #add B to new_num_list
  return new_num_list

#function to total up the numbers
def add_new_list(new_num_list):
  num_total = 0
  for i in range(len(new_num_list)):
    num_total = num_total + new_num_list[i]
  return num_total

def main():
  if debug: #if debug mode activated
    roman_num_list_length = len(get_next_roman_num())
    for i in range(roman_num_list_length):
      roman_num = get_next_roman_num()[i]
      if (check_for_roman_numerals(roman_num)): #if roman num are entered correctly
        num_list = convert_roman_num_to_num(roman_num) #convert roman num to nums
        if (len(num_list)) == 1: #if there is only one num
          number = add_new_list(num_list) #convert num from list to num
          print(roman_num, " = ", number)
        else: #if there is more than one num
          if check_for_tens(num_list):  #if nums follow tens rule
            new_num_list = subtract_and_simplify(num_list)
            #check for sub and make new list
            number = add_new_list(new_num_list) #add up new list to get num
            print(roman_num, " = ", number)
          else:
            print(roman_num, " Is an Invalid Roman Numeral")
      else:
        print(roman_num, " Is an Invalid Roman Numeral")
  else: #if debug mode not activated
    roman_num = input("Enter Roman Numeral: ") #user inputs, roman num
    if (check_for_roman_numerals(roman_num)): #if roman num are entered correctly
      num_list = convert_roman_num_to_num(roman_num) #convert roman num to nums
      if (len(num_list)) == 1: #if there is only one num
        number = add_new_list(num_list) #convert num from list to num
        print(roman_num, " = ", number)
      else: #if there is more than one num
        if check_for_tens(num_list):  #if nums follow tens rule
          new_num_list = subtract_and_simplify(num_list)
          #check for sub and make new list
          number = add_new_list(new_num_list) #add up new list to get num
          print(roman_num, " = ", number)
        else:
          print(roman_num, " Is an Invalid Roman Numeral")
    else:
      print(roman_num, " Is an Invalid Roman Numeral")


if __name__ == "__main__":
  main()
