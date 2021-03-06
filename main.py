##Rudy Garcia
import math,sys

##Dictionaries
base_values = {"0":0,"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26, "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

base_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]

##Main function that runs
def main():
  x=0
  main_count = 0
  print("Hello, I convert between number-systems \nfor you. Because of my programmers limited \nmental capactiy I only go upto base 36 \n(Covering 0-9 and the English standard alphabet)\nEnter \"quit\" to quit anytime\nDon't put spaces in your inputs!")
  last_number = ""
  last_base = ""
  play = False
  while play != True:
    if main_count == 1:
      print("\nYou can enter \'answer\' to use your last answer as your new input number or last base as your new input base\n")
    base_1 = input("What's your starting base:\t")
    base_1, play = correct_inputs(base_1, last_number, last_base, 1)
    if play != True:
      check_list, new_string = restrict_list(base_list, base_1)
      print(f"Possible digits for starting number:  {new_string}")
      number_1 = input("Starting number:\t")
      number_1, play = correct_inputs(number_1,last_number, last_base, 2, "number", check_list)
      if play != True:
        base_2 = input("Second base to translate into:\t")
        base_2, play = correct_inputs(base_2, last_number, last_base, 3)
        if play!= True:
          final_number = math_time(base_1, base_2, number_1)
          print(f"Your base {base_2} answer is:\t{final_number}\n")
          last_number = final_number
          last_base = base_2
          main_count += 1


##Makes sure user inputs are correct
def correct_inputs(start_input, last_number,last_base, position, kind = "base", check_list = base_list):
  main_count = 0
  count = 0
  play = False
  if kind == "base":
      while count < 1:
        ##reasks for input if the first one didn't work
        if main_count > 0:
          start_input = input("I need a correct value:\t")
        ## implements the use of the last answer for user
        if start_input == "answer" and last_base != "":
          start_input = last_base
          count += 1
        ## Makes sure to end main() if user inputs "quit"
        if start_input == "quit":
          start_input = "quit"
          play = True
          count = 1
        ## keeps trying to esnure user number system base input is correct
        if count != 1:
          try:
            start_input = int(start_input)
            if 1 <= start_input <= 36:
              count += 1
          except ValueError:
            count = 0
        main_count += 1

    ## handles the number input from user
  elif kind == "number":
        length = len(start_input)
        while start_input == "" or length == 0:
          start_input = input("I need a correct number:\t")
          length = len(start_input)
        while count < length:
          ## reasks for input if the first one didn't work
          if main_count != 0 or length == 0:
            start_input = input("I need a correct number:\t")
            count = 0
          ## implements the last answer as an input
          if start_input == 'answer' and last_number != "":
            start_input = last_number
          ## quits main if user inputs "quit"
          if start_input == "quit":
            start_input = "quit"
            count = length + 1
          length = len(start_input)
          ## goes through each letter and make sure its in the list of possible digits for the first base counting system
          if count != length + 1:
            for x in start_input:
                x = int(base_values[x])
                try:
                  useless = check_list[x]
                  count += 1
                except IndexError:
                  count = length - 1
          main_count += 1   
  return start_input, play

## Does the math
def math_time(base_1, base_2, starting_number):
    final_number = ""
    number = number_to_list(starting_number)
    length = len(number)
    count = 0
    intermediate = 0
    base_1, base_2 = int(base_1), int(base_2)
    ## if base one, the value in base 10 is just the length anyways
    if base_1 == 1:
      intermediate = len(starting_number)
    ## counts through the number turning it into base 10, which is the intermediate
    else:
      while count < length:
        digit = number[count]
        digit_val = base_values[digit]
        intermediate += digit_val * (base_1**(length - count - 1))
        count += 1
        
    x, count = 1,1
    ##checks to see how long the resulting number should be based on base_2
    while x <= intermediate/base_2:
        x*= base_2
        count += 1
    ##Counts down by a process called Weighted Division
    while count >= 1:
      if x <= intermediate:
          new_digit = intermediate/x
          integer_place = math.floor(new_digit)
          ## list comprehension takes the digit value and returns the digit
          integer_pos_place = [str for str, value in base_values.items() if value == integer_place]
          digit_place = integer_pos_place[0]

          ##clean up after each weighted division
          final_number += digit_place
          intermediate -= integer_place*x
      else:
          final_number += "0"
      ## clean up 2
      count -= 1
      x /= base_2
    ##takes out extra 0's infront of the number
    while final_number[0] == 0:
      final_number = final_number[1:]
    return final_number

## takes a number as a string and splits the alphanumeric characters as individual elements
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

##This restricts the list of possible digits according to each base
def restrict_list(base_list, base_1):
    base_1 = base_1
    count = 0
    new_list = []
    new_string = ""
    while count < base_1:
      if count == base_1 -1:
        if base_1 != 1:
          new_string += f"and {base_list[count]}"
        if base_1 == 1:
          new_string += f"{base_list[count]}"
      else:
        new_string += f"{base_list[count]}, "
      new_list.append(base_list[count])
      count += 1
    return new_list, new_string

main()