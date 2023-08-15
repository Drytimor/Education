from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup
from time import sleep
from transliterate import translit


token ="6395231248:AAEQhwvZWllHEj1050G65PyotNARIRzXQ4U"


headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16128205146 t2375925855354670132 athfa3c3975 altpub cvcv=2 smf=0"
    }


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def commands_start(message: types.Message):
    await message.answer("Назови фильм")


@dp.message_handler()
async def get_review(message: types.Message):

    name_film = translit(message.text.replace(" ", "-").replace("ё", "yo")
                                     .replace("я", "ya").replace("ю", "y")
                                     .replace(".", "").replace("ц", "c")
                                     .replace("й", "y").replace("ь", "").lower(), reversed=True)

    url = "https://www.megacritic.ru/film/" + name_film
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="jr-layout-outer jrEditorReviewPanel", limit=10)
    if len(data) == 0:
        await message.answer("Ничего не нашел, давай другой фильм")
        return
    else:
        for elem in data:
            review_film = f"{elem.find('div', class_='jrReviewTitle').text}\n"\
                            f"{elem.find('div', class_='description jrReviewComment').text}" \

            await message.answer(review_film)

    await message.answer("Давай еще фильм")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
