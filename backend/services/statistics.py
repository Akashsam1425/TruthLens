import re


def calculate_statistics(text):
    """
    Calculate all document statistics.
    """

    text = text.strip()

    # -------------------------
    # Character Statistics
    # -------------------------

    character_count = len(text)

    character_without_spaces = len(
        text.replace(" ", "")
    )

    # -------------------------
    # Words
    # -------------------------

    words = re.findall(r"\b[\w'-]+\b", text)

    word_count = len(words)

    unique_words = len(
        set(word.lower() for word in words)
    )

    # -------------------------
    # Sentences
    # -------------------------

    sentences = re.split(
        r"[.!?]+",
        text
    )

    sentences = [
        s.strip()
        for s in sentences
        if s.strip()
    ]

    sentence_count = len(sentences)

    # -------------------------
    # Paragraphs
    # -------------------------

    paragraphs = [
        p
        for p in text.split("\n")
        if p.strip()
    ]

    paragraph_count = len(paragraphs)

    # -------------------------
    # Average Word Length
    # -------------------------

    average_word_length = 0

    if word_count > 0:

        average_word_length = round(

            sum(len(word) for word in words)
            / word_count,

            2

        )

    # -------------------------
    # Average Sentence Length
    # -------------------------

    average_sentence_length = 0

    if sentence_count > 0:

        average_sentence_length = round(

            word_count
            / sentence_count,

            2

        )

    # -------------------------
    # Vocabulary Diversity
    # -------------------------

    vocabulary_diversity = 0

    if word_count > 0:

        vocabulary_diversity = round(

            (unique_words / word_count)
            * 100,

            2

        )

    # -------------------------
    # Reading Time
    # -------------------------

    reading_time = max(

        1,

        round(word_count / 200)

    )

    # -------------------------
    # Long / Short Sentences
    # -------------------------

    long_sentences = 0

    short_sentences = 0

    for sentence in sentences:

        length = len(
            sentence.split()
        )

        if length > 25:
            long_sentences += 1

        elif length < 8:
            short_sentences += 1

    # -------------------------
    # Repeated Words
    # -------------------------

    frequency = {}

    for word in words:

        word = word.lower()

        frequency[word] = (

            frequency.get(word, 0)

            + 1

        )

    repeated_words = sum(

        1

        for count in frequency.values()

        if count > 5

    )

    # -------------------------
    # Return Statistics
    # -------------------------

    return {

        "character_count": character_count,

        "character_without_spaces": character_without_spaces,

        "word_count": word_count,

        "unique_words": unique_words,

        "sentence_count": sentence_count,

        "paragraph_count": paragraph_count,

        "average_word_length": average_word_length,

        "average_sentence_length": average_sentence_length,

        "vocabulary_diversity": vocabulary_diversity,

        "reading_time": reading_time,

        "long_sentences": long_sentences,

        "short_sentences": short_sentences,

        "repeated_words": repeated_words

    }