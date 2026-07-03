from services.statistics import calculate_statistics


def analyze_text(text):
    """
    Analyze text and calculate AI suspicion score.
    """

    # -----------------------------
    # Get Statistics
    # -----------------------------

    analysis = calculate_statistics(text)

    ai_score = 0

    # -----------------------------
    # Rule 1
    # Long average sentences
    # -----------------------------

    if analysis["average_sentence_length"] > 20:
        ai_score += 20

    # -----------------------------
    # Rule 2
    # Low vocabulary diversity
    # -----------------------------

    if analysis["vocabulary_diversity"] < 45:
        ai_score += 20

    # -----------------------------
    # Rule 3
    # Many repeated words
    # -----------------------------

    if analysis["repeated_words"] > 10:
        ai_score += 20

    # -----------------------------
    # Rule 4
    # Long sentences dominate
    # -----------------------------

    if analysis["long_sentences"] > analysis["short_sentences"]:
        ai_score += 20

    # -----------------------------
    # Rule 5
    # Very long document
    # -----------------------------

    if analysis["reading_time"] > 5:
        ai_score += 20

    # -----------------------------
    # Limit score
    # -----------------------------

    analysis["ai_score"] = min(ai_score, 100)

    return analysis