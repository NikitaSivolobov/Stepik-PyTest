import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# тест, который проверяет, что страница содержит кнопку добавления в корзину
def test_button(browser):
    browser.get(link)
    time.sleep(30)
           
    # проверка assert - наличие кнопки
    assert browser.find_element_by_class_name("btn-add-to-basket"), f"Кнопка не найдена"
    time.sleep(5)
    
