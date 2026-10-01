state={
    "done":False,
    "stage":0 
} 
max_iters=10 
for i in range(max_iters):
    print(f"Iteration: {i+1}") 
    print("observe") 
    print("Decide")  
    print("Act")
    state["stage"] +=1 
    if state["stage"]==3:
        state["done"]=True 
    if state["done"]: 
        print("success") 
        break 
    else:
        print("Failure") 
print(state)
