torch_lit = True
if torch_lit:
    outcome = "Flicker: I'm safe thanks to the flame."
else:
    outcome = "Doom: death and despair await me."
print(outcome)

has_key = True
if has_key:
    outcome = "Click: there goes the lock."
else:
    outcome = "Doom: I can't get through."
print(outcome)

guard_awake = False
if not guard_awake:
    outcome = "Shadow: the guard will never catch me."
else:
    outcome = "Doom: there's no way to escape."
print(outcome)

drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: not even the greatest storm could stop me."
else:
    outcome = "Doom: I have no way inside."
print(outcome)

escaped = True
if escaped:
    outcome = "Legend: my name will be remebered for centuries!"
else:
    outcome = "Doom: I beleive that I will die here."
print(outcome)
