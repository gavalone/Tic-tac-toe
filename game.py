from gameparts import Board
from gameparts.exception import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Пожалуйста, введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        adding_text = ''
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            adding_text = f'Победили {current_player}!'
            save_result(adding_text)
            print(adding_text)
            running = False
        elif game.is_board_full():
            adding_text = 'Ничья!'
            save_result(adding_text)
            print(adding_text)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


def save_result(adding_text):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(adding_text + '\n')


if __name__ == '__main__':
    main()