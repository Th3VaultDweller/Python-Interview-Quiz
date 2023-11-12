questions_and_answers = [
    {"Что такое Middleware": "Middleware — это промежуточное программное обеспечение, которое располагается между приложением и сетевыми службами. Основная цель middleware — обработка запросов и ответов между клиентом и сервером."},
    {"Какая разница в быстродействии между Django и Flask и почему?": "Django чуть медленнее Flask из-за своей более высокой функциональности и накладных расходов. Однако на практике разница в скорости работы между ними незначительна для большинства веб-приложений. Flask может быть немного быстрее при обработке простых запросов, но Django лучше масштабируется при увеличении нагрузки благодаря встроенным инструментам кэширования и оптимизации.\nКроме того, производительность в большей степени зависит от архитектуры и качества кода конкретного приложения."},
    {'Можно ли объявлять функцию внутри другой функции? Где она будет видна?': 'Да, функции можно объявлять внутри других функций. Такая вложенная функция будет видна и доступна для вызова только внутри родительской функции, в которой она определена. Это называется замыканием и позволяет ограничить область видимости вложенной функции, чтобы она не загрязняла глобальное пространство имен. Вложенные функции могут быть полезны, когда нужно реализовать вспомогательную логику, связанную только с работой родительской функции.'},
    {'Что такое await?': 'Await используется для работы с асинхронным кодом и корутинами. Его можно применять только внутри асинхронной функции, определенной с async def.\nAwait позволяет избежать блокировки основного потока программы во время ожидания результатов asynс-функций. Await делает возможным использование асинхронного кода в синхронном стиле последовательно.\nПри вызове await передается управление обратно событийному циклу. Выполнение функции приостанавливается до завершения await-выражения.\nЧаще всего await используется при вызове асинхронных функций и методов — для ожидания результата. Await также может применяться к объектам asyncio.Future и asyncio.Task для ожидания их завершения.\nЕсли await вызывается для корутины, то выполнение текущей корутины приостанавливается до завершения той, которая вызвана.'},
    {'Что такое async?': 'Async — это синтаксис для создания асинхронного кода на основе корутин. Асинхронное программирование позволяет выполнять операции вне основного потока выполнения программы. С помощью async def определяются асинхронные функции-корутины. Такие функции не выполняются сразу, а возвращают объект-корутину. Для запуска корутин используется await. Это передает управление обратно в событийный цикл до завершения корутины. Asyncio — стандартный модуль для работы с асинхронным кодом. Он содержит событийный цикл и различные классы. Асинхронный код усложняет логику программы, но позволяет добиться большей производительности за счет неблокирующих вызовов.\nКорутины полезны для операций ввода/вывода, ожидания сети, обращения к БД — там, где нужно не блокировать основной поток.'},
    # Общие вопросы по Computer Science и Web Development
    {'Что такое инженерия и процесс разработки в целом?': 'Ответ не добавлен'},
    {'Чем отличаются процедурная и объектно-ориентироавнная парадигмы программирования?': 'ООП или Объе́ктно-ориенти́рованное программи́рование хорошо применяется в практике программирования для более лёгкого создания управляемых проектов. Процедурный подход подразумевает написание программного кода без использования объектов. Процедурное программирование заключается в написании кода с или без подпрограмм.'},
    {'Какие основные принципы ООП (наследование, инкапсуляция, полиморфизм)': 'Абстракция — отделение концепции от ее экземпляра;\nПолиморфизм — реализация задач одной и той же идеи разными способам;\nНаследование — способность объекта или класса базироваться на другом объекте или классе. Это главный механизм для повторного использования кода. Наследственное отношение классов четко определяет их иерархию;\nИнкапсуляция — размещение одного объекта или класса внутри другого для разграничения доступа к ним.'},
    {'Что такое множественное наследование?': 'Множественное наследование — это возможность класса иметь более одного родительского класса. При множественном наследовании дочерний класс наследует все свойства родительских классов. Синтаксис множественного наследования очень похож на синтаксис обычного наследования.'},
    {'Какие есть шесть этапов разработки продукта в Software Development lifecycle и какая разница между Agile и Kanban?': 'Ответ не добавлен'},
    {'Какие есть методы HTTP-запросов и какая между ними разница?': 'GET запрашивает представление ресурса. Запросы с использованием этого метода могут только извлекать данные.\nHEAD запрашивает ресурс так же, как и метод GET, но без тела ответа.\nPOST используется для отправки сущностей к определённому ресурсу. Часто вызывает изменение состояния или какие-то побочные эффекты на сервере.\nPUT заменяет все текущие представления ресурса данными запроса.\nDELETE удаляет указанный ресурс.\nCONNECT устанавливает "туннель" к серверу, определённому по ресурсу.\nOPTIONS используется для описания параметров соединения с ресурсом.\nTRACE выполняет вызов возвращаемого тестового сообщения с ресурса.\nPATCH используется для частичного изменения ресурса.'},
    {'Что такое авторизация и как она работает?': 'Ответ не добавлен'},
    {'Что такое cookies?': 'Куки (cookies) — это хранящиеся на компьютерах и гаджетах небольшие файлы, c помощью которых сайт запоминает информацию о посещениях пользователя. Благодаря кукам при каждом посещении того или иного ресурса не нужно вводить регистрационные данные — браузер их подгружает самостоятельно.\nПоэтому нагрузка не сервер не возрастает и повышается скорость открытия веб-страниц. Сами по себе куки не опасны — это обычные текстовые файлы. Они не могут запускать какие-либо процессы на компьютере и каким-то образом влиять на работу операционной системы.'},
    {'Что такое веб-уязвимость?': 'Ответ не добавлен'},
    {'Какие есть классические базы данных?': 'Ответ не добавлен'},
    {'Как читать спецификацию в конкретном языке (например, PEP8 в Python)?': 'Ответ не добавлен'},
    {'Как происходит взаимодействие клиента и сервера?': 'Ответ не добавлен'},
    {'Какие есть подходы к проектированию API?': 'Ответ не добавлен'},
    {'Как использовать паттерны программирования?': 'Ответ не добавлен'},
    {'Что такое Acceptance Testing и зачем его используют?': 'Ответ не добавлен'},
    {'Что такое модульные и интеграционные тесты, API-тесты?': 'Ответ не добавлен'},
    {'Как писать unit-тесты?': 'Ответ не добавлен'},
    {'Какие есть best practices в написании автотестов?': 'Ответ не добавлен'},
    {'В чем разница между хешированием и шифрованием?': 'Ответ не добавлен'},
    # Python
    {'Python - интерпретируемый язык или компилируемый?': 'Это интерпретируемый язык, а не компилируемый, как C++ или Java. Программа на Python представляет собой обычный текстовый файл.'},
    {'Какие есть меняющиеся и постоянные типы данных?': 'Неизменяемые типы данных: целые числа (int), строки (str), кортежи (tuple), числа с плавающей запятой (float).\nИзменяемые типы данных: списки (list), словари (dict).'},
    {'Что такое область видимости переменных?': 'Область видимости или scope определяет контекст переменной, в рамках которого ее можно использовать. В Python есть два типа контекста: глобальный и локальный.\nГлобальный контекст подразумевает, что переменная является глобальной, она определена вне любой из функций и доступна любой функции в программе. В отличие от глобальных переменных локальная переменная определяется внутри функции и доступна только из этой функции, то есть имеет локальную область видимости.'},
    {'Что такое introspection?': 'Интроспекция — это способность объекта во время выполнения получить тип, доступные атрибуты и методы, а также другую информацию, необходимую для выполнения дополнительных операций с объектом.'},
    {'Разница между is и ==?': 'Важно помнить об этой разнице при работе с Python. Особенно это актуально при работе с изменяемыми типами данных, такими как списки или словари, где «==» и «is» могут дать совершенно разные результаты. «==» сравнивает значения, а «is» проверяет, указывают ли объекты на одну и ту же область памяти.'},
    {'Разница между __init __ () и __new __ ()?': 'Ответ не добавлен'},
    {'В чем разница между потоками и процессами?': 'Ответ не добавлен'},
    {'Какие есть виды импорта?': 'Ответ не добавлен'},
    {'Что такое класс, итератор, генератор?': 'Ответ не добавлен'},
    {'Что такое метакласс, переменная цикла?': 'Ответ не добавлен'},
    {'В чем разница между итераторами и генераторами?': 'Ответ не добавлен'},
    {'Как работают декораторы, контекстные менеджеры?': 'Ответ не добавлен'},
    {'Как работают dict comprehension, list comprehension и set comprehension?': 'Ответ не добавлен'},
    {'Можно ли использовать несколько декораторов для одной функции?': 'Ответ не добавлен'},
    {'Можно ли создать декоратор из класса?': 'Да. Если decorator является классом, он должен принимать функцию func в качестве аргумента в своем методе __init__(). Кроме того, класс должен быть вызываемым, чтобы он мог выступать в качестве декоратора функции.'},
    {'Какие есть основные популярные пакеты (requests, pytest, etc)': 'Ответ не добавлен'},
    {'Что такое lambda-функции?': 'Лямбда-выражение в программировании — специальный синтаксис для определения функциональных объектов, заимствованный из λ-исчисления. Применяется как правило для объявления анонимных функций по месту их использования, и обычно допускает замыкание на лексический контекст, в котором это выражение использовано.'},
    {'Что означает *args, **kwargs и как они используются?': 'Ответ не добавлен'},
    {'Что такое exceptions, <try-except>?': 'Ответ не добален'},
    {'Что такое PEP (Python Enhancement Proposal), какие из них знаете (PEP 8, PEP 484)?': 'Ответ не добавлен'},
    {'Какие есть типы данных и какая разница между list и tuple, зачем они?': 'Ответ не добавлен'},
    {'Как использовать встроенные коллекции (list, set, dictionary)?': 'Ответ не добавлен'},
    {'В чем заключается сложность доступа к элементам dict?': 'Ответ не добавлен'},
    {'Как создается объект в Python, для чего __new__, зачем __init__?': 'Ответ не добавлен'},
    {'Что такое шаблонизатор и как в нем выполнять базовые операции (объединять участки шаблона, выводить дату, выводить данные с серверной стороны)?':'Ответ не добавлен'},
    {'Как Python работает с HTTP-сервером?': 'Ответ не добавлен'},
    {'Что происходит, когда создается виртуальная среда?': 'Ответ не добавлен'},
    {'Что такое модель памяти Python?': 'Ответ не добавлен'},
    {'Что такое SQLAlchemy (Core и ORM частей) и какие есть альтернативы?': 'Ответ не добавлен'},
    {'Принципы работы и механизм Garbage collection, reference counting?': 'Ответ не добавлен'},
    {'Как работает thread locals?': 'Ответ не добавлен'},
    {'Что такое _slots_?': 'Ответ не добавлен'},
    {'Как передаются аргументы функций в Python (by value or reference)?': 'Ответ не добавлен'},
    {'Что такое type annotation?': 'Ответ не добавлен'},
    {'Для чего используют нижние подчеркивания в именах классов?': 'Ответ не добавлен'},
    {'Каким образом можно запустить код на Python параллельно?': 'Ответ не добавлен'},
    {'Как работать с stdlib?': 'Ответ не добавлен'},
    {'Что такое дескрипторы?': 'Ответ не добавлен'},
    # Базы данных
    {'Какие есть базовые методы работы с SQL- базой данных в Python?': 'Ответ не добавлен'},
    {'Что такое SQL-транзакция?': 'Ответ не добавлен'},
    {'Как сделать выборку из SQL-базы с простой агрегацией?': 'Ответ не добавлен'},
    {'Как выглядит запрос, который выполняет JOIN между таблицами и к самим себе?': 'Ответ не добавлен'},
    {'Как отправлять запросы в SQL-базу данных без ORM?': 'Ответ не добавлен'},
    {'Разница между SQL и NoSQL?': 'Ответ не добавлен'},
    {'Какие есть уровни изоляции транзакций?': 'Ответ не добавлен'},
    {'Какие есть виды индексов?': 'Ответ не добален'},
    {'Работали ли с Docker-контейнерами, объяснить основные термины K8s (кластер, pod, node, deployment, service), что такое Kibana?': 'Ответ не добавлен'},
    # Алгоритмы
    {'Что такое алгоритмы (например, Big-O нотация)?': 'Алгоритм - приводящая к решению задач последовательность действий.\nBig O нотация нужна для описания сложности алгоритмов. Для этого используется понятие времени.'},
    {'Какие есть базовые алгоритмы сортировки?': 'Пузырьковая сортировка (Bubble Sort). Этот вид сортировки изучают в начале знакомства с дисциплиной Computer Science, поскольку он максимально просто демонстрирует саму концепцию сортировки. При этом подходе осуществляется перебор по списку и сравнение соседних элементов. Они меняются местами в том случае, если порядок неправильный. Так продолжается до тех пор, пока все элементы не расположатся в нужном порядке. Из-за большого количества повторений у пузырьковой сортировки его сложность в худшем случае — O(n^2).\nСортировка с выбором (Selection Sort).Сортировка выбором — также простой алгоритм, но более эффективный по сравнению с пузырьковой сортировкой. В большинстве случаев сортировка выбором будет более удачным выбором из двух.В этом алгоритме список (или массив) делится на две части: список с отсортированными элементами и список с элементами, которые только нужно сортировать. Сначала ищется самый маленький элемент во втором. Он добавляется в конце первого. Таким образом алгоритм постепенно формирует список от меньшего к большему. Так происходит до тех пор, пока не будет готовый отсортированный массив.\nСортировка вставками (Insertion Sort). Сортировка вставками быстрее и проще двух предыдущих. Именно так большинство людей тасует карты любой игре. На каждой итерации программа берет один из элементов и подыскивает для него место в уже отсортированном списке. Так происходит до тех пор, пока не останется ни одного неиспользованного элемента.\nСортировка слиянием (Merge Sort). Сортировка слиянием — элегантный пример использования подхода «Разделяй и властвуй». Он состоит из двух этапов: Несортированный список последовательно делится на N списков, где каждый включает один «несортированный» элемент, а N — это число элементов в оригинальном массиве. Списки последовательно сливаются группами по два, создавая новые отсортированные списки до тех пор, пока не появится один финальный отсортированный список.\nБыстрая сортировка (Quick Sort). Как и сортировка слиянием, быстрая сортировка использует подход «Разделяй и властвуй». Алгоритм чуть сложнее, но в стандартных реализациях он работает быстрее сортировки слиянием, а его сложность в худшем случае редко достигает O(n^2). Он состоит из трех этапов: Выбирается один опорный элемент. Все элементы меньше опорного перемешаются слева от него, остальные — направо. Это называется операцией разбиения. Рекурсивно повторяются 2 предыдущих шага к каждому новому списку, где новые опорные элементы будут меньше и больше оригинального соответственно.'},
    {'Что такое Bubble Sort и как это работает?': 'Пузырьковая сортировка (Bubble Sort). Этот вид сортировки изучают в начале знакомства с дисциплиной Computer Science, поскольку он максимально просто демонстрирует саму концепцию сортировки. При этом подходе осуществляется перебор по списку и сравнение соседних элементов. Они меняются местами в том случае, если порядок неправильный. Так продолжается до тех пор, пока все элементы не расположатся в нужном порядке. Из-за большого количества повторений у пузырьковой сортировки его сложность в худшем случае — O(n^2).'},
    {'Что такое линейная сложность сортировки?': 'Линейная - O(n) - Означает, что сложность алгоритма линейно растёт с увеличением входных данных. Другими словами, удвоение размера входных данных удвоит и необходимое время для выполнения алгоритма. Такие алгоритмы легко узнать по наличию цикла по каждому элементу массива.'},
    # Middle вопросы
    {'Что такое многопоточность?': 'Многопото́чность (англ. Multithreading) — свойство платформы (например, операционной системы, виртуальной машины и т. д.) или приложения, состоящее в том, что процесс, порождённый в операционной системе, может состоять из нескольких потоков, выполняющихся «параллельно», то есть без предписанного порядка во времени.'},
    {'Что такое архитектура веб-сервисов?': 'Архитектура веб-приложения представляет собой макет со всеми программными компонентами (такими как базы данных, приложения и промежуточное ПО) и их взаимодействием друг с другом. Он определяет, как данные доставляются через HTTP, и гарантирует, что сервер на стороне клиента и внутренний сервер могут их понять.'},
    {'Как написать, задеплоить и поддерживать (микро) сервис?': 'Ответ не добавлен'},
    {'Как масштабировать API?': 'Ответ не добавлен'},
    {'Как проводить Code review?': 'Code review — процесс итерационный и на каждой итерации происходит следующее:\n1) Автор делится кодом\n2) Ревьювер смотрит код, формирует фидбек и отправляет его автору\n3) Автор реагирует на фидбек уточняющими комментариями или изменениями в коде и снова отдает код на ревью.'},
    {'Что такое абстрактная фабрика, как ее реализовать и зачем ее применяют?': 'Абстрактная фабрика объявляет методы создания различных абстрактных продуктов (кресло/столик). Конкретные фабрики относятся каждая к своей вариации продуктов (Викторианский/Модерн) и реализуют методы абстрактной фабрики, позволяя создавать все продукты определённой вариации.\nПрименяется:\n1) Когда бизнес-логика программы должна работать с разными видами связанных друг с другом продуктов, не завися от конкретных классов продуктов. Абстрактная фабрика скрывает от клиентского кода подробности того, как и какие конкретно объекты будут созданы. Но при этом клиентский код может работать со всеми типами создаваемых продуктов, поскольку их общий интерфейс был заранее определён.\n2) Когда в программе уже используется Фабричный метод, но очередные изменения предполагают введение новых типов продуктов. В хорошей программе каждый класс отвечает только за одну вещь. Если класс имеет слишком много фабричных методов, они способны затуманить его основную функцию. Поэтому имеет смысл вынести всю логику создания продуктов в отдельную иерархию классов, применив абстрактную фабрику.'},
    {'Что такое цикломатическая сложность?': 'Цикломатическая сложность -показатель сложности исходного кода программы, который связан (коррелирует) с вероятностью возникновения ошибок (багов) в программе. Большая цикломатическая сложность программы (модуля) как правило означает запутанность кода, и повышение риска ошибок при модификации кода.'},
    {'то такое временная сложность алгоритма (time complexity)?': 'Временная сложность алгоритма (в худшем случае) — это функция размера входных и выходных данных, равная максимальному количеству элементарных операций, проделываемых алгоритмом для решения экземпляра задачи указанного размера. Во многих задачах размер выхода не превосходит или пропорционален размеру входа — в этом случае можно рассматривать временную сложность как функцию размера только входных данных. Аналогично понятию временной сложности в худшем случае определяется понятие временная сложность алгоритма в наилучшем случае. Также рассматривают понятие среднее время работы алгоритма, то есть математическое ожидание времени работы алгоритма. Иногда говорят просто: «Временная сложность алгоритма» или «Время работы алгоритма», имея в виду временную сложность алгоритма в худшем, наилучшем или среднем случае (в зависимости от контекста).'},
]
