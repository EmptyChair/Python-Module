
tags = """BHU NEP LIB DOM HAI ALS""".split()

output = ""
for tag in tags:
    output += f"command = {{ type = end_guarantee which = USA where = {tag} }}\n"
    output += f"command = {{ type = end_access which = {tag} when = 1 }}\n"
    output += f"command = {{ type = military_control which = USA where = {tag} when = 0 }}\n"

print(output)