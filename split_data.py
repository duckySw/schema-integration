import os


def split_file(input_file, num_parts):
    file_size = os.path.getsize(input_file+".ttl")
    part_size = file_size // num_parts
    with open(input_file+".ttl", 'rb') as f:
        for i in range(num_parts):
            if i == 1:
                with open(f'{input_file}_{i}.ttl', 'wb') as part_file:
                    part_file.write(f.read(part_size))


input_file_prefix = 'new.24_cities'
num_parts = 100
split_file(input_file_prefix, num_parts)
