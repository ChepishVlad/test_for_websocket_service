class TestSelectPositive:
    def select_existed_user_by_phone(self):
        # создать пользователя, но не добавлять в систему
        # выполнить запрос
        # провалидировать ответ (должен возвращаться только один пользователь
        pass

    def select_user_by_name_or_surname(self):
        # создать трех пользователей - двух с одинаковым именем и двух с одинаковой фамилией
        # выполнить запрос
        # провалидировать ответ - должен возвращаться список из двух пользователей
        pass




class TestSelectNegative:
    def select_not_existed_user_by_phone(self):
        # выполнить запрос с номером телефона/ фамилией / именем несуществующего пользователя
        # провалидировать ответ - возвращаемый список должен быть пуст
        pass
