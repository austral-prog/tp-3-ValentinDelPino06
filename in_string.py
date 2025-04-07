def check_vowels():
    # Código a implementar utilizando input.
    nombre = input()
    nombre = nombre.lower()  # Para asegurar que detecta vocales sin importar mayúsculas/minúsculas

    vocala = "a" in nombre
    vocale = "e" in nombre
    vocali = "i" in nombre
    vocalo = "o" in nombre
    vocalu = "u" in nombre

    print(f"Contiene a: {vocala}")
    print(f"Contiene e: {vocale}")
    print(f"Contiene i: {vocali}")
    print(f"Contiene o: {vocalo}")
    print(f"Contiene u: {vocalu}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
