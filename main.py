import random

Phrase_1 = ["You're written in every beat of my heart", 
            "No one else compares to you",
            "You're my favorite kind of magic",
            "I'm lost in everything you are",
            "You're the dream I never want to wake from"]

Pharse_2 = ["With you, I've found my forever",
            "You're the missing piece I didn't know I needed",
            "Every part of me belongs to you",
            "You're my once in a lifetime",
            "I'd choose you in every universe"]


def lyric_mix():
    while True:
        list_1 = Phrase_1.copy()
        list_2 = Pharse_2.copy()
            
        for i in range(1, 6):
            chosen_phrase_1 = random.choice(list_1)
            chosen_phrase_2 = random.choice(list_2)

            list_1.remove(chosen_phrase_1)
            list_2.remove(chosen_phrase_2)

            print(f"{str(i)}. {chosen_phrase_1}, {chosen_phrase_2}")

    
        confirm = input("Would you like to generate 5 more? (yes/no): ").strip().lower()

        if confirm.startswith("n"):
            break
        elif confirm.startswith("y"):
            continue
        else:
            continue

lyric_mix()



