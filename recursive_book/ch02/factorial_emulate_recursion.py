# The explicit call stack, which holds "frame objects". --> 1
callStack = []
# "Call" the "factorial() function". --> 2
callStack.append({'returnAddr': 'start', 'number': 5})
return_value = None

while len(callStack) > 0:
    # The body of the "factorial() function":
    number = callStack[-1]['number']  # Set number parameter.
    returnAddr = callStack[-1]['returnAddr']
    if returnAddr == 'start':
        if number == 1:
            # BASE CASE
            return_value = 1
            callStack.pop()  # "Return" from "function call". 3
            continue
        else:
            # RECURSIVE CASE
            callStack[-1]['returnAddr'] = 'after recursive call'
            # "Call" the "factorial() function": # --> 4
            callStack.append({'returnAddr': 'start', 'number': number - 1})
            continue
    elif returnAddr == 'after recursive call':
        return_value *= number
        callStack.pop()  # "Return from function call". 5
        continue

print(return_value)
