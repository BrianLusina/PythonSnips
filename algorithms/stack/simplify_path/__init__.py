def simplify_path(path: str) -> str:
    # Use a stack to keep track of valid directory names
    directory_stack = []

    # Split the path by '/' to get individual components
    path_components = path.split("/")

    # Process each component in the path
    for component in path_components:
        # Skip empty components (from consecutive slashes) and current directory references
        if not component or component == ".":
            continue

        # Handle parent directory reference
        if component == "..":
            # Pop from stack if not empty (go to parent directory)
            if directory_stack:
                directory_stack.pop()
        else:
            # Add valid directory name to the stack
            directory_stack.append(component)

    # Construct the simplified path from the stack
    # Always start with '/' for absolute path
    simplified_path = "/" + "/".join(directory_stack)

    return simplified_path
