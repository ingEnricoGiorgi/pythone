class Letter:
    def __init__(self, letterFrom, letterTo):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self._body = []

    def addLine(self, line):
        self._body.append(line)

    def getText(self):
        text = f"Dear {self._letterTo}:\n\n"
        for line in self._body:
            text += line + "\n"
        text += "\nSincerely,\n\n" + self._letterFrom
        return text


# Programma di collaudo
letter = Letter("Trump", "Elon")
letter.addLine("You're fired")
letter.addLine("I wish you all the best.")
print(letter.getText())
