"""
PROJECT 3 — Text Analyzer (Your first multi-helper function tool)

Write ONE main function + at least TWO helper functions.

Main function: 
analyze_text(text)
Returns a dictionary containing:
1. number of words
2. number of unique words
3. most common word
4. number of sentences

Requirements:
Helper function 1: clean_text(text)
1. lowercase
2. remove punctuation (.,!?)
3. return cleaned string

Helper function 2: split_into_sentences(text)
1. split using ., ?, !
2. return a list of sentences (empty ones removed)

Main logic:
Inside analyze_text(text), you must:
1. clean the text
2. split words
3. count words and unique words
4. find most common word
5. count sentences using helper 2
6. Then return something like:
{
    "words": 22,
    "unique_words": 13,
    "most_common": "apple",
    "sentences": 3
}
"""
def clean_text(text: str) -> str:
    text = text.lower()
    for c in '.,!?': 
        text = text.replace(c, '')
    return text

def split_into_sentences(text: str) -> list:
    import re
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]

def analyze_text(text: str) -> dict:
    text_clean = clean_text(text)
    words = text_clean.split()
    unique_words = set(words)

    # Count word frequencies
    count_words = {}
    for word in words:
        count_words[word] = count_words.get(word, 0) + 1
    
    # Most common word(s)
    max_count = max(count_words.values()) if count_words else 0
    most_common = [w for w, c in count_words.items() if c == max_count]

    sentences = split_into_sentences(text)

    return {
        'Number of words': len(words),
        'Number of unique words': len(unique_words),
        'Most common word': most_common,
        'Number of sentences': len(sentences)
    }

text = input('Enter a paragraph: ')
result = analyze_text(text)
print(result)