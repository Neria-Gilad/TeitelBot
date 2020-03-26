from random import choice

generic_answers = [
    "אני לא מאמין ששאלת את זה",
    "\U0001F914",  # thinking emoji
    "\U0001F926",  # facepalm emoji
    "מה הכוונה?",
    "אולי",
    "זה מסווג",
    "למה זה חשוב פתאום?",

]

generic_universal_truths = [
    "מי ששלם עם עצמו, אוהב פיצה",

]

generic_positive_responses = [
    "בטח!",
]

generic_negative_responses = [
    "אין לי מה להגיד על זה",
    "יכולת להגיד משהו שימושי אבל בחרת להגיד את זה",
    "אין לי סיבה לקחת את זה ברצינות",
    "וואו.",
    "-_-",
]


def generic_answer():
    return choice(generic_answers)


def generic_universal_truth():
    return choice(generic_universal_truths)


def generic_positive_response():
    return choice(generic_positive_responses)


def generic_negative_response():
    return choice(generic_negative_responses)
