import hashlib
import os


def find_duplicate_files(directory):
    files_seen = {}
    stack = [directory]
    # track tuples of duplicates (duplicate, original)
    duplicates = []

    while len(stack):
        current_path = stack.pop()

        # it it is a directory put contents in the stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # if it is a file
        else:
            # get its hash
            file_hash = sample_hash_file(current_path)

            # get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # if we have seen it before
            if file_hash in files_seen:
                existing_last_edit_time, existing_path = files_seen[file_hash]

                if current_last_edited_time > existing_last_edit_time:
                    # current file is the duplicate
                    duplicates.append((current_path, existing_path))

                else:
                    # old file is the duplicate
                    duplicates.append((existing_path, current_path))

                    # update files seen already
                    files_seen[file_hash] = (current_last_edited_time, current_path)
            else:
                """
                if it is a new file, throw in files seen already record its path and last edit time
                so we can tell later if it is a duplicate
                """
                files_seen[file_hash] = (current_last_edited_time, current_path)
    return duplicates


def sample_hash_file(current_path):
    num_of_bytes_to_read = 4000
    total_bytes = os.path.getsize(current_path)

    hasher = hashlib.sha512()

    with open(current_path, "rb") as file:
        # if the file is too small to take 3 samples, hash the entire file
        if total_bytes < num_of_bytes_to_read * 3:
            hasher.update(file.read())
        else:
            num_bytes_btwn_samples = (total_bytes - num_of_bytes_to_read * 3) / 2

            # read first, middle and last bytes
            for offset_multiplier in range(3):
                start_of_sample = offset_multiplier * (num_of_bytes_to_read + num_bytes_btwn_samples)
                file.seek(start_of_sample)
                sample = file.read(num_of_bytes_to_read)
                hasher.update(sample)

    return hasher.hexdigest()
