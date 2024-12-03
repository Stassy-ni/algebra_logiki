import streamlit as st

st.title("Информатика. 8 класс")
st.header("Тест по разделу 'Алгебра логики'")

# Проверяем состояние сессии
if "finished" not in st.session_state:
    st.session_state["finished"] = False  # Тест изначально не завершен
if "variant" not in st.session_state:
    st.session_state["variant"] = None  # Вариант теста не выбран
if "test_started" not in st.session_state:
    st.session_state["test_started"] = False  # Тест не начат

# Переменные для подсчета
results = []  # Список для хранения результатов по заданиям
total_points = 0  # Общая сумма баллов
all_questions_answered = True  # Флаг, чтобы проверять, завершены ли все задания

# Ввод ФИО и класса
fio = st.text_input("Введите ФИО:", key="fio", disabled=st.session_state["test_started"])
klass = st.text_input("Введите класс:", key="klass", disabled=st.session_state["test_started"])


# Выбор варианта теста
variant = st.selectbox(
    "Выберите вариант:",
    ["", "Вариант 1", "Вариант 2", "Вариант 3"],
    key="variant",
    disabled=st.session_state["test_started"]
)

# Кнопка "Начать тест"
if not st.session_state["test_started"] and st.button("Начать тест"):
    if fio.strip() and klass.strip() and variant:
        st.session_state["test_started"] = True  # Тест начат
        st.write("Тест начался. Удачи!")
    else:
        st.error("Пожалуйста, заполните ФИО, класс и выберите вариант теста.")


