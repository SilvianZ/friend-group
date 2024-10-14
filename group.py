"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import numpy as np  # type: ignore

liu_uz = {"name": "Zhijing Liu", "age": "22", "job": "a student"}
silvian = {"name": "Xinyao Zhuang", "age": "22", "job": "a student"}
Jill = {"name": "Jill", "age": "26", "job": "a biologist"}
Zalika = {"name": "Zalika", "age": "28", "job": "an artist"}
John = {"name": "John", "age": "27", "job": "a writer"}
Nash = {"name": "Nash", "age": "34", "job": "a chef"}


my_group = [Jill, Zalika, John, Nash, liu_uz, silvian]

groupmate_name = []
modified_rows = []

for row in my_group:
    groupmate_name.append(row["name"])

# print(groupmate_name)
# print(my_group)

n = len(groupmate_name)

# initialize
connect_matrix = np.zeros((n, n), dtype=object)

# 填充关系
connect_matrix[0][1] = connect_matrix[1][0] = "friend"
connect_matrix[0][2] = connect_matrix[2][0] = "partner"
connect_matrix[2][3] = connect_matrix[3][2] = "cousin"
connect_matrix[3][1] = "landlord"
connect_matrix[4][5] = connect_matrix[5][4] = "classmate"

# print(connect_matrix)

for i, information in enumerate(my_group):
    relationships = []
    if "age" in information and "job" in information:
        for j, relation in enumerate(connect_matrix[i]):
            if relation:
                relationships.append(f"{relation} with {groupmate_name[j]}")
        print(f"{information['name']} is {information['age']}, {information['job']}, and has the following relationships: {','.join(relationships)}.")
    # elif "age" not in i and "job" in i:
    #     print(i["name"], "is", i["age"], ",", i["job"])
    # elif "job" not in i and "age" in i:
    #     print(i["name"], "is", i["age"], ".")
    # else:  # having no job and age information
    #     print(i["name"], "is one of the group members.")

