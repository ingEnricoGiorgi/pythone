class Student:
    def __init__(self, name):
        self._name = name
        self._quiz_scores = []

    def getName(self):
        return self._name

    def addQuiz(self, score):
        self._quiz_scores.append(score)

    def getTotalScore(self):
        return sum(self._quiz_scores)

    def getAverageScore(self):
        if len(self._quiz_scores) == 0:
            return 0
        return sum(self._quiz_scores) / len(self._quiz_scores)
    
student1 = Student(name="Marco Rossi")

# Aggiungere i punteggi dei quiz
student1.addQuiz(85)
student1.addQuiz(92)
student1.addQuiz(78)
student1.addQuiz(90)

# Ottenere e stampare le informazioni
nome = student1.getName()
punteggio_totale = student1.getTotalScore()
media = student1.getAverageScore()

# Stampare i risultati
print(f"Nome studente: {nome}")
print(f"Punteggi quiz: {student1._quiz_scores}")
print(f"Punteggio totale: {punteggio_totale}")
print(f"Media dei punteggi: {media:.2f}")