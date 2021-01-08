import math,sys

base_values = {"0":0,"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26, "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

base_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]

def main():
  x=0
  main_count = 0
  print("Hello, I convert between number-systems \nfor you. Because of my programmers limited \nmental capactiy I only go upto base 36 \n(Covering 0-9 and the English standard alphabet)\n Enter \"quit\" to quit anytime")
  play = False
  while play != True:
    base_1 = input("What's your starting base:\t")
    base_1, play = correct_inputs(base_1)
    if play != True:
      check_list, new_string = restrict_list(base_list, base_1)
      print(f"Possible digits for starting number:  {new_string}")
      number_1 = input("Starting number:\t")
      number_1, play = correct_inputs(number_1, "number", check_list)
      if play != True:
        base_2 = input("Second base to translate into:\t")
        base_2, play = correct_inputs(base_2)
        if play!= True:
          final_number = math_time(base_1, base_2, number_1)
          print(f"Your answer is:\t{final_number}")


def correct_inputs(start_input, kind = "base", check_list = base_list):
  main_count = 0
  count = 0
  if start_input == "quit":
    start_input = "quit"
    play = True
  else:
    if kind == "base":
      while count < 1:
        if main_count > 0:
          start_input = input("I need a correct value:\t")
        if start_input == "quit":
          start_input = "quit"
          count = 1
        try:
          start_input = int(start_input)
          if 1 <= start_input <= 36:
            count += 1
        except ValueError:
          count = 0
        main_count += 1
    elif kind == "number":
      length = len(start_input)
      while count < length:
        if main_count != 0:
          count = 0
          start_input = input("I need a correct number:\t")
        if start_input == "quit":
          start_input = "quit"
          count = length + 1
        length = len(start_input)
        for x in start_input:
            x = int(base_values[x])
            try:
              digit_val = check_list[x]
              count += 1
            except IndexError:
              count = length - 1
        main_count += 1   
    play = False 
  return start_input, play

def math_time(base_1, base_2, starting_number):
    final_number = ""
    number = number_to_list(starting_number)
    length = len(number)
    print(length)
    count = 0
    intermediate = 0
    base_1, base_2 = int(base_1), int(base_2)
    if base_1 == 1:
      intermediate = len(starting_number)
    else:
      while count < length:
        digit = number[count]
        print(digit)
        digit_val = base_values[digit]
        intermediate += digit_val * (base_1**(length - count - 1))
        count += 1

    x, count = 1,1
    while x <= intermediate:
        x*= base_2
        count += 1
    while count >= 1:
      if x <= intermediate:
          new_digit = intermediate/x
          integer_place = math.floor(new_digit)
          final_number += str(base_values[f"{integer_place}"])
          intermediate -= integer_place*x
      else:
          final_number += "0"
      count -= 1
      x /= base_2
  
    return final_number


def number_to_list(number):
  count = 0
  list_1 = [""]
  while count < len(number):
    bit = number[count]
    list_1.insert(-1,bit)
    count += 1
  number = list_1
  useless = number.pop(-1)
  return number

def restrict_list(base_list, base_1):
    base_1 = base_1
    count = 0
    new_list = []
    new_string = ""
    while count < base_1:
      if count == base_1 -1:
        new_string += f"and {base_list[count]}"
      else:
        new_string += f"{base_list[count]}, "
      new_list.append(base_list[count])
      count += 1
    return new_list, new_string
main()