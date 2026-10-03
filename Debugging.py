max_iters = 5
i = 0

while i < max_iters:
    observation = "task observed"
    decision = "continue"
    result = "working"

    print("Step:", i + 1)
    print("Observe:", observation)
    print("Decide:", decision)
    print("Act:", result)

    i = i + 1

print("Loop finished")