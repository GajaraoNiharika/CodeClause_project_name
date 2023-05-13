import time

def typing_test():
    quote = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence:\n", quote)
    input("Press enter to start...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_per_minute = len(user_input.split()) / elapsed_time * 60
    accuracy = sum([1 for i in range(len(user_input)) if user_input[i] == quote[i]]) / len(quote) * 100
    print(f"Your typing speed is {words_per_minute:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")

typing_test()



