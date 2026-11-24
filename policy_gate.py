
def check_action(action, amount=0):
    if action == "payment" and amount > 500:
        return "Approval required"

    return "Action allowed"


print(check_action("payment", 750))
print(check_action("payment", 200))
print(check_action("email", 0))
