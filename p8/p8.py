from util import macro

def start():
  # p0()
  # p1()
  # p2()
  # p3()
  p4()

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

def p0():
  macro.moduleStart("Greet")
  greet_with(location="London", name="Angela")

def p1():
  macro.moduleStart("Paint")

  def paint_calc(height, width, cover):
    import math
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")

  test_h = int(input("Height of wall: "))
  test_w = int(input("Width of wall: "))
  coverage = 5
  paint_calc(height=test_h, width=test_w, cover=coverage)

def p2():
  macro.moduleStart("")

  def prime_checker(number):
    for i in range(2, number):
      if number % i == 0:
        print("Number is Not Prime")
        return
    print("Number is Prime")

  n = int(input("Check this number: "))
  prime_checker(number=n)

def p3():
  macro.moduleStart("Cipher Start")
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
  #e.g.
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  ##HINT: How do you get the index of an item in a list:
  #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
  ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

  def encrypt(text, shift):
    encrypted_text = ""
    for i in text:
      shifted_index = alphabet.index(i) + shift
      if shifted_index > 25: encrypted_text += alphabet[shifted_index - 26]
      else: encrypted_text += alphabet[shifted_index]
    print(encrypted_text)

  def decrypt(text, shift):
    decrypted_text = ""
    for i in text:
      shifted_index = alphabet.index(i) - shift
      if shifted_index < 0: decrypted_text += alphabet[shifted_index + 26]
      else: decrypted_text += alphabet[shifted_index]
    print(decrypted_text)

  if direction == "encode": encrypt(text, shift)
  else: decrypt(text, shift)

def p4():
  macro.moduleStart("Cipher End")
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode": shift_amount *= -1
    for char in start_text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if char in alphabet:
        new_position = alphabet.index(char) + shift_amount
        end_text += alphabet[new_position]
      else: end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

  #TODO-1: Import and print the logo from art.py when the program starts.
  from art import logo
  print(logo)

  #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
  #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
  #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
  #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
  should_end = False
  while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
      should_end = True
      print("Goodbye")

start()