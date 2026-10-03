def observe():
    return "Task information" 
def decide(observation):
    return "perform action" 
def act(decision):
    return "success" 
max_iters = 10 
for i in range(max_iters):
    observation=observe() 
    decision=decide(observation) 
    result=act(decision) 
    if result=="success":
        print("Task completed") 
        break 
    else:
        print("failure") 