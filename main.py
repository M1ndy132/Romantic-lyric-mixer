import random

Phrase_1 = ["You're written in every beat of my heart", 
            "No one else compares to you",
            "You're my favorite kind of magic",
            "I'm lost in everything you are",
            "You're the dream I never want to wake from"]

Phrase_2 = ["With you, I've found my forever",
            "You're the missing piece I didn't know I needed",
            "Every part of me belongs to you",
            "You're my once in a lifetime",
            "I'd choose you in every universe"]


def lyric_mix():
    while True:
        # Reuse the copy(), helps save us from errors that may pop up with removing from lists while looping within them.
        list_1 = Phrase_1.copy()
        list_2 = Phrase_2.copy()
            
        for i in range(1, 6):
            chosen_phrase_1 = random.choice(list_1)
            chosen_phrase_2 = random.choice(list_2)

            list_1.remove(chosen_phrase_1)
            list_2.remove(chosen_phrase_2)

            print(f"{str(i)}. {chosen_phrase_1}, {chosen_phrase_2}")

        # There defininetly is a better way to end this, but this works for now.
        # Currently, allows for endless regenaration, which could be a feature so not too urgent to correct.
        confirm = input("Would you like to generate 5 more? (yes/no): ").strip().lower()

        if confirm.startswith("n"):
            break
        elif confirm.startswith("y"):
            continue
        else:
            continue


print("We got two lists, each with five phrases.")
print("While it ain't much, we get by.")
print("So hop on in and generate your five romanctic lyrics.")
print("If you do it just right, and have some game to your name, you'll be alright.")

while option := input("Generate or No?: ").strip().capitalize():
    match option:
        case "Generate":
            lyric_mix()
        case "No":
            print("Go and work magic rizzler/ette!!!")
            print("See you next time, maybe you'll be able add your own lines. :)\n" \
            "My smile looks so believable, I know. ")
            break





