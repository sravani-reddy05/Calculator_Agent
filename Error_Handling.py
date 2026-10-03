def act(action):
    try:
        if action == "search":
            return {"status": "success"}

        else:
            raise Exception("Invalid action")

    except Exception as e:
        return {"status": "error", "message": str(e)}


print(act("hello"))