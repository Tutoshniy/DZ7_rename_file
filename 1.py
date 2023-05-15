import os


def group_rename_files(new_name: str, num_digits: int, source_ext: str, file_ext: str, name_range=None):
    counter = 1
    for filename in os.listdir('.'):
        if filename.endswith(source_ext):
            if name_range:
                original_name = filename[name_range[0] - 1:name_range[1]]
                new_filename = f'{original_name}{new_name}_{str(counter).zfill(num_digits)}{file_ext}'
            else:
                new_filename = f'{new_name}_{str(counter).zfill(num_digits)}{file_ext}'
            os.rename(filename, new_filename)
            counter += 1


if __name__ == "__main__":
    group_rename_files("прикол", 3, '.txt', '.txt', [1, 4])
