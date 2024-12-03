number = int(input())
array = list(map(int, input().split()))

even_numbers = []
odd_number = []

for i in range(len(array)):
    if i % 2 == 0:
        even_numbers.append(i)

for i in range(len(array)):
    if i % 2 == 1:
        odd_number.append(i)
        
for i in range(1, len(even_numbers)):
    print(even_numbers[i], end = ' ')
    
for i in range(1, len(odd_number)):
    print(odd_number[i], end = ' ')


def main():
    print('Hello world')


def test():
    print("this is test")

    
        




    











