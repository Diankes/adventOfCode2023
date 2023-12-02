import re

num_names = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}
start_end_num_pattern = re.compile(r'\d.*\d|\d')
total_num_pairs = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        for num_name in num_names:
            line = line.replace(num_name, num_names[num_name])
        has_two_nums_or_one_num = re.search(start_end_num_pattern, line)
        if has_two_nums_or_one_num:
            exp_str = has_two_nums_or_one_num.group()
            parsed_num = int(f"{exp_str[0]}{exp_str[-1]}")
            total_num_pairs.append(parsed_num)
print(sum(total_num_pairs))
