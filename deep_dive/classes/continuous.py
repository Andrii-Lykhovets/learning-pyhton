class PresentContinuous:
    def __init__(self, subject, auxiliary, infinitive):
        self.subject = subject
        self.auxiliary = auxiliary
        self.infinitive = infinitive

    def affirmative(self):

        return f'{self.subject} {self.auxiliary} {self.infinitive}ing.'

    def negative(self):
        return f'{self.subject} {self.auxiliary} not {self.infinitive}ing.'

    def question(self):
        return f'{self.auxiliary} {self.subject} {self.infinitive}ing?'


class ToBeInPresentContinuous(PresentContinuous):
    def __init__(self, subject, auxiliary, infinitive):
        super().__init__(subject, auxiliary, infinitive)

    def question(self):
        if self.subject == 'I':
            return super().question().capitalize().replace(' Be ', ' Am ').replace(' i ', ' I ')
        elif self.subject in ['You', 'We', 'They']:
            if self.subject == ' you ':
                return super().question().capitalize().replace(' you ', ' You ').replace(self.auxiliary, ' are ')
            elif self.subject == ' we ':
                return super().question().capitalize().replace(' we ', ' We ').replace(self.auxiliary, ' are ')
            elif self.subject == ' they ':
                return super().question().capitalize().replace(' they ', ' They ').replace(self.auxiliary, ' are ')
        elif self.subject in ['He', 'She', 'It']:
            return super().question().capitalize().replace(self.auxiliary, ' is ')

    def affirmative(self):
        if self.subject == 'I':
            return super().affirmative().replace(' be ', ' am ')
        elif self.subject in ['You', 'We', 'They']:
            return super().affirmative().replace(' be ', ' are ')
        elif self.subject in ['He', 'She', 'It']:
            return super().affirmative().replace(' be ', ' is ')

    def negative(self):
        if self.subject == 'I':
            return super().negative().replace(' be ', ' am ')
        elif self.subject in ['You', 'We', 'They']:
            return super().negative().replace(' be ', ' are ')
        elif self.subject in ['He', 'She', 'It']:
            return super().negative().replace(' be ', ' is ')


print('C O N T I N U O U S')
i_component = ToBeInPresentContinuous('I', 'be', 'learn')
you_component = ToBeInPresentContinuous('you', 'be', 'work')
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
print('\n= you_component: \n')
print(affirmative)
print(negative)
print(question)

# infinitives = ['study', 'work', 'start', 'watch', 'speak', 'fly', 'go', 'rain', 'do', 'deny', 'intensify']
# continuous_components = []
# for infinitive in infinitives:
#     continuous_components.append(ToBeInPresentContinuous('I', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('You', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('We', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('They', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('He', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('She', 'be', infinitive))
#     continuous_components.append(ToBeInPresentContinuous('It', 'be', infinitive))
#
# print('\n= loop:\n')
# for component in continuous_components:
#     affirmative = component.affirmative()
#     negative = component.negative()
#     question = component.question()
#     print(affirmative)
#     print(negative)
#     print(question)
#     print()
