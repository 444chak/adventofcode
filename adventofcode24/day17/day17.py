import os
import re
import time

start = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

    # Extraire les registres et le programme à partir des chaînes données
    registers_input = [line for line in data if line.startswith("Register")]
    program_input = [line for line in data if line.startswith("Program")]

    # Utiliser des expressions régulières pour extraire les valeurs des registres
    registers = [int(re.search(r"\d+", reg).group()) for reg in registers_input]

    # Utiliser des expressions régulières pour extraire le programme
    program = list(map(int, re.findall(r"\d+", program_input[0])))


print("Registers:", registers)
print("Program:", program)
print("Data loaded\n")


def run_program(registers, program):
    # Initialiser les registres et l'IP (Instruction Pointer)
    A, B, C = registers
    IP = 0
    output = []

    # Définir les fonctions pour chaque opcode
    def adv(operand):
        nonlocal A
        divisor = 2 ** (
            operand
            if operand <= 3
            else (A if operand == 4 else B if operand == 5 else C)
        )
        A //= divisor

    def bxl(operand):
        nonlocal B
        B ^= operand

    def bst(operand):
        nonlocal B
        value = (
            operand
            if operand <= 3
            else (A if operand == 4 else B if operand == 5 else C)
        )
        B = value % 8

    def jnz(operand):
        nonlocal IP
        if A != 0:
            IP = operand
            return True  # Indique que l'IP a été modifié
        return False

    def bxc(_):
        nonlocal B
        B ^= C

    def out(operand):
        value = (
            operand
            if operand <= 3
            else (A if operand == 4 else B if operand == 5 else C)
        )
        output.append(value % 8)

    def bdv(operand):
        nonlocal B
        divisor = 2 ** (
            operand
            if operand <= 3
            else (A if operand == 4 else B if operand == 5 else C)
        )
        B = A // divisor

    def cdv(operand):
        nonlocal C
        divisor = 2 ** (
            operand
            if operand <= 3
            else (A if operand == 4 else B if operand == 5 else C)
        )
        C = A // divisor

    # Dictionnaire des opcodes
    opcodes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    # Boucle d'exécution du programme
    while IP < len(program):
        opcode = program[IP]
        operand = program[IP + 1] if IP + 1 < len(program) else 0

        if opcode in opcodes:
            # Exécuter l'opération associée
            jumped = opcodes[opcode](operand)
            if opcode == 3 and jumped:
                continue  # Évite l'incrémentation de l'IP pour jnz

        # Incrémenter l'IP de 2 après chaque instruction
        IP += 2

    # Retourner la sortie sous forme de chaîne séparée par des virgules
    return ",".join(map(str, output)), registers


# Part 1
output, registers = run_program(registers, program)
print("Part 1:", output)
print(output, registers)

print("-----------")
# Part 2
# avec quelle valeur de A le programme produit une copie de lui-même

# program doit être = à output


# Part 2
# Trouver la valeur de A pour laquelle le programme produit une copie de lui-même


testable = [(1, 0)]
for i, a in testable:
    for a_test in range(a, a + 10):
        out = [int(x) for x in run_program([a_test, 0, 0], program)[0].split(",")]
        if out == program[-i:]:
            testable.append((i + 1, a_test * 8))
            if i == len(program):
                print(a_test)

print("Time taken: " + str(round(time.time() - start, 3)) + "s")
