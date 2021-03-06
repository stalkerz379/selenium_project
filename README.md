## Final Project

### Disclaimer
This project is the **training project**. The code and the structure does not pretend to satisfy the tastes of a test automation gurus)) :wink:
The project based on [this application](http://selenium1py.pythonanywhere.com/).
Want to say **thanks** for the creators of this web app and having a chance to practice. :+1:

For running the tests, please, create new virtual environment and make sure you have installed all necessary packets/modules, you can find the lists of packets in **requirements.txt**. The instruction how to install the packets is in the next section.

To run the tests you can use the next command: **pytest -v --tb=line \path\to\test_product_page.py**.
There are some more option to run the tests:
1. **--language=your_language** - optional, you can choose the language to run the tests. By the default English is selected.
2. **-m your_marker** - optional, pytest markers, you can find the full list in **pytest.ini**.

### The Structure of this repository
Here is the basic structure of this repository:
1. The folder pages contains:
   - **base_page.py** - this file describes the basic class and methods (that are the same for all pages) for the web page. All other classes inherit from this class.
   - **basket_page.py** - this files contains the class and methods for the basket page, it inherits from the BasePage class.
   - **locators.py** - this file contains all the locators for all classes.
   - **login_page.py** - this file contains the class and methods for the login page. It inherits from the BasePage class.
   - **main_page.py** - this file contains the class and methods for the main page. It inherits from the BasePage class.
   - **product_page.py** - this file contains the class and methods for the product page. It inherits from the BasePage class.
2. **__init__.py** - this file allows python to interpret directories as packages.
3. **conftest.py** - this is the basic file that contains fixture for the browser, at the current moment it works by default with **Chrome**. Also it contains a command line option to select the language. You can select the language by adding a flag **--language=your_language** when running tests. **By the default the language is English.**
4. **pytest.ini** - this file contains the markers in separate file. You can run tests with selected marked. E.g. add a flag **-m your_flag_name** as a command line argument when running the tests.
5. **requirements.py** - this file contains all modules that were installed during the process of creating this repository. **If you have any troubles with running the tests, please, make sure that you have installed all the necessary packets. You can install the packets: *pip install -r \path\to\requirements.txt*.**
6. **test_main_page.py** - this file contains the tests for the main page of the web app. 
7. **test_product_page.py** - this file contains the tests for the product page.

### Requirements for the final project

**Pay attention that at the current moment all the requirements are in russian. Sorry, for this inconvenience.**

#### Base page
- [x] Создайте в своем проекте папку pages, там мы будем хранить все наши Page Object 
- [x] В папке создайте два файла: *base_page.py* и *main_page.py*  

Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
- [x] В файле *base_page.py* создайте класс с названием **BasePage**. 
- [x] Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. 
- [x] Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().

#### Main page
- [x] Откройте файл *main_page.py* 
- [x] В нем нужно сделать импорт базового класса **BasePage**
- [x] В нем создайте класс  **MainPage**. Его нужно сделать наследником класса **BasePage**
- [x] Перенесите метод из предыдущего задания в класс **MainPage** и видоизмените его чтобы все работало.
 
#### Tests in test_main_page.py
- [x] В самом верху файла нужно импортировать класс, описывающий главную страницу
- [x] Преобразуйте тест
- [x] Убедитесь что тест запускается командой "pytest -v --tb=line --language=en test_main_page.py"

#### Методы-проверки в Page object
Допустим, нам нужно проверять такой сценарий: 
1. Открыть главную страницу 
2. Проверить, что есть ссылка, которая ведет на логин 
Для этого в классе **MainPage** нужно реализовать метод, который будет проверять наличие ссылки.

- [x] B классе **MainPage** создайте метод **should_be_login_link**
- [x] Добавьте в файл с тест-кейсами новый тест на проверку логин линки на странице
- [x] Проверьте что тест работает командой *"pytest -v --tb=line --language=en test_main_page.py"*

#### Проверка элемента на странице
Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью *assert* и перехватывать исключения.
Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице **BasePage**, который будет возвращать нам True или False
- [x] В конструктор **BasePage** добавим команду для неявного ожидания со значением по умолчанию в 10
- [x] Теперь в этом же классе реализуем метод *is_element_present*, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
    1. Чтобы перехватывать исключение, нужна конструкция *try/except*
    2. Импортируйте нужное исключение
- [x] Теперь модифицируйте метод проверки ссылки на логин чтобы он выводил понятное сообщение об ошибке
- [x] Запустите тесты и посмотрите, что вывод об ошибке стал более понятным: *"pytest -v --tb=line --language=en test_main_page.py"*

#### Locators in separate file
- [x] В папке pages создайте новый файл *locators.py*
- [x] Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject
- [x] В файле *main_page.py* импортируйте новый класс с локаторами
- [x] Теперь в классе **MainPage** замените все строки, где содержится *"#login_link"* на импортированый локатор
- [x] Проверьте что тесты запускаются

#### Login Page
- [x] В файле *locators.py* создайте класс **LoginPageLocators**
- [x] Подберите селекторы к формам регистрации и логина, добавьте их в класс **LoginPageLocators**
- [x] Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода. 
- [x] В методе **should_be_login_url** реализуйте проверку, что подстрока *"login"* есть в текущем url браузера. Для этого используйте соответствующее свойство Webdriver.

#### Добавление в корзину со страницы товара
- [x] Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
- [x] Нажимаем на кнопку "Добавить в корзину".
- [x] Посчитать результат математического выражения и ввести ответ. Используйте для этого метод **solve_quiz_and_get_code()**. Например, можете добавить его в класс **BasePage**, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.

Ожидаемый результат: 

- [x] Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
- [x] Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

#### Независимость от данных
- [x] Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.
- [x] Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
- [x] Сделайте такой же метод для цены.
- [x] Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.

#### Отрицательные проверки: отсутствие элемента
- [x] Добавить в **BasePage** абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
- [x] Использовать метод проверки наличия элемента на странице в product page как assertion
- [x] Добавить в **BasePage** абстрактный метод, который проверяет, что элемент исчезает со страницы
- [x] Использовать метод проверки исчезновения элемента на странице в *product page* как assertion

Реализуйте несколько простых тестов: 

1. **test_guest_cant_see_success_message_after_adding_product_to_basket**: 
- [x] Открываем страницу товара 
- [x] Добавляем товар в корзину 
- [x] Проверяем, что нет сообщения об успехе с помощью **is_not_element_present**
 
2. **test_guest_cant_see_success_message**: 
- [x] Открываем страницу товара 
- [x] Проверяем, что нет сообщения об успехе с помощью **is_not_element_present**

3. **test_message_disappeared_after_adding_product_to_basket**: 
- [x] Открываем страницу товара
- [x] Добавляем товар в корзину
- [x] Проверяем, что нет сообщения об успехе с помощью **is_disappeared**

#### Отрицательные проверки: Product page
- [x] Добавьте в файл c тестами *test_product_page.py* новые тесты на проверку что пользователь может найти ссылку на логин пейдж на странице Product page "test_guest_should_see_login_link_on_product_page"
- [x] Добавьте второй тест **test_guest_can_go_to_login_page_from_product_page**

#### Hаследование и отрицательные проверки
В файл *test_main_page.py* добавьте тест с названием **test_guest_cant_see_product_in_basket_opened_from_main_page**:
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

#### Группировка тестов и setup
В этом задании мы хотим добавить тестовые сценарии не только для гостей сайта, но и для зарегистрированных пользователей. Для этого:

- [x] В файле *test_product_page.py* добавьте новый класс для тестов **TestUserAddToBasketFromProductPage**.
- [x] Добавьте туда уже написанные тесты **test_guest_cant_see_success_message** и **test_guest_can_add_product_to_basket** и переименуйте, заменив guest на user. Шаги тестов не изменятся, добавится лишь регистрация перед тестами. Параметризация здесь уже не нужна, не добавляйте её. 
- [x] Добавьте в **LoginPage** метод **register_new_user(email, password)**, который принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
- [x] Добавьте в **BasePage** проверку того, что пользователь залогинен
- [x] Добавьте в класс фикстуру setup. В этой функции нужно:
    - [x] открыть страницу регистрации;
    - [x] зарегистрировать нового пользователя;
    - [x] проверить, что пользователь залогинен
- [x] Запустите оба теста и убедитесь, что они проходят и действительно регистрируют новых пользователей
