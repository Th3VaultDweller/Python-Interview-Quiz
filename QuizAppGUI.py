# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuizAppGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

import quiz
# вопросы и ответы будут дублироваться в консоли
from quiz import random_question


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.ChangeLanguageButton = QtWidgets.QToolButton(Dialog)
        self.ChangeLanguageButton.setAcceptDrops(False)
        self.ChangeLanguageButton.setObjectName("ChangeLanguageButton")
        self.verticalLayout.addWidget(self.ChangeLanguageButton)

        self.Question = QtWidgets.QLabel(Dialog)
        self.Question.setMouseTracking(False)
        self.Question.setAutoFillBackground(True)
        self.Question.setScaledContents(True)
        self.Question.setWordWrap(True)
        self.Question.setObjectName("Question")
        self.verticalLayout.addWidget(self.Question)

        self.Answer = QtWidgets.QLabel(Dialog)
        self.Answer.setAutoFillBackground(True)
        self.Answer.setScaledContents(False)
        self.Answer.setWordWrap(True)
        self.Answer.setOpenExternalLinks(True)
        self.Answer.setObjectName("Answer")
        self.verticalLayout.addWidget(self.Answer)

        self.ShowRandomQuestionButton = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.ShowRandomQuestion()
        )
        self.ShowRandomQuestionButton.setObjectName("ShowRandomQuestionButton")
        self.verticalLayout.addWidget(self.ShowRandomQuestionButton)

        if self.ShowRandomQuestionButton.clicked:
            self.ShowAnswerButton = QtWidgets.QPushButton(
                Dialog, clicked=lambda: self.ShowAnswer()
            )
            self.ShowAnswerButton.setObjectName("ShowAnswerButton")
            self.verticalLayout.addWidget(self.ShowAnswerButton)
        else:
            self.ShowAnswerButton.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ChangeLanguageButton.setText(_translate("Dialog", "Язык приложения"))
        self.Question.setText(_translate("Dialog", "Вопрос"))
        self.Answer.setText(_translate("Dialog", "Ответ"))
        self.ShowAnswerButton.setText(_translate("Dialog", "Показать ответ"))
        self.ShowRandomQuestionButton.setText(_translate("Dialog", "Случайный вопрос"))

    def ShowRandomQuestion(self):
        """Показать случайный вопрос по нажатию кнопки"""
        self.Question.setText(random_question)

    def ShowAnswer(self):
        if "Что такое Middleware?" in random_question:
            self.Answer.setText(
                "Middleware — это промежуточное программное обеспечение, которое располагается между приложением и сетевыми службами. \nОсновная цель middleware — обработка запросов и ответов между клиентом и сервером."
            )
        if (
            "Какая разница в быстродействии между Django и Flask и почему?"
            in random_question
        ):
            self.Answer.setText(
                "Django чуть медленнее Flask из-за своей более высокой функциональности и накладных расходов. Однако на практике разница в скорости работы между ними незначительна для большинства веб-приложений.\nFlask может быть немного быстрее при обработке простых запросов, но Django лучше масштабируется при увеличении нагрузки благодаря встроенным инструментам кэширования и оптимизации.\nКроме того, производительность в большей степени зависит от архитектуры и качества кода конкретного приложения."
            )
        if "Что такое протоколы?" in random_question:
            self.Answer.setText(
                "Протоколы — это соглашения, которые определяют интерфейс класса и поведение его объектов. Протоколы задаются с помощью специальных методов, таких как str, len и другие. Они позволяют классам работать с различными функциями и операторами языка.\nРеализуя протоколы можно интегрировать классы в языке и делать их поведение естественным и интуитивным. В Python есть протоколы для чисел, итераторов, контекстных менеджеров, атрибутов и других областей. Встроенные и сторонние библиотеки полагаются на стандартные протоколы."
            )
        if (
            "Можно ли объявлять функцию внутри другой функции? Где она будет видна?"
            in random_question
        ):
            self.Answer.setText(
                "Да, функции можно объявлять внутри других функций. Такая вложенная функция будет видна и доступна для вызова только внутри родительской функции, в которой она определена. Это называется замыканием и позволяет ограничить область видимости вложенной функции, чтобы она не загрязняла глобальное пространство имен.\nВложенные функции могут быть полезны, когда нужно реализовать вспомогательную логику, связанную только с работой родительской функции."
            )
        if "Что такое await?" in random_question:
            self.Answer.setText(
                "Await используется для работы с асинхронным кодом и корутинами. Его можно применять только внутри асинхронной функции, определенной с async def.\nAwait позволяет избежать блокировки основного потока программы во время ожидания результатов asynс-функций. Await делает возможным использование асинхронного кода в синхронном стиле последовательно.\nПри вызове await передается управление обратно событийному циклу. Выполнение функции приостанавливается до завершения await-выражения.\nЧаще всего await используется при вызове асинхронных функций и методов — для ожидания результата. Await также может применяться к объектам asyncio.Future и asyncio.Task для ожидания их завершения.\nЕсли await вызывается для корутины, то выполнение текущей корутины приостанавливается до завершения той, которая вызвана."
            )
        if "Что такое async?" in random_question:
            self.Answer.setText(
                "Async — это синтаксис для создания асинхронного кода на основе корутин. Асинхронное программирование позволяет выполнять операции вне основного потока выполнения программы. С помощью async def определяются асинхронные функции-корутины. Такие функции не выполняются сразу, а возвращают объект-корутину. Для запуска корутин используется await. Это передает управление обратно в событийный цикл до завершения корутины.\nAsyncio — стандартный модуль для работы с асинхронным кодом. Он содержит событийный цикл и различные классы. Асинхронный код усложняет логику программы, но позволяет добиться большей производительности за счет неблокирующих вызовов.\nКорутины полезны для операций ввода/вывода, ожидания сети, обращения к БД — там, где нужно не блокировать основной поток."
            )
        # Общие вопросы по Computer Science и Web Development
        if "Что такое инженерия и процесс разработки в целом?" in random_question:
            self.Answer.setText()
        if "Какие знаете принципы программирования?" in random_question:
            self.Answer.setText()
        if (
            "Чем отличаются процедурная и объектно-ориентироавнная парадигмы программирования?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Какие основные принципы ООП (наследование, инкапсуляция, полиморфизм)?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое множественное наследование?" in random_question:
            self.Answer.setText()
        if (
            "Какие есть шесть этапов разработки продукта в Software Development lifecycle и какая разница между Agile и Kanban?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Какие есть методы HTTP-запросов и какая между ними разница?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Какие есть методы HTTP-запросов и какая между ними разница?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое авторизация и как она работает?" in random_question:
            self.Answer.setText()
        if "Что такое cookies?" in random_question:
            self.Answer.setText()
        if "Что такое веб-уязвимость?" in random_question:
            self.Answer.setText()
        if "Какие знаете классические базы данных?" in random_question:
            self.Answer.setText()
        if (
            "Как читать спецификацию в конкретном языке (например, PEP8 в Python)?"
            in random_question
        ):
            self.Answer.setText()
        if "Как происходит взаимодействие клиента и сервера?" in random_question:
            self.Answer.setText()
        if "Какие есть подходы к проектированию API?" in random_question:
            self.Answer.setText()
        if "Как использовать паттерны программирования?" in random_question:
            self.Answer.setText()
        if "Что такое Acceptance Testing и зачем его используют?" in random_question:
            self.Answer.setText()
        if "Что такое модульные и интеграционные тесты, API-тесты?" in random_question:
            self.Answer.setText()
        if "Как писать unit-тесты?" in random_question:
            self.Answer.setText()
        if "Какие есть best practices в написании автотестов?" in random_question:
            self.Answer.setText()
        if "Какие базовые команды системы контроля версий?" in random_question:
            self.Answer.setText()
        if "Как использовать Git?" in random_question:
            self.Answer.setText()
        if "В чем разница между хешированием и шифрованием?" in random_question:
            self.Answer.setText()
        # Python
        if "Python - интерпретируемый язык или компилируемый?" in random_question:
            self.Answer.setText()
        if "Какие есть меняющиеся и постоянные типы данных?" in random_question:
            self.Answer.setText()
        if "Что такое область видимости переменных?" in random_question:
            self.Answer.setText()
        if "Что такое introspection?" in random_question:
            self.Answer.setText()
        if "Разница между is и ==?" in random_question:
            self.Answer.setText()
        if "Разница между __init __ () и __new __ ()?" in random_question:
            self.Answer.setText()
        if "В чем разница между потоками и процессами?" in random_question:
            self.Answer.setText()
        if "Какие есть виды импорта?" in random_question:
            self.Answer.setText()
        if "Что такое класс, итератор, генератор?" in random_question:
            self.Answer.setText()
        if "Что такое метакласс, переменная цикла?" in random_question:
            self.Answer.setText()
        if "В чем разница между итераторами и генераторами?" in random_question:
            self.Answer.setText()
        if "В чем разница между staticmethod и classmethod?" in random_question:
            self.Answer.setText()
        if "Как работают декораторы, контекстные менеджеры?" in random_question:
            self.Answer.setText()
        if (
            "Как работают dict comprehension, list comprehension и set comprehension?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Можно ли использовать несколько декораторов для одной функции?"
            in random_question
        ):
            self.Answer.setText()
        if "Можно ли создать декоратор из класса?" in random_question:
            self.Answer.setText()
        if (
            "Какие есть основные популярные пакеты (requests, pytest, etc)?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое lambda-функции?" in random_question:
            self.Answer.setText()
        if "Что означает *args, **kwargs и как они используются?" in random_question:
            self.Answer.setText()
        if "Что такое exceptions, <try-except>?" in random_question:
            self.Answer.setText()
        if (
            "Что такое PEP (Python Enhancement Proposal), какие из них знаете (PEP 8, PEP 484)?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Какие есть типы данных и какая разница между list и tuple, зачем они?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Как использовать встроенные коллекции (list, set, dictionary)?"
            in random_question
        ):
            self.Answer.setText()
        if "В чем заключается сложность доступа к элементам dict?" in random_question:
            self.Answer.setText()
        if (
            "Как создается объект в Python, для чего __new__, зачем __init__?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Что такое шаблонизатор и как в нем выполнять базовые операции (объединять участки шаблона, выводить дату, выводить данные с серверной стороны)?"
            in random_question
        ):
            self.Answer.setText()
        if "Как Python работает с HTTP-сервером?" in random_question:
            self.Answer.setText()
        if "Что происходит, когда создается виртуальная среда?" in random_question:
            self.Answer.setText()
        if "Async Python: как работает, зачем, что под капотом?" in random_question:
            self.Answer.setText()
        if "Что такое модель памяти Python?" in random_question:
            self.Answer.setText()
        if (
            "Что такое SQLAlchemy (Core и ORM частей) и какие есть альтернативы?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Принципы работы и механизм Garbage collection, reference counting?"
            in random_question
        ):
            self.Answer.setText()
        if "Как работает thread locals?" in random_question:
            self.Answer.setText()
        if "Что такое _slots_?" in random_question:
            self.Answer.setText()
        if (
            "Как передаются аргументы функций в Python (by value or reference)?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое type annotation?" in random_question:
            self.Answer.setText()
        if (
            "Для чего используют нижние подчеркивания в именах классов?"
            in random_question
        ):
            self.Answer.setText()
        if (
            "Каким образом можно запустить код на Python параллельно?"
            in random_question
        ):
            self.Answer.setText()
        if "Как работать с stdlib?" in random_question:
            self.Answer.setText()
        if "Что такое дескрипторы?" in random_question:
            self.Answer.setText()
        # Базы данных
        if (
            "Какие есть базовые методы работы с SQL- базой данных в Python?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое SQL-транзакция?" in random_question:
            self.Answer.setText()
        if "Как сделать выборку из SQL-базы с простой агрегацией?" in random_question:
            self.Answer.setText()
        if (
            "Как выглядит запрос, который выполняет JOIN между таблицами и к самим себе?"
            in random_question
        ):
            self.Answer.setText()
        if "Как отправлять запросы в SQL-базу данных без ORM?" in random_question:
            self.Answer.setText()
        if "Разница между SQL и NoSQL?" in random_question:
            self.Answer.setText()
        if "Как оптимизировать SQL-запросы?" in random_question:
            self.Answer.setText()
        if "Какие есть уровни изоляции транзакций?" in random_question:
            self.Answer.setText()
        if "Какие есть виды индексов?" in random_question:
            self.Answer.setText()
        if (
            "Работали ли с Docker-контейнерами, объяснить основные термины K8s (кластер, pod, node, deployment, service), что такое Kibana?"
            in random_question
        ):
            self.Answer.setText()
        # Алгоритмы
        if "Что такое алгоритмы (например, Big-O notation)?" in random_question:
            self.Answer.setText()
        if "Какие есть базовые алгоритмы сортировки?" in random_question:
            self.Answer.setText()
        if "Что такое Bubble Sort и как это работает?" in random_question:
            self.Answer.setText()
        if "Что такое линейная сложность сортировки?" in random_question:
            self.Answer.setText()
        # Middle вопросы
        if "Что такое многопоточность?" in random_question:
            self.Answer.setText()
        if "Что такое архитектура веб сервисов?" in random_question:
            self.Answer.setText()
        if "Как написать, задеплоить и поддерживать (микро) сервис?" in random_question:
            self.Answer.setText()
        if "Как масштабировать API?" in random_question:
            self.Answer.setText()
        if "Как проводить Code review?" in random_question:
            self.Answer.setText()
        if (
            "Что такое абстрактная фабрика, как ее реализовать и зачем ее применяют?"
            in random_question
        ):
            self.Answer.setText()
        if "Что такое цикломатическая сложность?" in random_question:
            self.Answer.setText()
        if (
            "Что такое временная сложность алгоритма (time complexity)?"
            in random_question
        ):
            self.Answer.setText()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
