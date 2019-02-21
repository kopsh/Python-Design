qutoes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    def get_qutoe(self, n):
        try:
            return qutoes[n]
        except IndexError as e:
            return "Not Found!"


class QutoeTerminalView:
    def show(self, qutoe):
        print('The quote is {}'.format(qutoe))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_qutoe(self):
        return input('Which quote number would you like to see?')


class QutoeTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QutoeTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_qutoe()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
        quote = self.model.get_qutoe(n)
        self.view.show(quote)


if __name__ == "__main__":
    controller = QutoeTerminalController()
    while True:
        controller.run()
