def count_occurance():
    counter = 0

    for i in range(0, 1000):

        if i % 2 == 0 and '9' in str(i):  # for example if we wanted to count even and number should have 9 in it.
            print(f"number is={i}")
            counter += 1

    print(f"counter {counter}")


count_occurance()
