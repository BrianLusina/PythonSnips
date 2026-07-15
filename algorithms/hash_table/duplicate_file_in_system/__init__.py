from collections import defaultdict
from typing import List, Dict


def find_duplicate(paths: List[str]) -> List[List[str]]:
    if not paths:
        return []

    # Dictionary to store the content as key and list of file paths as value
    file_map: Dict[str, List[str]] = defaultdict(list)

    for path in paths:
        values = path.split()
        # Starting at 1 to skip the directory name, Iterate through each file in the current directory path
        for i in range(1, len(values)):
            # Split the file name and content
            name_content = values[i].split("(")
            # Extract content part
            content = name_content[1][:-1]

            directory = values[0]
            file_name = name_content[0]

            # Construct the full file path
            file_path = f"{directory}/{file_name}"

            # Add the file path to the list of the corresponding content
            file_map[content].append(file_path)

    result = []
    # Iterate through the dictionary to find duplicates
    for file_path_value in file_map.values():
        # Only add to result if there are more than one file with the same content
        if len(file_path_value) > 1:
            result.append(file_path_value)

    return result
