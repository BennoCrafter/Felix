import ast


def get_length():
    inp = input("Please enter chars, from which you want the length:")
    if inp[0] == "[" and inp[-1] == "]":
        # list
        string_as_list = ast.literal_eval(inp)
        print(f"You're list has {len(string_as_list)} elements.")
    else:
        print(len(inp))