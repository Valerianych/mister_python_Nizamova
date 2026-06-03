def grade_by_score(score):
    if score < 0 or score > 100:
        raise ValueError("score out of range")
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "good"
    if score >= 50:
        return "pass"
    return "fail"