# Отображение заданий только после начала теста
if st.session_state["test_started"]:
    st.subheader(f"{st.session_state['variant']}")
    
    # Блокируем смену варианта
    variant = st.session_state["variant"]

    if st.session_state["variant"] == "Вариант 1":        # задания для Варианта 1
        st.header("Задание 1")
        st.write("Выберите верную логическую операцию:")
        st.write("Пользователь хочет создать резервную копию файлов с ПК. Компьютер проверяет наличие внешнего диска __(И, ИЛИ, НЕ) достаточного свободного места на нем.")
        logic_op_1 = st.selectbox("Выберите логическую операцию", ["", "И", "ИЛИ", "НЕ"])
        if logic_op_1:
            if logic_op_1 == "И":
                results.append(("Задание 1", True))
                total_points += 1  # 1 балл за правильный выбор
            else:
                results.append(("Задание 1", False))
        else:
            all_questions_answered = False

        # Задание 2
        st.header("Задание 2")
        st.write("Составьте из логических выражений дизъюнкцию (A∨B):")
        st.write("Для воспроизведения звука на компьютере должны быть подключены колонки. Для воспроизведения звука на компьютере должны быть подключены наушники.")
        words = ["Для", "воспроизведения", "звука", "на", "компьютере", "должны", "быть", "подключены", "колонки", "и", "или", "не", "наушники"]
        user_selection = st.multiselect("Выберите правильное выражение:", words)
        correct_answer = ["Для", "воспроизведения", "звука", "на", "компьютере", "должны", "быть", "подключены", "колонки", "или", "наушники"]
        if user_selection:
            if user_selection == correct_answer:
                total_points += 3  # 3 балла за правильное составление выражения
                results.append(("Задание 2", True))
            else:
                results.append(("Задание 2", False))
        else:
            all_questions_answered = False

        # Задание 3
        st.header("Задание 3")
        st.write("Прочитайте следующее предложение и выберите правильную схему логического выражения.")
        st.write("Чтобы поделиться документом, пользователь должен иметь доступ к сети и отправить его по почте или загрузить в облачное хранилище и отправить ссылку на документ.")
        option_3 = st.radio("Выберите правильную схему:", ["(A и B) или (C и D)", "A и (B или C и D)", "A или (B и C и D)", "(A и B и C) или D"])
        if option_3:
            if option_3 == "(A и B) или (C и D)":
                results.append(("Задание 3", True))
                total_points += 2  # 2 балла за правильный выбор схемы
            else:
                results.append(("Задание 3", False))
        else:
            all_questions_answered = False

        # Задание 4
        st.header("Задание 4")
        st.write("Прочитайте следующее предложение и определите, что является условием A и условием B.")
        st.write("Чтобы успешно завершить проект на компьютере, ученик должен создать файл с текстом и сохранить его на компьютере или флешке.")
        words = ["ученик", "должен", "создать", "файл", "с", "текстом", "и", "сохранить", "его", "на", "компьютере", "или", "флешке"]
        a_choice = st.multiselect("Выберите слова для условия A:", words)
        b_choice = st.multiselect("Выберите слова для условия B:", words)
        if a_choice and b_choice:
            if a_choice == ["создать", "файл", "с", "текстом"]:
                total_points += 2  # 2 балла за условие A
                results.append(("Задание 4, условие A", True))
            else:
                results.append(("Задание 4, условие A", False))
            if b_choice == ["сохранить", "его", "на", "компьютере", "или", "флешке"]:
                total_points += 2  # 2 балла за условие B
                results.append(("Задание 4, условие B", True))
            else:
                results.append(("Задание 4, условие B", False))
        else:
            all_questions_answered = False

        # Задание 5
        st.header("Задание 5")
        st.write("Определите все условия, при которых высказывание истинно.")
        st.write("Чтобы завершить установку программного обеспечения, компьютер должен быть подключен к интернету или иметь доступ к установочному диску.")
        multi_select_5 = st.multiselect("Выберите все правильные условия:", [
            "Компьютер подключен к интернету",
            "Компьютер имеет доступ к установочному диску",
            "Компьютер подключен к интернету и имеет доступ к установочному диску",
            "Компьютер не подключен к интернету и не имеет доступа к установочному диску"
        ])
        if multi_select_5:
            correct_answers = {
                "Компьютер подключен к интернету",
                "Компьютер имеет доступ к установочному диску",
                "Компьютер подключен к интернету и имеет доступ к установочному диску"
            }
            points_5 = sum(1 for answer in multi_select_5 if answer in correct_answers)
            total_points += points_5  # 1 балл за каждое правильное условие
            results.append(("Задание 5", points_5 == len(correct_answers)))
        else:
            all_questions_answered = False

        # Задание 6
        st.header("Задание 6")
        st.write("Определите истинность каждого утверждения.")
        st.write("Известно: A = 1 (истина), B = 0 (ложь).")
        formulas = ["A И B", "A И НЕ B", "НЕ A И B", "НЕ A ИЛИ НЕ B"]
        correct_answers_6 = {"A И B": 0, "A И НЕ B": 1, "НЕ A И B": 0, "НЕ A ИЛИ НЕ B": 1}
        for formula in formulas:
            user_answer = st.selectbox(f"{formula}:", ["", 0, 1], key=f"{formula}_6")
            if user_answer != "":
                if int(user_answer) == correct_answers_6[formula]:
                    total_points += 1  # 1 балл за каждую формулу
                    results.append((f"Задание 6, {formula}", True))
                else:
                    results.append((f"Задание 6, {formula}", False))
            else:
                all_questions_answered = False

        # Задание 7
        st.header("Задание 7")
        st.write("Расставьте правильный порядок выполнения логических операций:")
        steps = ["НЕ", "Скобки", "И", "ИЛИ"]
        user_order = st.multiselect("Выберите и расставьте шаги в правильном порядке:", steps, default=[])
        if user_order:
            if user_order == steps:
                total_points += 2  # 2 балла за правильную последовательность
                results.append(("Задание 7", True))
            else:
                results.append(("Задание 7", False))
        else:
            all_questions_answered = False

        # Задание 8
        st.header("Задание 8")
        st.write("Я хочу напечатать документ. ПК проверяет, подключен ли принтер к компьютеру или доступен ли виртуальный принтер (PDF-принтер). Определите, какой будет результат с точки зрения ПК.")
        st.write("Определите результат для каждого случая:")

        # Ответы для задания 8
        answers_8 = [
            {"Принтер подключен": "Да", "Виртуальный принтер доступен": "Да", "Результат": "Истина"},
            {"Принтер подключен": "Да", "Виртуальный принтер доступен": "Нет", "Результат": "Ложь"},
            {"Принтер подключен": "Нет", "Виртуальный принтер доступен": "Да", "Результат": "Ложь"},
            {"Принтер подключен": "Нет", "Виртуальный принтер доступен": "Нет", "Результат": "Ложь"},
        ]

        # Добавление заголовков для таблицы
        header_cols = st.columns(3)
        header_cols[0].write("**Принтер подключен**")
        header_cols[1].write("**Виртуальный принтер доступен**")
        header_cols[2].write("**Результат**")

        # Генерация элементов интерфейса для задания 8
        for i, row in enumerate(answers_8):
            cols = st.columns(3)
            # Проверяем, есть ли ключи в словаре перед доступом к ним
            printer_status = row.get("Принтер подключен", "Нет данных")
            virtual_printer_status = row.get("Виртуальный принтер доступен", "Нет данных")
            expected_result = row.get("Результат", "Нет данных")
            
            # Отображаем данные в интерфейсе
            cols[0].write(printer_status)
            cols[1].write(virtual_printer_status)
            user_answer = cols[2].selectbox(
                "Результат:",
                ["", "Истина", "Ложь"],
                key=f"result_8_{i}"
            )

        # Задание 9
        st.header("Задание 9")
        st.write("Напишите наименьшее число x, для которого истинно высказывание:")
        st.write("(x ≥ 10) И НЕ (x делится на 3)")
        answer_9 = st.text_input("Введите наименьшее значение x:")
        if answer_9:
            if answer_9 == "10":
                total_points += 1  # 1 балл за правильный ответ
                results.append(("Задание 9", True))
            else:
                results.append(("Задание 9", False))
        else:
            all_questions_answered = False

        # Задание 10
        st.header("Задание 10")
        st.write("Постройте таблицу истинности для выражения:")
        st.write("A И (B ИЛИ НЕ B)")
        header_cols = st.columns(5)
        header_cols[0].write("**A**")
        header_cols[1].write("**B**")
        header_cols[2].write("**НЕ B**")
        header_cols[3].write("**B ИЛИ НЕ B**")
        header_cols[4].write("**A И (B ИЛИ НЕ B)**")
        answers_10 = [
            {"НЕ B": 1, "B ИЛИ НЕ B": 1, "A И (B ИЛИ НЕ B)": 0},
            {"НЕ B": 0, "B ИЛИ НЕ B": 1, "A И (B ИЛИ НЕ B)": 0},
            {"НЕ B": 1, "B ИЛИ НЕ B": 1, "A И (B ИЛИ НЕ B)": 1},
            {"НЕ B": 0, "B ИЛИ НЕ B": 1, "A И (B ИЛИ НЕ B)": 1},
        ]
        for i in range(4):
            cols = st.columns(5)
            cols[0].write("1" if i >= 2 else "0")  # A
            cols[1].write("1" if i % 2 != 0 else "0")  # B
            ne_b = cols[2].selectbox("", ["", 0, 1], key=f"ne_b_{i}")
            b_or_ne_b = cols[3].selectbox("", ["", 0, 1], key=f"b_or_ne_b_{i}")
            a_and_b_or_ne_b = cols[4].selectbox("", ["", 0, 1], key=f"a_and_b_or_ne_b_{i}")
            row_points = 0
            if ne_b == answers_10[i]["НЕ B"]:
                row_points += 0.5
            if b_or_ne_b == answers_10[i]["B ИЛИ НЕ B"]:
                row_points += 0.5
            if a_and_b_or_ne_b == answers_10[i]["A И (B ИЛИ НЕ B)"]:
                row_points += 0.5
            total_points += row_points
            results.append((f"Задание 10, строка {i + 1}", row_points == 1.5))

    elif st.session_state["variant"] == "Вариант 2":
        st.header("Задание 1")
        st.write("Выберите верную логическую операцию:")
        st.write("Для скачивания обновлений на компьютер необходимо подключение к интернету __(И, ИЛИ, НЕ) наличие прав администратора.")
        logic_op_1 = st.selectbox("Выберите логическую операцию", ["", "И", "ИЛИ", "НЕ"])
        if logic_op_1:
            if logic_op_1 == "И":
                results.append(("Задание 1", True))
                total_points += 1  # 1 балл за правильный выбор
            else:
                results.append(("Задание 1", False))
        else:
            all_questions_answered = False

        st.header("Задание 2")
        st.write("Составьте из логических выражений конъюнкцию (A∧B):")
        st.write("Для отправки сообщения на электронную почту необходимо ввести адрес получателя, а также текст сообщения.")
        words = ["Для", "отправки", "сообщения", "на", "электронную", "почту", "необходимо", "ввести", "адрес", "получателя", "и", "или", "не", "текст", "сообщения"]
        user_selection = st.multiselect("Выберите правильное выражение:", words)
        correct_answer = ["Для", "отправки", "сообщения", "на", "электронную", "почту", "необходимо", "ввести", "адрес", "получателя", "и", "текст", "сообщения"]
        if user_selection:
            if user_selection == correct_answer:
                total_points += 3  # 3 балла за правильное составление выражения
                results.append(("Задание 2 (A∧B)", True))
            else:
                results.append(("Задание 2 (A∧B)", False))
        else:
            all_questions_answered = False

        st.header("Задание 3")
        st.write("Прочитайте следующее предложение и выберите правильную схему логического выражения.")
        st.write("Для безопасного входа в аккаунт пользователь должен ввести пароль и пройти проверку капчи или использовать одноразовый код, отправленный на телефон.")
        option_3 = st.radio("Выберите правильную схему:", ["(A и B) или C", "A и (B или C)", "A или (B и D)", "(A или B или C) или D"])
        if option_3:
            if option_3 == "(A и B) или C":
                results.append(("Задание 3", True))
                total_points += 2  # 2 балла за правильный выбор схемы
            else:
                results.append(("Задание 3", False))
        else:
            all_questions_answered = False

        st.header("Задание 4")
        st.write("Прочитайте следующее предложение и определите, что является условием A и условием B:")
        st.write("Для успешного выполнения домашнего задания ученик должен открыть учебник и выполнить упражнения по указанным страницам.")
        words = ["ученик", "должен", "открыть", "учебник", "и", "выполнить", "упражнения", "по", "указанным", "страницам"]
        a_choice = st.multiselect("Выберите слова для условия A:", words)
        b_choice = st.multiselect("Выберите слова для условия B:", words)
        if a_choice and b_choice:
            if a_choice == ["открыть", "учебник"]:
                total_points += 2  # 2 балла за условие A
                results.append(("Задание 4, условие A", True))
            else:
                results.append(("Задание 4, условие A", False))
            if b_choice == ["выполнить", "упражнения", "по", "указанным", "страницам"]:
                total_points += 2  # 2 балла за условие B
                results.append(("Задание 4, условие B", True))
            else:
                results.append(("Задание 4, условие B", False))
        else:
            all_questions_answered = False

        # Задание 5
        st.header("Задание 5")
        st.write("Определите все условия, при которых высказывание истинно.")
        st.write("Для успешной установки приложения пользователь должен предоставить разрешения для доступа к памяти устройства или установить программу через официальное приложение.")
        multi_select_5 = st.multiselect("Выберите все правильные условия:", [
            "Пользователь предоставляет разрешения для доступа к памяти",
            "Программа установлена через официальное приложение",
            "Пользователь предоставляет разрешения и устанавливает программу через приложение",
            "Программа не установлена, и разрешения не предоставлены"
        ])
        if multi_select_5:
            correct_answers = {
                "Пользователь предоставляет разрешения для доступа к памяти",
                "Программа установлена через официальное приложение",
                "Пользователь предоставляет разрешения и устанавливает программу через приложение",
            }
            points_5 = sum(1 for answer in multi_select_5 if answer in correct_answers)
            total_points += points_5  # 1 балл за каждое правильное условие
            results.append(("Задание 5", points_5 == len(correct_answers)))
        else:
            all_questions_answered = False

        st.header("Задание 6")
        st.write("Определите истинность каждого утверждения:")
        st.write("Известно: A = 0 (ложь), B = 1 (истина).")
        formulas = ["A И B", "A И НЕ B", "НЕ A ИЛИ B", "НЕ A И НЕ B"]
        correct_answers_6 = {
            "A И B": 0,
            "A И НЕ B": 0,
            "НЕ A ИЛИ B": 1,
            "НЕ A И НЕ B": 0
        }
        for formula in formulas:
            user_answer = st.selectbox(f"{formula}:", ["", 0, 1], key=f"{formula}_6")
            if user_answer != "":
                if int(user_answer) == correct_answers_6[formula]:
                    total_points += 1  # 1 балл за каждую формулу
                    results.append((f"Задание 6, {formula}", True))
                else:
                    results.append((f"Задание 6, {formula}", False))
            else:
                all_questions_answered = False

        # Задание 7
        st.header("Задание 7")
        st.write("Расставьте правильный порядок выполнения логических операций:")
        steps = ["НЕ", "Скобки", "И", "ИЛИ"]
        user_order = st.multiselect("Выберите и расставьте шаги в правильном порядке:", steps, default=[])
        if user_order:
            if user_order == steps:
                total_points += 2  # 2 балла за правильную последовательность
                results.append(("Задание 7", True))
            else:
                results.append(("Задание 7", False))
        else:
            all_questions_answered = False

        st.header("Задание 8")
        st.write("Для печати документа ПК проверяет, подключен ли принтер к компьютеру и доступна ли бумага в лотке. Определите, какой будет результат.")

        # Заголовки для таблицы
        header_cols = st.columns(3)
        header_cols[0].write("**Принтер подключен**")
        header_cols[1].write("**Бумага в лотке доступна**")
        header_cols[2].write("**Результат**")

        answers_8 = [
            {"Принтер подключен": "Да", "Бумага в лотке доступна": "Да", "Результат": "Истина"},
            {"Принтер подключен": "Да", "Бумага в лотке доступна": "Нет", "Результат": "Ложь"},
            {"Принтер подключен": "Нет", "Бумага в лотке доступна": "Да", "Результат": "Ложь"},
            {"Принтер подключен": "Нет", "Бумага в лотке доступна": "Нет", "Результат": "Ложь"},
        ]
        for i, row in enumerate(answers_8):
            cols = st.columns(3)
            cols[0].write(row["Принтер подключен"])
            cols[1].write(row["Бумага в лотке доступна"])
            user_answer = cols[2].selectbox("Результат:", ["", "Истина", "Ложь"], key=f"result_8_printer_{i}")
            if user_answer:
                if user_answer == row["Результат"]:
                    total_points += 1  # 1 балл за каждую строку
                    results.append((f"Задание 8, строка {i + 1}", True))
                else:
                    results.append((f"Задание 8, строка {i + 1}", False))
            else:
                all_questions_answered = False

        # Задание 9
        st.header("Задание 9")
        st.write("Напишите наименьшее число x, для которого истинно высказывание:")
        st.write("(x > 15) И НЕ (x делится на 5)")
        answer_9 = st.text_input("Введите наименьшее значение x:")
        if answer_9:
            if answer_9 == "16":
                total_points += 1  # 1 балл за правильный ответ
                results.append(("Задание 9", True))
            else:
                results.append(("Задание 9", False))
        else:
            all_questions_answered = False

        st.header("Задание 10")
        st.write("Постройте таблицу истинности для выражения:")
        st.write("A И (НЕ B И A)")
        header_cols = st.columns(5)
        header_cols[0].write("**A**")
        header_cols[1].write("**B**")
        header_cols[2].write("**НЕ B**")
        header_cols[3].write("**НЕ B И A**")
        header_cols[4].write("**A И (НЕ B И A)**")
        answers_10_a = [
            {"НЕ B": 1, "НЕ B И A": 0, "A И (НЕ B И A)": 0},
            {"НЕ B": 0, "НЕ B И A": 0, "A И (НЕ B И A)": 0},
            {"НЕ B": 1, "НЕ B И A": 1, "A И (НЕ B И A)": 1},
            {"НЕ B": 0, "НЕ B И A": 0, "A И (НЕ B И A)": 0},
        ]
        for i in range(4):
            cols = st.columns(5)
            cols[0].write("1" if i >= 2 else "0")  # A
            cols[1].write("1" if i % 2 != 0 else "0")  # B
            ne_b = cols[2].selectbox("", ["", 0, 1], key=f"ne_b_{i}_a")
            ne_b_and_a = cols[3].selectbox("", ["", 0, 1], key=f"ne_b_and_a_{i}")
            a_and_ne_b_and_a = cols[4].selectbox("", ["", 0, 1], key=f"a_and_ne_b_and_a_{i}")
            row_points = 0
            if ne_b == answers_10_a[i]["НЕ B"]:
                row_points += 0.5
            if ne_b_and_a == answers_10_a[i]["НЕ B И A"]:
                row_points += 0.5
            if a_and_ne_b_and_a == answers_10_a[i]["A И (НЕ B И A)"]:
                row_points += 0.5
            total_points += row_points
            results.append((f"Задание 10 (A И (НЕ B И A)), строка {i + 1}", row_points == 1.5))

    elif st.session_state["variant"] == "Вариант 3":
        st.header("Задание 1")
        st.write("Выберите верную логическую операцию:")
        st.write("Для доступа к защищенному разделу сайта пользователь должен пройти авторизацию __(И, ИЛИ, НЕ) ввести одноразовый пароль, отправленный на телефон.")
        logic_op_1 = st.selectbox("Выберите логическую операцию", ["", "И", "ИЛИ", "НЕ"])
        if logic_op_1:
            if logic_op_1 == "И":
                results.append(("Задание 1", True))
                total_points += 1  # 1 балл за правильный выбор
            else:
                results.append(("Задание 1", False))
        else:
            all_questions_answered = False

        st.header("Задание 2")
        st.write("Составьте из логических выражений дизъюнкцию (A∨B):")
        st.write("Для загрузки файла с сервера пользователь должен иметь доступ к интернету, однако, он также может активировать функцию офлайн-режима.")
        words = ["Для", "загрузки", "файла", "с", "сервера", "пользователь", "должен", "иметь", "доступ", "к", "интернету", "и", "или", "не", "активировать", "функцию", "офлайн-режима"]
        user_selection = st.multiselect("Выберите правильное выражение:", words)
        correct_answer = ["Для", "загрузки", "файла", "с", "сервера", "пользователь", "должен", "иметь", "доступ", "к", "интернету", "или", "активировать", "функцию", "офлайн-режима"]
        if user_selection:
            if user_selection == correct_answer:
                total_points += 3  # 3 балла за правильное составление выражения
                results.append(("Задание 2 (A∨B)", True))
            else:
                results.append(("Задание 2 (A∨B)", False))
        else:
            all_questions_answered = False

        st.header("Задание 3")
        st.write("Прочитайте следующее предложение и выберите правильную схему логического выражения.")
        st.write("Для выполнения задания ученик должен включить компьютер и запустить текстовый редактор или открыть учебное пособие.")
        option_3 = st.radio("Выберите правильную схему:", ["(A и B) или C", "A и (B или C)", "A или (B и D)", "(A или B или C) или D"])
        if option_3:
            if option_3 == "(A и B) или C":
                results.append(("Задание 3", True))
                total_points += 2  # 2 балла за правильный выбор схемы
            else:
                results.append(("Задание 3", False))
        else:
            all_questions_answered = False

        st.header("Задание 4")
        st.write("Прочитайте следующее предложение и определите, что является условием A и условием B:")
        st.write("Для подготовки презентации ученик должен выбрать тему презентации и собрать информацию для слайдов.")
        words = ["ученик", "должен", "выбрать", "тему", "презентации", "и", "собрать", "информацию", "для", "слайдов"]
        a_choice = st.multiselect("Выберите слова для условия A:", words)
        b_choice = st.multiselect("Выберите слова для условия B:", words)
        if a_choice and b_choice:
            if a_choice == ["выбрать", "тему", "презентации"]:
                total_points += 2  # 2 балла за условие A
                results.append(("Задание 4, условие A", True))
            else:
                results.append(("Задание 4, условие A", False))
            if b_choice == ["собрать", "информацию", "для", "слайдов"]:
                total_points += 2  # 2 балла за условие B
                results.append(("Задание 4, условие B", True))
            else:
                results.append(("Задание 4, условие B", False))
        else:
            all_questions_answered = False

        # Задание 5
        st.header("Задание 5")
        st.write("Определите все условия, при которых высказывание истинно.")
        st.write("Для выполнения задания система должна быть подключена к интернету или обладать заранее загруженными данными.")
        multi_select_5 = st.multiselect("Выберите все правильные условия:", [
            "Система подключена к интернету",
            "Система обладает заранее загруженными данными",
            "Система подключена к интернету и обладает заранее загруженными данными",
            "Система не подключена к интернету и не обладает загруженными данными"
        ])
        if multi_select_5:
            correct_answers = {
            "Система подключена к интернету",
            "Система обладает заранее загруженными данными",
            "Система подключена к интернету и обладает заранее загруженными данными",
            }
            points_5 = sum(1 for answer in multi_select_5 if answer in correct_answers)
            total_points += points_5  # 1 балл за каждое правильное условие
            results.append(("Задание 5", points_5 == len(correct_answers)))
        else:
            all_questions_answered = False

        st.header("Задание 6")
        st.write("Определите истинность каждого утверждения:")
        st.write("Известно: A = 1 (истина), B = 0 (ложь).")
        formulas = ["A ИЛИ B", "A ИЛИ НЕ B", "НЕ A И B", "НЕ A И НЕ B"]
        correct_answers_6 = {
            "A ИЛИ B": 1,
            "A ИЛИ НЕ B": 1,
            "НЕ A И B": 0,
            "НЕ A И НЕ B": 0
        }
        for formula in formulas:
            user_answer = st.selectbox(f"{formula}:", ["", 0, 1], key=f"{formula}_6_variant2")
            if user_answer != "":
                if int(user_answer) == correct_answers_6[formula]:
                    total_points += 1  # 1 балл за каждую формулу
                    results.append((f"Задание 6, {formula}", True))
                else:
                    results.append((f"Задание 6, {formula}", False))
            else:
                all_questions_answered = False

        # Задание 7
        st.header("Задание 7")
        st.write("Расставьте правильный порядок выполнения логических операций:")
        steps = ["НЕ", "Скобки", "И", "ИЛИ"]
        user_order = st.multiselect("Выберите и расставьте шаги в правильном порядке:", steps, default=[])
        if user_order:
            if user_order == steps:
                total_points += 2  # 2 балла за правильную последовательность
                results.append(("Задание 7", True))
            else:
                results.append(("Задание 7", False))
        else:
            all_questions_answered = False

        st.header("Задание 8")
        st.write("Система проверяет, может ли пользователь выполнить обновление программы, если устройство подключено к интернету и заряжено более чем на 50%.")

        # Заголовки таблицы
        header_cols = st.columns(3)
        header_cols[0].write("**Устройство подключено к интернету**")
        header_cols[1].write("**Зарядка выше 50%**")
        header_cols[2].write("**Результат**")

        answers_8 = [
            {"Устройство подключено к интернету": "Да", "Зарядка выше 50%": "Да", "Результат": "Истина"},
            {"Устройство подключено к интернету": "Да", "Зарядка выше 50%": "Нет", "Результат": "Ложь"},
            {"Устройство подключено к интернету": "Нет", "Зарядка выше 50%": "Да", "Результат": "Ложь"},
            {"Устройство подключено к интернету": "Нет", "Зарядка выше 50%": "Нет", "Результат": "Ложь"},
        ]
        for i, row in enumerate(answers_8):
            cols = st.columns(3)
            cols[0].write(row["Устройство подключено к интернету"])
            cols[1].write(row["Зарядка выше 50%"])
            user_answer = cols[2].selectbox("Результат:", ["", "Истина", "Ложь"], key=f"result_8_battery_{i}")
            if user_answer:
                if user_answer == row["Результат"]:
                    total_points += 1  # 1 балл за каждую строку
                    results.append((f"Задание 8, строка {i + 1}", True))
                else:
                    results.append((f"Задание 8, строка {i + 1}", False))
            else:
                all_questions_answered = False

        # Задание 9
        st.header("Задание 9")
        st.write("Напишите наименьшее число x, для которого истинно высказывание:")
        st.write("(x ≥ 20) И НЕ (x делится на 4)")
        answer_9 = st.text_input("Введите наименьшее значение x:")
        if answer_9:
            if answer_9 == "21":
                total_points += 1  # 1 балл за правильный ответ
                results.append(("Задание 9", True))
            else:
                results.append(("Задание 9", False))
        else:
            all_questions_answered = False

        st.header("Задание 10")
        st.write("Постройте таблицу истинности для выражения:")
        st.write("(НЕ B ИЛИ A) И B")
        header_cols = st.columns(5)
        header_cols[0].write("**A**")
        header_cols[1].write("**B**")
        header_cols[2].write("**НЕ B**")
        header_cols[3].write("**НЕ B ИЛИ A**")
        header_cols[4].write("**(НЕ B ИЛИ A) И B**")
        answers_10_b = [
            {"НЕ B": 1, "НЕ B ИЛИ A": 1, "(НЕ B ИЛИ A) И B": 0},
            {"НЕ B": 0, "НЕ B ИЛИ A": 0, "(НЕ B ИЛИ A) И B": 0},
            {"НЕ B": 1, "НЕ B ИЛИ A": 1, "(НЕ B ИЛИ A) И B": 0},
            {"НЕ B": 0, "НЕ B ИЛИ A": 1, "(НЕ B ИЛИ A) И B": 1},
        ]
        for i in range(4):
            cols = st.columns(5)
            cols[0].write("1" if i >= 2 else "0")  # A
            cols[1].write("1" if i % 2 != 0 else "0")  # B
            ne_b = cols[2].selectbox("", ["", 0, 1], key=f"ne_b_{i}_b")
            ne_b_or_a = cols[3].selectbox("", ["", 0, 1], key=f"ne_b_or_a_{i}")
            ne_b_or_a_and_b = cols[4].selectbox("", ["", 0, 1], key=f"ne_b_or_a_and_b_{i}")
            row_points = 0
            if ne_b == answers_10_b[i]["НЕ B"]:
                row_points += 0.5
            if ne_b_or_a == answers_10_b[i]["НЕ B ИЛИ A"]:
                row_points += 0.5
            if ne_b_or_a_and_b == answers_10_b[i]["(НЕ B ИЛИ A) И B"]:
                row_points += 0.5
            total_points += row_points
            results.append((f"Задание 10 ((НЕ B ИЛИ A) И B), строка {i + 1}", row_points == 1.5))


