def parse_port(value):
    if isinstance(value, bool):
        raise TypeError("port must be int or str")

    if isinstance(value, int):
        port = value
    elif isinstance(value, str):
        value = value.strip()
        if not value.isdigit():
            raise ValueError("port must contain only digits")
        port = int(value)
    else:
        raise TypeError("port must be int or str")

    if port < 1 or port > 65535:
        raise ValueError("port out of range")

    return port
