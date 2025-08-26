from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),               # A is either a knight or a knave
    Not(And(AKnight, AKnave)),         # A cannot be both
    Implication(AKnight, And(AKnight, AKnave)),  # If A is a knight, his statement is true
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a knave, his statement is false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),  # A tells truth only if he is a knight
    Implication(AKnave, Not(And(AKnave, BKnave))) # A lies if he is a knave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # A’s statement true if same kind
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), # A’s statement false if knave
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),   # B’s statement true if different kinds
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # B lies if knave
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # B's first statement depends on A's unknown statement
    Implication(BKnight, Or(And(AKnight, AKnave), And(AKnave, AKnight))), # B tells truth if knight
    Implication(BKnave, Not(Or(And(AKnight, AKnave), And(AKnave, AKnight)))), # B lies if knave

    # B's second statement
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C’s statement
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
