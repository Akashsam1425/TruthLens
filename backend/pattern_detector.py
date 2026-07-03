def detect_patterns(text):

    reasons = []

    transition_words = [
        "furthermore",
        "moreover",
        "additionally",
        "in conclusion",
        "therefore",
        "however",
        "thus"
    ]

    text_lower = text.lower()

    count = 0

    for word in transition_words:
        count += text_lower.count(word)

    if count > 5:
        reasons.append(
            "Frequent use of transition words"
        )

    sentences = text.split(".")

    lengths = []

    for sentence in sentences:

        words = sentence.split()

        if len(words) > 0:
            lengths.append(len(words))

    if len(lengths) > 5:

        avg = sum(lengths) / len(lengths)

        variation = max(lengths) - min(lengths)

        if variation < avg:
            reasons.append(
                "Very uniform sentence lengths"
            )

    repeated_phrases = 0

    words = text_lower.split()

    for i in range(len(words) - 2):

        phrase = (
            words[i]
            + " "
            + words[i+1]
            + " "
            + words[i+2]
        )

        if text_lower.count(phrase) > 2:
            repeated_phrases += 1

    if repeated_phrases > 5:
        reasons.append(
            "Repeated phrase patterns detected"
        )

    return reasons