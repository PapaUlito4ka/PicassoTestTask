from random import randint
from time import sleep

from celery import shared_task, app

from files.models import File


@shared_task
def process_file(file_id: str):
    """Функция обработки файла"""

    # Симуляция обработки файла
    sleep(randint(1, 3))
    # Проверка на наличие созданного файла в БД
    number_of_tries = 20
    while not File.objects.filter(pk=file_id).exists():
        if number_of_tries <= 0:
            return
        number_of_tries -= 1
        sleep(0.1)
    File.objects.filter(pk=file_id).update(processed=True)
