import random

while True:
    print("Hello there")
    s = input("Enter Password or summit: ")  # get input from stdin
    i = random.randint(0, len(s))  # process the input
    print(f"New output {i}:  {s}", flush=True)  # prints processed input to stdout
