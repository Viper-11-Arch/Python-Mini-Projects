import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "😍" : 2,
    "😁" : 4,
    "💓" : 6,
    "😎" : 8
}

symbol_value = {
    "😍" : 3,
    "😁" : 5,
    "💓" : 2,
    "😎" : 4
}

def check_winnings(columns,lines,bet,value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amt = input("Enter the amount to be deposited: $")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter an Valid Amount!")
    return amt




def get_number_of_lines():
    while True:
        lines = input("Enter the Number of line to bet on(1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter an Valid Number of Lines!")
        else:
            print("Enter an Number")
    return lines

def get_bet():
    while True:
        bet = input(f"How much would you like to bet ${MIN_BET} - ${MAX_BET}: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter an Valid Bet Amount!")
        else:
            print("Enter an Valid Number")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount, your current balance ${balance}")
        else:
            break
    print(f"You're betting ${bet} on ${lines} line")
    print(f"Total bet amount: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet, symbol_value)
    print(f"You Won ${winnings}")
    print(f"You won on Lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance: ${balance}")
        start = input("Press Enter to Play/Q to Quit!")
        if start == "q".lower():
            print("Are you Scared! It's Okay! Bye!")
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()