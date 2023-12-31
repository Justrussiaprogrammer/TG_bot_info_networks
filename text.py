START_TEXT = ("Приветствуем в нашем боте, пользователь! Всем нашем небольшим коллективом поздравляем тебя с новым "
              "годом! Надеемся у тебя все сложится как нельзя лучше в новом году, без негативных сюрпризов! Немного "
              "удачи, немного оптимизма - и ты сможешь преодолеть все преграды! Ну мы надеемся, по крайней мере)"
              "\n\nДля получения всей информации о боте введи команду /help")
HELP_TEXT = ("/start - вводное сообщение\n"
             "/help - набор команд\n"
             "/get - выбор типа запроса, потребуется пройти серию действий.\nДля сброса последовательности вызовите "
             "любую /команду\n"
             "/echo - вернет эхо")
ECHO_TEXT = "Эхо вернулось!"
ANOTHER_TEXT = "Ты написал что-то не то, но сервер пашет! Напиши /help"


GET_FUNCTION_TEXT = 'Какую информацию об обучении нейросетей нужно получить?'
GET_FILENAME_TEXT = 'Из какого файла брать нейросеть?'

INPUT_VALUES = ('Введите номера столбцов обработки через запятую - или целые положительные числа, или в виде '
                'диапазона (например, 2 - 5), или одного столбца (например, 3)')
INPUT_TIME = 'Теперь введите период запроса в формате HH:MM'
INPUT_TIMES = 'Теперь введите период запроса в формате "HH:MM HH:MM"'

SUCCESS_PLOT = 'Ваш график: 🫱'

NEGATIVE_ERROR = 'Одно из введенных чисел - отрицательное, повторите ввод'
HOUR_ERROR = 'Ошибка в вводе часов, повторите ввод'
MINUTE_ERROR = 'Ошибка в вводе минут, повторите ввод'
INPUT_ERROR = 'Формат ввода неверный, повторите ввод'
QUERY_ERROR = 'Неправильный ввод, попробуйте еще раз :)'

GET_BACK = 'Предыдущий шаг'

MIN_FUNCTION = 'минимум'
MAX_FUNCTION = 'максимум'
PLOT_FUNCTION = 'график'
VALUE_FUNCTION = 'значение'
MEAN_FUNCTION = 'среднее'
DEVIATION_FUNCTION = 'отклонение'
VARIANCE_FUNCTION = 'дисперсия'
GET_INFO_FUNCTION = 'информация о файле'
MEDIAN_FUNCTION = 'медиана'
ALL_FUNCTIONS = [MIN_FUNCTION, MAX_FUNCTION, PLOT_FUNCTION, VALUE_FUNCTION, MEAN_FUNCTION, DEVIATION_FUNCTION,
                 VARIANCE_FUNCTION, GET_INFO_FUNCTION, MEDIAN_FUNCTION]

FIRST_FILENAME = 'train1.csv'
SECOND_FILENAME = 'train2.csv'
THIRD_FILENAME = 'train3.csv'
FOURTH_FILENAME = 'train4.csv'
FIFTH_FILENAME = 'train5.csv'
ALL_FILENAMES = [FIRST_FILENAME, SECOND_FILENAME, THIRD_FILENAME, FOURTH_FILENAME, FIFTH_FILENAME, GET_BACK]

URL = './archive/'
