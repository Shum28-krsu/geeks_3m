import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Проверка возраста'
    page.theme_mode = ft.ThemeMode.LIGHT

    def text_name(e):  
        name = name_input.value.strip()

        if name:
            text_hello.value = f"Hello {name}"
            text_hello.color = ft.Colors.BLACK
        else:
            text_hello.value = "Введи имя!"
            text_hello.color = ft.Colors.RED_900

        page.update()

    def check_age(e):
        age = age_input.value.strip()

        if age.isdigit(): 
            age = int(age)
            
            if age >= 18:
                result_text.value = "Доступ разрешен"
                result_text.color = ft.Colors.GREEN
            else:
                result_text.value = "Доступ запрещен"
                result_text.color = ft.Colors.RED
        else:
            result_text.value = "Введите корректный возраст"
            result_text.color = ft.Colors.YELLOW

        page.update()

    text_hello = ft.Text('Hello')
    name_input = ft.TextField(label='Введите имя')
    name_btn = ft.ElevatedButton('Отправить имя', on_click=text_name)

    result_text = ft.Text('Введите возраст')
    age_input = ft.TextField(label='Введите возраст')
    age_btn = ft.ElevatedButton('Проверка', on_click=check_age)

    page.add(text_hello, name_input, name_btn,result_text, age_input, age_btn)

ft.app(main_page, view=ft.AppView.WEB_BROWSER)