def agent():
    max_iters = 10

    for iteration in range(1, max_iters + 1):

        # OBSERVE
        print(f"\nIteration {iteration}")
        observation = input("Observe: ")

        # DECIDE
        if "weather" in observation.lower():
            decision = "Get weather information"
        elif "email" in observation.lower():
            decision = "Send email"
        elif "news" in observation.lower():
            decision = "Search news"
        else:
            decision = "Continue observing"

        print("Decision:", decision)

        # ACT
        if decision == "Get weather information":
            print("Action: Getting weather information...")
            return "success"

        elif decision == "Send email":
            print("Action: Sending email...")
            return "success"

        elif decision == "Search news":
            print("Action: Searching news...")
            return "success"

        else:
            print("Action: Continue...")

    # If 10 iterations are completed without success
    return "failure"


result = agent()
print("\nAgent result:", result)