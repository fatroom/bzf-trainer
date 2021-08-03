import json

source = open('questions.txt', 'r').readlines()

i = 0
questions = []
while i < len(source):
    for j in (i, i+2, i+3, i+4, i+5):
        if len(source[j].split('  ')) > 2:
            print(source[j])

    question = {
        "text": source[i].split('  ')[1].strip(),
        "answers": [
            {
                "id": 1,
                "text": source[i + 2].split('  ')[1].strip(),
                "correct": True
            },
            {
                "id": 2,
                "text": source[i + 3].split('  ')[1].strip()
            },
            {
                "id": 3,
                "text": source[i + 4].split('  ')[1].strip()
            },
            {
                "id": 4,
                "text": source[i + 5].split('  ')[1].strip()
            }
        ]
    }
    if source[i + 1].startswith('img: '):
        question['img'] = source[i + 1].split('  ')[1].strip()

    questions.append(question)
    i = i + 7

print(json.dumps(questions))
