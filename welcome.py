from telebot import types
import telebot
from bot import bot

def welcome_(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1.Архитектура и основные составные части систем ИИ")
    item2 = types.KeyboardButton("2.Системы распознавания образов (идентификации)")
    item3 = types.KeyboardButton("3.Адаптация и обучение")
    item4 = types.KeyboardButton("4.Автоматизированный синтез физических принципов действия. Синтез речи.")
    item5 = types.KeyboardButton("5.Методы и алгоритмы анализа структуры многомерных данных.")
    item6 = types.KeyboardButton("6.Языки программирования для решения задач ИИ")
    item7 = types.KeyboardButton("7.Сферы использования языка Python")
    item8 = types.KeyboardButton("8.Методы машинного обучения")
    item9 = types.KeyboardButton("9.Сист подход при разработке КИС")
    item10 = types.KeyboardButton("10.Инф, прогр, технич, матем и др. обеспеч КИС.")
    item11 = types.KeyboardButton("11.Критерии качества и экономической эффективности внедрения и эксплуатации КИС.")
    item12 = types.KeyboardButton("12.Унифицированные способы представления базовых концепций бизнес-процессов. Диаграммы BPMN.")
    item13 = types.KeyboardButton("13.Интеллектуальные системы. Виды, состав, области применения инт.систем.")
    item14 = types.KeyboardButton("14.Экспертные системы. Применение систем поддержки принятия решений.")
    item15 = types.KeyboardButton("15.Сети передачи данных. Локальные и глобальные вычислительные сети.")
    item16 = types.KeyboardButton("16.Принципы организации сети Интернет.")
    item17 = types.KeyboardButton("17.Основные понятия теории сложных систем. Основные принципы системного подхода. Понятие декомпозиции и координации.")
    item18 = types.KeyboardButton("18.Оптимизация сложных систем. Методы оптимизации.")
    item19 = types.KeyboardButton("19")
    item20 = types.KeyboardButton("20.Основные опр-ия и теоремы теории игр. Методы решения задач.")
    item21 = types.KeyboardButton("21.Теория массового обслуживания. Определение характеристик типовых систем массового обслуживания (СМО). Приоритетные СМО.")
    item22 = types.KeyboardButton("22.Методы статистического моделирования СМО.")
    item23 = types.KeyboardButton("23.Имитационное моделирование")
    item24 = types.KeyboardButton("24.Теория расписаний. Задача упорядочения. Функции штрафа. Типовые задачи.")
    item25 = types.KeyboardButton("25.Энтропия дискретных источников сообщений и сложных систем")
    item26 = types.KeyboardButton("26.Идентификация объектов. Метод регрессивного анализа.")
    item27 = types.KeyboardButton("27.Задачи идентификации и классификации. Метод экспертных оценок.")
    item28 = types.KeyboardButton("28.Функциональные характеристики системы. Пространство траекторий функционирования. Функционалы.")
    item29 = types.KeyboardButton("29.Объектно-ориентированный анализ и проектирование.")
    item30 = types.KeyboardButton("30.Понятие жизненного цикла информационной системы. Модели и основные этапы жизненного цикла.")
    item31 = types.KeyboardButton("31.Вычислительные системы. Состав и структура вычислительных систем.")
    item32 = types.KeyboardButton("32")
    item33 = types.KeyboardButton("33.Оптимизация сложный систем. Многокритериальная оптимизация.")
    item34 = types.KeyboardButton("34.Выбор стратегии информационного поиска. Выбор методов адресации данных. Доступ к данным.")
    item35 = types.KeyboardButton("35")
    item36 = types.KeyboardButton("36.Системы отображения информации. Виртуальная реальность.")
    item37 = types.KeyboardButton("37.Динамические системы. Движение системы. Траектории функционирования системы.")
    item38 = types.KeyboardButton("38.Логико-динамическая модель системы.")
    item39 = types.KeyboardButton("39.Системы управления качеством программного обеспечения")
    item40 = types.KeyboardButton("40.Формализованное описание элементов системы и взаимодействия между ними.")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14,
               item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27,
               item28, item29, item30, item31, item32, item33, item34, item35, item36, item37, item38, item39, item40)


    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> ".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
