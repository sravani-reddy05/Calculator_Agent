def agent():
    log = []

    for i in range(3):
        log.append(f"Step {i+1}: Observe")
        log.append(f"Step {i+1}: Decide")
        log.append(f"Step {i+1}: Act")

    return log

print(agent())