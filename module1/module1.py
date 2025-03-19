while True:
    # Check Collatz' Conjecture for given number
    num = int(input('Enter a number (non-positive to quit): '))
    if num > 0:
        print(num, end='')
        cycles = 1
        while num > 1:
            cycles += 1
            if num % 2 == 0:
                # Even numbers: divide by 2
                num //= 2
            else:
                # Odd numbers: 3n+1
                num = num * 3 + 1
            print(f' -> {num}', end='')
        print(f' (stopping time in {cycles} cycle{'s' if cycles > 1 else ''})')
    else:
        break