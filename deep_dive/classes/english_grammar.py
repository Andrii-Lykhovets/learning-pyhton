class PresentSimple:
    def __init__(self, subject, auxiliary, infinitive):  # __init__ is a class constructor
        self.subject = subject
        self.auxiliary = auxiliary
        self.infinitive = infinitive

    def affirmative(self):
        if self.subject in ['He', 'She', 'It']:
            if self.infinitive[-1] == 'y':
                return f'{self.subject} {self.infinitive[0:-1]}ies.'  # [0:-1] prends jusq'au la lettre finale
            elif self.infinitive[-1] in ['s', 'x']:
                return f'{self.subject} {self.infinitive[0:-1]}es.'
            elif self.infinitive[-2:] in ['sh', 'ch'] or self.infinitive[-1] == 'o':
                return f'{self.subject} {self.infinitive}es.'
            return f'{self.subject} {self.infinitive}s.'
        return f'{self.subject} {self.infinitive}.'

    def negative(self):
        return f'{self.subject} {self.auxiliary} not {self.infinitive}.'

    def question(self):
        return f'{self.auxiliary} {self.subject} {self.infinitive}?'


class CapitalizedPresentSimple(PresentSimple):
    def __init__(self, subject, auxiliary, infinitive):
        super().__init__(subject, auxiliary, infinitive)

    def question(self):
        return super().question().capitalize().replace(' i ', ' I ')


i_component = CapitalizedPresentSimple('I', 'do', 'learn')
affirmative = i_component.affirmative()
negative = i_component.negative()
question = i_component.question()
print('= i_component: \n')
print(affirmative)
print(negative)
print(question)

infinitives = ['study', 'work', 'start', 'watch', 'speak', 'fly', 'go', 'rain', 'do', 'deny', 'intensify']
sentence_components = []
for infinitive in infinitives:
    sentence_components.append(CapitalizedPresentSimple('I', 'do', infinitive))
    sentence_components.append(CapitalizedPresentSimple('You', 'do', infinitive))
    sentence_components.append(CapitalizedPresentSimple('We', 'do', infinitive))
    sentence_components.append(CapitalizedPresentSimple('They', 'do', infinitive))
    sentence_components.append(CapitalizedPresentSimple('He', 'does', infinitive))
    sentence_components.append(CapitalizedPresentSimple('She', 'does', infinitive))
    sentence_components.append(CapitalizedPresentSimple('It', 'does', infinitive))

print('\n= loop:\n')
for component in sentence_components:
    affirmative = component.affirmative()
    negative = component.negative()
    question = component.question()
    print(affirmative)
    print(negative)
    print(question)
    print()


class PresentContinuous:
    def __init__(self, subject, auxiliary, infinitive):
        self.subject = subject
        self.auxiliary = auxiliary
        self.infinitive = infinitive

    def affirmative(self):
        return f'{self.subject} {self.auxiliary} {self.infinitive}ing.'.capitalize()

    def negative(self):
        return f'{self.subject} {self.auxiliary} not {self.infinitive}ing.'.capitalize()

    def question(self):
        return f'{self.auxiliary} {self.subject} {self.infinitive}ing?'.capitalize().replace(' i ', ' I ')


class ToBeInPresentContinuous(PresentContinuous):
    def __init__(self, subject, infinitive):
        if subject == 'I':
            auxiliary = 'am'
        elif subject in ['he', 'she', 'it']:
            auxiliary = 'is'
        else:
            auxiliary = 'are'
        super().__init__(subject, auxiliary, infinitive)


print('C O N T I N U O U S')
i_component = ToBeInPresentContinuous('I', 'learn')
you_component = ToBeInPresentContinuous('you', 'work')
affirmative = i_component.affirmative()
negative = i_component.negative()
question = i_component.question()
print('= i_component: \n')
print(affirmative)
print(negative)
print(question)

affirmative = you_component.affirmative()
negative = you_component.negative()
question = you_component.question()
print('= you_component: \n')
print(affirmative)
print(negative)
print(question)

infinitives = ['study', 'work', 'start', 'watch', 'speak', 'fly', 'go', 'rain', 'do', 'deny', 'intensify']
continuous_components = []
for infinitive in infinitives:
    continuous_components.append(ToBeInPresentContinuous('I', infinitive))
    continuous_components.append(ToBeInPresentContinuous('you', infinitive))
    continuous_components.append(ToBeInPresentContinuous('we', infinitive))
    continuous_components.append(ToBeInPresentContinuous('they', infinitive))
    continuous_components.append(ToBeInPresentContinuous('he', infinitive))
    continuous_components.append(ToBeInPresentContinuous('she', infinitive))
    continuous_components.append(ToBeInPresentContinuous('it', infinitive))

print('\n= loop:\n')
for component in continuous_components:
    affirmative = component.affirmative()
    negative = component.negative()
    question = component.question()
    print(affirmative)
    print(negative)
    print(question)
    print()
