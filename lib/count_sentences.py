#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string")
        self.value = value

    def is_sentence(self):
        """Check if the value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Check if the value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Check if the value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Count the number of sentences in the value."""
        sentence_endings = ['.', '?', '!']
        sentences = [sentence.strip() for sentence in self.value.split() if sentence.endswith(tuple(sentence_endings))]
        return len(sentences)
