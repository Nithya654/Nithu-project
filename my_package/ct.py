def find_symbol_pair(symbols, num_symbols, target):
    """
    Finds a pair of different symbols whose ASCII values sum to the target.

    Args:
        symbols: A list of strings representing the symbols.
        num_symbols: An integer representing the number of symbols.
        target: An integer representing the target sum.

    Returns:
        A string representing the concatenation of the first pair of symbols
        whose ASCII values sum to the target, or "-1" if no such pair exists.
    """
    for i in range(num_symbols):
        for j in range(num_symbols):
            if i != j:
                if ord(symbols[i]) + ord(symbols[j]) == target:
                    return symbols[i] + symbols[j]
    return "-1"

if __name__ == "__main__":
    try:
        symbols_input = input("Enter the symbols as a comma-separated string (e.g., e,b,c,d): ").split(',')
        num_symbols_input = int(input("Enter the number of symbols: "))
        target_input = int(input("Enter the target number: "))

        if len(symbols_input) != num_symbols_input:
            print("Error: The number of symbols entered does not match the specified count.")
        else:
            result = find_symbol_pair(symbols_input, num_symbols_input, target_input)
            print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for the number of symbols and the target.")