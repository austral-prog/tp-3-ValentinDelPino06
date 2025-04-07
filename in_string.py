def check_vowels():
    # Código a implementar utilizando input.
    nombre=input()
    #Valentin Del Pino
    vocala = ("a" in nombre)
    vocale = ("e" in nombre)
    vocali = ("i" in nombre)
    vocalo = ("o" in nombre)
    vocalu = ("u" in nombre)
print(f"Contiene a: {vocala}\nContiene e: {vocale}\nContiene i: {vocali}\nContiene o: {vocalo}\nContiene u: {vocalu}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
