# def parse_syllabus(text):
#     # simple split (can improve later)
#     topics = text.split("\n")
#     topics = [t.strip() for t in topics if len(t.strip()) > 3]
#     return topics
def parse_syllabus(text):
    lines = text.split("\n")

    topics = []
    for line in lines:
        line = line.strip()

        if len(line) > 5:
            topics.append(line)

    return topics