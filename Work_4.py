#Write a 1 to 10 even number? Write a 1 to 10 odd number?

for i in range(1, 11):
  if i % 2 == 0:
    print(i, "Even")
  else:
    print(i, "odd")