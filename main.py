import math,sys

base_values = {"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26, "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

base_list = {""}

def main():
  print("Hello, I convert between number-systems \nfor you. Because of my programmers limited \nmental capactiy I only go upto base 36 \n(Covering 0-9 and the English standar alphabet)\n Enter quit to quit anytime")
  base_1, base_2, number_1 = "" , "" , ""
  while base_1 != "quit" and base_2 != "quit" and number_1 != "quit":
    base_1 = input("What's your starting base:\t")
    base_1 = correct_inputs(base_1)
    check_list = restrict_list(base_list, base_1)
    number_1 = input("Starting number:\t")
    number_1 = correct_inputs(number_1, "number")
    base_2 = input("Second base to translate into:\t")
    base_2 = correct_inputs(base_2)
    final_number = math_time(base_1, base_2, number_1)
    print(f"Your answer is:\t{final_number}")


def correct_inputs(start_input, kind = "base", check_list = base_values):
  main_count = 0
  count = 0
  if kind == "base":
    while count < 1:
      if main_count > 0:
        start_input = input("I need a correct value:\t")
      try:
        useless_1 = check_list[start_input]
        count += 1
      except KeyError:
        count = 0
      main_count += 1
  elif kind == "number":
    length = len(start_input)
    while count < length:
      if main_count != 0:
        count = 0
        start_input = input("I need a correct number:\t")
      length = len(start_input)
      try:
        for x in start_input:
          digit_val = base_values[f"{x}"]
          count += 1
      except KeyError:
        count = length - 1
      main_count += 1    

def math_time(base_1, base_2, starting_number):
  final_number = ""
  number = number_to_list(starting_number)
  length = len(number)
  count = 0
  intermediate = 0
  base_1, base_2 = int(base_1), int(base_2)
  while count < length:
    digit = number[count]
    digit_val = base_values[digit]
    intermediate = digit_val * (base_1**(length - count - 1))
    count += 1
  
  x, count = 1,1
  while x <= intermediate:
      x*= base_2
      count += 1
  while count >= 1:
    if x <= intermediate:
        new_digit = intermediate/x
        integer_place = math.floor(new_digit)
        final_number += f"{base_values[integer_place]}"
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

def restrict_list(o_list, base_1):
  base_1 = int(base_1)
  count = 0
  new_list = [""]
  while count < base_1:
    new_list = new_list.append(o_list[count])
    count += 1
  return new_list
main()