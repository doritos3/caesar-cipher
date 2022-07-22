alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position%26]
    else:
        end_text+=char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)


restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  proceed = input('Would you like to continue? \'yes\' or \'no\'? ').lower()
  if proceed == "no":
    restart = False
    print("Good Bye\n")
  elif proceed !='yes' and proceed!='no':
      proceed = input('Please write a correct response\nWould you like to continue? \'yes\' or \'no\'? ').lower()