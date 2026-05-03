def normalize(text):
    return text.lower().strip()


def map_syllabus(extracted_topics, syllabus_topics):
    # 🔥 Apply normalization here
    extracted_set = set([normalize(t["topic"]) for t in extracted_topics])
    syllabus_set = set([normalize(s) for s in syllabus_topics])

    covered = extracted_set & syllabus_set
    missing = syllabus_set - extracted_set

    return {
        "covered": list(covered),
        "missing": list(missing)
    }