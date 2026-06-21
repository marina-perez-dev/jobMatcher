def ask_input(label, type_="str"):
    value = input(f"{label} : ").strip()

    if value == "":
        return "" if type_ == "str" else None

    if type_ == "int":
        try:
            return int(value)
        except ValueError:
            print("Valeur invalide, ignorée.")
            return None

    return value

