import requests
import os

def get_download_xml(url: str, headers: dict, directory: str, name_file: str):
    """Получает URL и записывает текст файла в директорию"""
    response = requests.get(url, headers=headers).text
    try:
        with open(f"{directory}/{name_file}", "w") as file:
            file.write(response)
    except:
        print("Error file")
    finally:
        return f"{directory}/{name_file}"






