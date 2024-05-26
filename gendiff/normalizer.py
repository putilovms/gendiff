def normalize_value(v, quoted=False):
    if isinstance(v, bool):
        return str(v).lower()
    elif v is None:
        return 'null'
    elif isinstance(v, str):
        return f"'{v}'" if quoted else v
    else:
        return str(v)
