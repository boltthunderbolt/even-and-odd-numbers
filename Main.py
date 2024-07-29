
## Even and Odd Numbers
def main():
  x = int(input("What numbers? "))
  if is_even(x):
    print(f"{x} is Even numbers");
  else :
    print(f"{x} is Odd numbers");

def is_even(numbers):
  return numbers % 2 == 0

main()