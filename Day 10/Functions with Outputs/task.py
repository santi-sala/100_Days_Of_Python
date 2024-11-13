def format_name(f_name, l_name):
    firs_name = f_name.title()
    second_name = l_name.title()
    name = firs_name + " " + second_name
    return name

final_name = format_name("sAnTigo", "sALA")
print(final_name)