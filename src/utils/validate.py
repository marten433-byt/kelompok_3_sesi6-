def validate_name(name: str) -> bool:
    if not name or not name.strip():
        return False

    cleaned = name.strip()

    if len(cleaned) < 2:
        return False

    if not all(char.isalpha() or char.isspace() for char in cleaned):
        return False

    return True