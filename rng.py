def doorcode():
    import random

    first = str(random.randrange(0, 9))
    second = str(random.randrange(0, 9))
    third = str(random.randrange(0, 9))
    fourth = str(random.randrange(0, 9))

    rng = (first + second + third + fourth)

    print(rng)

doorcode()