# Завершение теста
if st.session_state["test_started"] and not st.session_state["finished"]:
    if st.button("Завершить тест"):
        if all_questions_answered:  # Проверяем, все ли задания выполнены
            st.session_state["finished"] = True  # Блокируем тест
            st.session_state["total_points"] = total_points  # Сохраняем результат
            st.session_state["results"] = results  # Сохраняем подробности по заданиям
            st.success("Тест завершен. Спасибо за выполнение!")
        else:
            st.warning("Пожалуйста, завершите тест для просмотра результатов.")  # Показываем сообщение только при незавершенном тесте

# Вывод результатов
if st.session_state["finished"]:
    st.subheader(f"Результаты для: {fio}, {klass}")
    st.write(f"Набрано баллов: {st.session_state['total_points']} из 30")
    if st.session_state["total_points"] >= 24:
        st.write("Ваша отметка: 5")
    elif st.session_state["total_points"] >= 20:
        st.write("Ваша отметка: 4")
    elif st.session_state["total_points"] >= 14:
        st.write("Ваша отметка: 3")
    else:
        st.write("Ваша отметка: 2")

    # Отображение результатов по каждому заданию
    for task, correct in st.session_state["results"]:
        color = "green" if correct else "red"
        st.markdown(
            f"<span style='color:{color}'>{task}: {'Правильно' if correct else 'Неправильно'}</span>",
            unsafe_allow_html=True
        )
