sample_tuple = [(10, 20, 30), (1, 2, 3), (2323, 32432, 234189)]
final_tuple = [t[:-1] + (100,) for t in sample_tuple]
print(final_tuple)
