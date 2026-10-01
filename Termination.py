def agent(max_iters=10):

    for iteration in range(1, max_iters + 1):

        print(f"\n--- Iteration {iteration} ---")

        # OBSERVE
        observation = input("Observe: ")

        # DECIDE
        if "weather" in observation.lower():
            decision = "Get weather information"
        elif "email" in observation.lower():
            decision = "Send email"
        elif "news" in observation.lower():
            decision = "Search news"
        else:
            decision = "Continue"

        print("Decision:", decision)

        # ACT
        if decision == "Get weather information":
            print("Action: Getting weather information...")
            state = "success"

        elif decision == "Send email":
            print("Action: Sending email...")
            state = "success"

        elif decision == "Search news":
            print("Action: Searching news...")
            state = "success"

        else:
            print("Action: No useful action")
            state = "continue"

        # TERMINATION
        if state == "success":
            print("Agent terminated successfully.")
            return "success"

    # Maximum iterations exceeded
    print("Maximum iterations reached.")
    print("Agent terminated with failure.")
    return "failure"


# Run the agent
result = agent(max_iters=10)

print("\nFinal Result:", result)