print("Willkommen in der Quiz-Arena!")

playing = input("Hast du Lust zum spielen? ")

if playing.lower() != "ja":
    quit()

print("Nice, lass uns anfangen!")
score = 0
answer = input("Woraus besteht Diamant? ")
if answer.lower() == "kohlenstoff":
    print('Richtig! Nächste Frage..')
    score +=1
else:
    print("Falsch! Versuch es mit einer anderen Frage.")

answer = input("Aus wie vielen Eizelnknochen besteht eine menlische Hand? ")
if answer.lower() == "27":
    print('Richtig! Nächste Frage..')
    score +=1
else:
    print("Falsch! Versuch es mit einer anderen Frage.")

answer = input("Wofür stehen die olympische Ringe? ")
if answer.lower() == "5 kontinente":
    print('Richtig! Nächste Frage..')
    score +=1
else:
    print("Falsch! Versuch es mit einer anderen Frage.")

answer = input("Wie hoch ist der Eiffelturm? ")
if answer.lower() == "300m":
    print('Richtig! Nächste Frage..')
    score +=1
else:
    print("Falsch! Versuch es mit einer anderen Frage.")

answer = input("Wie hoch hängt ein Basketballkorb? ")
if answer.lower() == "3,05m":
    print('Richtig! Nächste Frage..')
    score +=1
else:
    print("Falsch!")

print("Du hast " + str(score) + " richtige Antworte.")
print("Du hast " + str((score/5) * 100) + "%")
