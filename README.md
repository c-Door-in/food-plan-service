# food-plan-service
Сервис по подбору рецептов блюд на каждый день.
(в разработке)

## Настройки

### Подключите зависимости
```
pip install -r requirements.txt
```
### Подключите переменные окружения
Создайте файл `.env` в корневой директории рядом с `settings.py` и введите
```
TGBOT_TOKEN=<token>
PROVIDER_TOKEN=<token>
BOT_DELAY=Целое число секунд
```
Где:
- TGBOT_TOKEN - токен телеграм-бота.  
- PROVIDER_TOKEN - токен провайдера для оплаты. (botfather/mybots/payments - выбрать юкассу, стоимость тестового заказа не более 1000 рублей!)
- BOT_DELAY - параметр, указывающий на то, через какое количество секунд будет отправлено следующее уведомление о приеме пищи.
## Запуск бота
Для запуска бота введите
```
python manage.py bot
```
## Запуск парсера
Для запуска парсера введите
```
python manage.py parser
```
Добавит около 60 блюд, кому подходит и кому не подходит выбирает случайно.

## Редактирование бота
Код бота располагается в `/tgbot/bot_modules/`
