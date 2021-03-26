list_of_dicts = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, {"a": 7, "b": 8, "c": 9}]

a_key = "b"
values_of_key = [a_dict[a_key] for a_dict in list_of_dicts]

print(values_of_key)
