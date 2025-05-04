def parse_multiplicity(multiplicity):
    """Парсит строку multiplicity и возвращает min и max."""
    if ".." in multiplicity:
        min_val, max_val = multiplicity.split("..")
    else:
        min_val = multiplicity
        max_val = multiplicity
    return min_val, max_val