from core import models

class StateActions:
    def save_log_file(self: 'models.State'):
        with open('states.txt', 'a') as file:
            file.write(f'{state.name}')