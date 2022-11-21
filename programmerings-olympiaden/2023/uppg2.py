encrypted_string = input("Kryptosträng ? ")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

solutions = []

def decrypted_solutions(krypto: str, sol: list):
    if len(krypto) < 2:
        if len(krypto) == 1:
            sol.append(letters[int(krypto)-1])
        solutions.append(sol)
        return

    two_digit = int(krypto[0] + krypto[1])
    if two_digit > 29 or two_digit < 10:
        sol.append(letters[int(krypto[0])-1])
        decrypted_solutions(krypto[1:], sol)
    elif two_digit <= 29 and two_digit > 10 and two_digit != 20:
        alt_sol = sol.copy()
        sol.append(letters[int(krypto[0])-1])
        decrypted_solutions(krypto[1:], sol)
        alt_sol.append(letters[two_digit-1])
        decrypted_solutions(krypto[2:], alt_sol)
    elif two_digit == 10 or two_digit == 20:
        sol.append(letters[int(krypto[:2])-1])
        decrypted_solutions(krypto[2:], sol)


decrypted_solutions(encrypted_string, [])
print(solutions)
print("Svar:", len(solutions))