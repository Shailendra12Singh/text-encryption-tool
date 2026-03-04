from collections import Counter

def frequency_analysis(text):
    text = text.lower()
    letters = [c for c in text if c.isalpha()]

    if not letters:
        print("No letters found in text.")
        return

    count = Counter(letters)
    most_common = count.most_common(1)[0]

    print("\nLetter Frequency:")
    for letter, freq in count.items():
        print(f"{letter}: {freq}")

    print("\nMost Frequent Letter:", most_common[0])

    # Assume most common letter represents 'e'
    probable_shift = (ord(most_common[0]) - ord('e')) % 26
    print("Probable Shift (assuming 'e' most common):", probable_shift)