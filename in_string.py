def check_vowels():
    # Código a implementar utilizando input.
    nombre=input()
    #Valentin Del Pino
    A = ("a" in nombre)
    E = ("e" in nombre)
    I = ("i" in nombre)
    O = ("o" in nombre)
    U = ("u" in nombre)
print(f"Contiene a: {A}\nContiene e: {E}\nContiene i: {I}\nContiene o: {O}\nContiene u: {U}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
