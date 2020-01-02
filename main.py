debug = True

#function to put guesses into the debugger
def get_next_roman_num():
  next_roman_num_list = ["I", "II", "III", "IV", "V",
                        "VI", "VII", "VIII", "IX", "X",
                         "XI", "XII", "XIII", "XIV", "XV",
                         "XVI", "XVII", "XVIII", "XIX", "XX",
                         "XXI", "XXII", "XXIII", "XXIV", "XXV",
                         "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
                         "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV",
                         "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
                         "XLI", "XLII", "XLIII", "XLIV", "XLV",
                         "XLVI", "XLVII", "XLVIII", "XLIX", "L"]
  return next_roman_num_list

#function to get numbers to test roman nums
def get_next_expected_num():
  next_expected_num_list = [1, 2, 3, 4, 5,
                            6, 7, 8, 9, 10,
                            11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25,
                            26, 27, 28, 29, 30,
                            31, 32, 33, 34, 35,
                            36, 37, 38, 39, 40,
                            41, 42, 43, 44, 45,
                            46, 47, 48, 49, 50]
  return next_expected_num_list

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

#function to make indexes out of the roman num
def index_roman_num(roman_num):
  index = list(roman_num)
  for i in range(len(index)):
    if index[i] == "I":
      index[i] = 1
    if index[i] == "V":
      index[i] = 2
    if index[i] == "X":
      index[i] = 3
    if index[i] == "L":
      index[i] = 4
    if index[i] == "C":
      index[i] = 5
    if index[i] == "D":
      index[i] = 6
    if index[i] == "M":
      index[i] = 7
  return index

#function to check
def check_for_rule_of_two(index):
  rule_of_two = True
  for i in range(len(index) - 1):
    if (index[i + 1] - index[i]) <= 2:
      continue
    else:
      rule_of_two = False
  return rule_of_two

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
  new_num_list = list() #make new list to hold new values
  size_num_list = len(num_list)
  for i in range(size_num_list):
    if i == 0: #A is the first num in list
      if num_list[i] < num_list[i + 1]: #A < B
        new_value = subtract_num(num_list[i], num_list[i + 1]) #C = B - A
        new_num_list.append(new_value) #add C
      if num_list[i] == num_list[i + 1] or num_list[i] > num_list[i + 1]: #A = B or A > B
        new_num_list.append(num_list[i]) #add A
    if i == (size_num_list - 1): #A is the last num in list
      if num_list[i] > num_list[i - 1]: #A > num before
        continue
      if num_list[i] == num_list[i - 1] or num_list[i] < num_list[i - 1]: #A = num bef or A < num bef
        new_num_list.append(num_list[i]) #add A
    if i != 0 and i != (size_num_list - 1): #A is in the middle of the list
      if num_list[i] > num_list[i - 1]: #A > num before
        continue
      else:
        if num_list[i] < num_list[i + 1]: #A < B
          new_value = subtract_num(num_list[i], num_list[i + 1]) #C = B - A
          new_num_list.append(new_value) #add C
        if num_list[i] == num_list[i + 1] or num_list[i] > num_list[i + 1]: #A = B or A > B
          new_num_list.append(num_list[i]) #add A
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
      expected_num = get_next_expected_num()[i]
      if (check_for_roman_numerals(roman_num)): #if roman num are entered correctly
        num_list = convert_roman_num_to_num(roman_num) #convert roman num to nums
        if (len(num_list)) == 1: #if there is only one num
          number = add_new_list(num_list) #convert num from list to num
          if number == expected_num:
            continue
          else:
            print("wrong calc ", roman_num, " expected ",
                  expected_num, " got ", number)
        else: #if there is more than one num
          index = index_roman_num(roman_num)
          if check_for_rule_of_two(index):
            if check_for_tens(num_list):  #if nums follow tens rule
              new_num_list = subtract_and_simplify(num_list)
              #check for sub and make new list
              number = add_new_list(new_num_list) #add up new list to get num
              if number == expected_num: #check if calculating correct num
                continue
              else: #print out message if calculation is incorrect
                print("wrong calc, ", roman_num, " expected ",
                      expected_num, " got ", number)
            else:
              print(roman_num, " is an invalid roman numeral")
          else:
            print(roman_num, " is an invalid roman numeral")
      else:
        print(roman_num, " is an invalid roman numeral")
  else: #if debug mode not activated
    roman_num = input("Enter Roman Numeral: ") #user inputs, roman num
    if (check_for_roman_numerals(roman_num)): #if roman num are entered correctly
      num_list = convert_roman_num_to_num(roman_num) #convert roman num to nums
      if (len(num_list)) == 1: #if there is only one num
        number = add_new_list(num_list) #convert num from list to num
        print(roman_num, " = ", number)
      else: #if there is more than one num
          index = index_roman_num(roman_num)
          if check_for_rule_of_two(index):
            if check_for_tens(num_list):  #if nums follow tens rule
              new_num_list = subtract_and_simplify(num_list)
              #check for sub and make new list
              number = add_new_list(new_num_list) #add up new list to get num
              print(roman_num, " = ", number)
            else:
              print(roman_num, " is an invalid roman numeral")
          else:
            print(roman_num, " is an invalid roman numeral")
    else:
      print(roman_num, " is an invalid roman numeral")


if __name__ == "__main__":
  main()
