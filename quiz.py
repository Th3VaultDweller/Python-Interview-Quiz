import random
import string

questions = [
    "Что такое Middleware?",
    "Какая разница в быстродействии между Django и Flask и почему?",
    "Что такое протоколы?",
    "Можно ли объявлять функцию внутри другой функции? Где она будет видна?",
    "Что такое await?",
    "Что такое async?",
]
answers = [
    "Middleware — это промежуточное программное обеспечение, которое располагается между приложением и сетевыми службами. Основная цель middleware — обработка запросов и ответов между клиентом и сервером.",
    "Django чуть медленнее Flask из-за своей более высокой функциональности и накладных расходов. Однако на практике разница в скорости работы между ними незначительна для большинства веб-приложений. Flask может быть немного быстрее при обработке простых запросов, но Django лучше масштабируется при увеличении нагрузки благодаря встроенным инструментам кэширования и оптимизации. Кроме того, производительность в большей степени зависит от архитектуры и качества кода конкретного приложения.",
    "Протоколы — это соглашения, которые определяют интерфейс класса и поведение его объектов. Протоколы задаются с помощью специальных методов, таких как str, len и другие. Они позволяют классам работать с различными функциями и операторами языка. Реализуя протоколы можно интегрировать классы в языке и делать их поведение естественным и интуитивным. В Python есть протоколы для чисел, итераторов, контекстных менеджеров, атрибутов и других областей. Встроенные и сторонние библиотеки полагаются на стандартные протоколы.",
    "Да, функции можно объявлять внутри других функций. Такая вложенная функция будет видна и доступна для вызова только внутри родительской функции, в которой она определена. Это называется замыканием и позволяет ограничить область видимости вложенной функции, чтобы она не загрязняла глобальное пространство имен. Вложенные функции могут быть полезны, когда нужно реализовать вспомогательную логику, связанную только с работой родительской функции.",
    "Await используется для работы с асинхронным кодом и корутинами. Его можно применять только внутри асинхронной функции, определенной с async def. Await позволяет избежать блокировки основного потока программы во время ожидания результатов asynс-функций. Await делает возможным использование асинхронного кода в синхронном стиле последовательно. При вызове await передается управление обратно событийному циклу. Выполнение функции приостанавливается до завершения await-выражения. Чаще всего await используется при вызове асинхронных функций и методов — для ожидания результата. Await также может применяться к объектам asyncio.Future и asyncio.Task для ожидания их завершения. Если await вызывается для корутины, то выполнение текущей корутины приостанавливается до завершения той, которая вызвана.",
    "Async — это синтаксис для создания асинхронного кода на основе корутин. Асинхронное программирование позволяет выполнять операции вне основного потока выполнения программы. С помощью async def определяются асинхронные функции-корутины. Такие функции не выполняются сразу, а возвращают объект-корутину. Для запуска корутин используется await. Это передает управление обратно в событийный цикл до завершения корутины. Asyncio — стандартный модуль для работы с асинхронным кодом. Он содержит событийный цикл и различные классы. Асинхронный код усложняет логику программы, но позволяет добиться большей производительности за счет неблокирующих вызовов.Корутины полезны для операций ввода/вывода, ожидания сети, обращения к БД — там, где нужно не блокировать основной поток.",
]


random_question = random.choice(questions)  # случайный выбор вопроса

if "Что такое Middleware?" in random_question:
    print(f"Что такое Middleware?")
    print(
        f"Ответ: Middleware — это промежуточное программное обеспечение, которое располагается между приложением и сетевыми службами. Основная цель middleware — обработка запросов и ответов между клиентом и сервером.\n"
    )

if "Какая разница в быстродействии между Django и Flask и почему?" in random_question:
    print(f"Какая разница в быстродействии между Django и Flask и почему?")
    print(
        f"Ответ: Django чуть медленнее Flask из-за своей более высокой функциональности и накладных расходов. Однако на практике разница в скорости работы между ними незначительна для большинства веб-приложений. Flask может быть немного быстрее при обработке простых запросов, но Django лучше масштабируется при увеличении нагрузки благодаря встроенным инструментам кэширования и оптимизации. Кроме того, производительность в большей степени зависит от архитектуры и качества кода конкретного приложения.\n"
    )

if "Что такое протоколы?" in random_question:
    print(f"Что такое протоколы?")
    print(
        f"Ответ: Протоколы — это соглашения, которые определяют интерфейс класса и поведение его объектов. Протоколы задаются с помощью специальных методов, таких как str, len и другие. Они позволяют классам работать с различными функциями и операторами языка. Реализуя протоколы можно интегрировать классы в языке и делать их поведение естественным и интуитивным. В Python есть протоколы для чисел, итераторов, контекстных менеджеров, атрибутов и других областей. Встроенные и сторонние библиотеки полагаются на стандартные протоколы.\n"
    )

if (
    "Можно ли объявлять функцию внутри другой функции? Где она будет видна?"
    in random_question
):
    print(f"Можно ли объявлять функцию внутри другой функции? Где она будет видна?")
    print(
        f"Ответ: Да, функции можно объявлять внутри других функций. Такая вложенная функция будет видна и доступна для вызова только внутри родительской функции, в которой она определена. Это называется замыканием и позволяет ограничить область видимости вложенной функции, чтобы она не загрязняла глобальное пространство имен. Вложенные функции могут быть полезны, когда нужно реализовать вспомогательную логику, связанную только с работой родительской функции.\n"
    )

if "Что такое await?" in random_question:
    print(f"Что такое await?")
    print(
        f"Await используется для работы с асинхронным кодом и корутинами. Его можно применять только внутри асинхронной функции, определенной с async def. Await позволяет избежать блокировки основного потока программы во время ожидания результатов asynс-функций. Await делает возможным использование асинхронного кода в синхронном стиле последовательно. При вызове await передается управление обратно событийному циклу. Выполнение функции приостанавливается до завершения await-выражения. Чаще всего await используется при вызове асинхронных функций и методов — для ожидания результата. Await также может применяться к объектам asyncio.Future и asyncio.Task для ожидания их завершения. Если await вызывается для корутины, то выполнение текущей корутины приостанавливается до завершения той, которая вызвана.\n"
    )

if "Что такое async?" in random_question:
    print(f"Что такое async?")
    print(
        f"Async — это синтаксис для создания асинхронного кода на основе корутин. Асинхронное программирование позволяет выполнять операции вне основного потока выполнения программы. С помощью async def определяются асинхронные функции-корутины. Такие функции не выполняются сразу, а возвращают объект-корутину. Для запуска корутин используется await. Это передает управление обратно в событийный цикл до завершения корутины. Asyncio — стандартный модуль для работы с асинхронным кодом. Он содержит событийный цикл и различные классы. Асинхронный код усложняет логику программы, но позволяет добиться большей производительности за счет неблокирующих вызовов.Корутины полезны для операций ввода/вывода, ожидания сети, обращения к БД — там, где нужно не блокировать основной поток."
    )
