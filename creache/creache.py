#!/usr/bin/env python

import re


def eval_type(t: str):

    if t == "String":
        return "String! = ''"
    elif t == "Int":
        return "Int! = 0"
    elif t == "Double" or t == "Float":
        return f"{t}! = 0.0"
    elif t == "Bool":
        return "Bool! = false"


def read_file(file: str):
    with open(file, "r") as f:
        contents = f.readlines()
    return contents


def main(file: str):
    # retrieve array of each line from file
    contents = read_file(file=file)

    swift_contents = [c for c in contents]

    # print(re.search("var.*", swift_contents[1]))
    regex_var_contents = [rc for rc in swift_contents if re.search("var.*", rc)]

    # replace names first
    replaced_vars_with_dynamic_vars = [
        re.sub("var", "@dynamic var", var) for var in swift_contents
    ]

    current_types = [
        re.search(r"(var\s+\w+\W+(?P<type>\w+)(?P<optional>!?))", t)
        for t in regex_var_contents
    ]

    for i in range(len(swift_contents)):
        if re.search(r"^(struct\s+(\w+))", swift_contents[i]):
            name = re.search(r"^struct\s+(?P<name>\w+)", swift_contents[i]).group(
                "name"
            )
            substitute = re.sub(name, f"{name}_Entity", swift_contents[i])
            swift_contents[i] = substitute

        if re.search(r"var", swift_contents[i]):
            substitute = re.sub("var", "@dynamic var", swift_contents[i])
            swift_contents[i] = substitute

        if re.search(r"(var\s+\w+\W+(?P<type>\w+)(?P<optional>!?))", swift_contents[i]):
            typed = re.search(
                r"(var\s+\w+\W+(?P<type>\w+)(?P<optional>!?))", swift_contents[i]
            )
            substitute = re.sub(
                r"(?<=:\s)(\w+)(!?)",
                eval_type(typed.group("type")),
                swift_contents[i],
            )
            swift_contents[i] = substitute

    refactored = re.findall(
        r"^struct.*|^\s+@dynamic var.*|\s^}$", "\n".join(swift_contents), re.M
    )

    with open("./User_Entity.swift", "w") as f:
        f.writelines(refactored)

    print("Wrote to User_Entity.swift")


def run(file: str):
    main(file=file)


def random():
    print("Random words here")
