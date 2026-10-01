# Agentic AI: Observe -> Decide -> Act Loop

for iteration in range(1, 4):   # 3 iterations

    # OBSERVE
    print(f"\nIteration {iteration}")
    environment = input("Observe: Enter current situation: ")

    # DECIDE
    if "weather" in environment.lower():
        decision = "Get weather information"
    elif "email" in environment.lower():
        decision = "Send email reply"
    elif "news" in environment.lower():
        decision = "Search latest news"
    else:
        decision = "Ask user for more details"

    print("Decision:", decision)

    # ACT
    if decision == "Get weather information":
        action = "Fetching weather data..."
    elif decision == "Send email reply":
        action = "Generating email response..."
    elif decision == "Search latest news":
        action = "Searching news..."
    else:
        action = "Requesting more information..."

    print("Action :", action)

print("\nAgent completed 3 iterations.")