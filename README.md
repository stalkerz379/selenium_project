# selenium_project
## Final Project

### Requirements for the final project

#### Base page
- [x] Создайте в своем проекте папку pages, там мы будем хранить все наши Page Object 
- [x] В папке создайте два файла: base_page.py и main_page.py  

Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
- [x] В файле base_page.py создайте класс с названием BasePage. 
- [x] Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. 
- [x] Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().

#### Main page
- [x] Откройте файл main_page.py 
- [x] В нем нужно сделать импорт базового класса BasePage
- [x] В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage
- [x] Перенесите метод из предыдущего задания в класс MainPage и видоизмените его чтобы все работало.
 
#### Tests in test_main_page.py
- [x] В самом верху файла нужно импортировать класс, описывающий главную страницу
- [x] Преобразуйте тест
- [x] Убедитесь что тест запускается командой "pytest -v --tb=line --language=en test_main_page.py"

#### Методы-проверки в Page object
Допустим, нам нужно проверять такой сценарий: 
1. Открыть главную страницу 
2. Проверить, что есть ссылка, которая ведет на логин 
Для этого в классе MainPage нужно реализовать метод, который будет проверять наличие ссылки.

- [x] B классе MainPage создайте метод should_be_login_link
- [x] Добавьте в файл с тест-кейсами новый тест на проверку логин линки на странице
- [x] Проверьте что тест работает командой "pytest -v --tb=line --language=en test_main_page.py"

#### Проверка элемента на странице
Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать исключения.
Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам True или False
- [x] В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10
- [x] Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
    1. Чтобы перехватывать исключение, нужна конструкция try/except
    2. Импортируйте нужное исключение
- [x] Теперь модифицируйте метод проверки ссылки на логин чтобы он выводил понятное сообщение об ошибке
- [x] Запустите тесты и посмотрите, что вывод об ошибке стал более понятным: "pytest -v --tb=line --language=en test_main_page.py"

#### Locators in separate file
- [x] В папке pages создайте новый файл locators.py 
- [x] Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject
- [x] В файле main_page.py импортируйте новый класс с локаторами
- [x] Теперь в классе MainPage замените все строки, где содержится "#login_link" на импортированый локатор
- [x] Проверьте что тесты запускаются

#### Login Page
- [x] В файле locators.py создайте класс LoginPageLocators 
- [x] Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators
- [x] Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода. 
- [x] В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера. Для этого используйте соответствующее свойство Webdriver.

#### Добавление в корзину со страницы товара
- [x] Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
- [x] Нажимаем на кнопку "Добавить в корзину".
- [x] *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(). Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.

Ожидаемый результат: 

- [x] Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
- [x] Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

#### Независимость от данных
- [x] Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.
- [x] Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
- [x] Сделайте такой же метод для цены.
- [x] Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.

#### Отрицательные проверки: отсутствие элемента
- [x] Добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
- [x] Использовать метод проверки наличия элемента на странице в product page как assertion
- [x] Добавить в BasePage абстрактный метод, который проверяет, что элемент исчезает со страницы
- [x] Использовать метод проверки исчезновения элемента на странице в product page как assertion

Реализуйте несколько простых тестов: 

1. test_guest_cant_see_success_message_after_adding_product_to_basket: 
- [x] Открываем страницу товара 
- [x] Добавляем товар в корзину 
- [x] Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 
2. test_guest_cant_see_success_message: 
- [x] Открываем страницу товара 
- [x] Проверяем, что нет сообщения об успехе с помощью is_not_element_present 

3. test_message_disappeared_after_adding_product_to_basket: 
- [x] Открываем страницу товара
- [x] Добавляем товар в корзину
- [x] Проверяем, что нет сообщения об успехе с помощью is_disappeared

#### Отрицательные проверки: Product page
- [x] Добавьте в файл c тестами test_product_page.py новые тесты на проверку что пользователь может найти ссылку на логин пейдж на странице Product page "test_guest_should_see_login_link_on_product_page"
- [x] Добавьте второй тест test_guest_can_go_to_login_page_from_product_page 

#### Hаследование и отрицательные проверки
В файл test_main_page.py добавьте тест с названием **test_guest_cant_see_product_in_basket_opened_from_main_page**:
- [x] Гость открывает главную страницу 
- [x] Переходит в корзину по кнопке в шапке сайта
- [x] Ожидаем, что в корзине нет товаров
- [x] Ожидаем, что есть текст о том что корзина пуста 

В файле test_product_page.py добавьте тест с названием **test_guest_cant_see_product_in_basket_opened_from_product_page**:
- [x] Гость открывает страницу товара
- [x] Переходит в корзину по кнопке в шапке 
- [x] Ожидаем, что в корзине нет товаров
- [x] Ожидаем, что есть текст о том что корзина пуста
В классе **BasePage** реализуйте соответствующий метод для перехода в корзину. Создайте файл *'basket_page.py'* и в нем класс BasketPage. Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах.
