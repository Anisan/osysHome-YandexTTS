import os
import requests
import hashlib
from app.core.main.BasePlugin import BasePlugin
from plugins.YandexTTS.forms.SettingForms import SettingsForm
from app.core.lib.common import playSound
from app.core.lib.cache import saveToCache, findInCache

class YandexTTS(BasePlugin):

    def __init__(self,app):
        super().__init__(app,__name__)
        self.title = "YandexTTS"
        self.description = """This is a plugin get voice by text"""
        self.category = "App"
        self.version = "0.2"
        self.actions = ["say"]

    def initialization(self):
        pass

    def admin(self, request):
        settings = SettingsForm()
        if request.method == 'GET':
            settings.access_key.data = self.config.get('access_key','')
            settings.speaker.data = self.config.get("speaker",'tatyana_abramova')
            settings.emotion.data = self.config.get("emotion",'good')
        else:
            if settings.validate_on_submit():
                self.config["access_key"] = settings.access_key.data
                self.config["speaker"] = settings.speaker.data
                self.config["emotion"] = settings.emotion.data
                self.saveConfig()
        content = {
            "form": settings,
        }
        return self.render('main_ytts.html', content)

    def say(self, message, level=0, args=None):

        hash = hashlib.md5(message.encode('utf-8')).hexdigest()

        base_url = 'https://tts.voicetech.yandex.net/generate?'

        # файл с кешированным аудио
        file_name = hash + '_ytts.mp3'

        cached_file_name = findInCache(file_name, "TTS", True)
        # Проверяем, существует ли файл с кешированным аудио и не является ли он пустым
        if not cached_file_name or os.path.getsize(cached_file_name) == 0:
            lang = "ru_RU"  # TODO landuage
            qs = {
                'format': 'mp3',
                'lang': lang,
                'speaker': self.config.get("speaker",'tatyana_abramova'),
                'emotion': self.config.get("emotion",'good'),
                'key': self.config.get("access_key",''),
                'text': message  # Замените message на реальное значение
            }
            try:
                response = requests.get(base_url, params=qs)

                # Проверяем успешность запроса
                if response.status_code == 200:
                    res = saveToCache(file_name,response.content,"TTS",True)
                    self.logger.debug("Файл успешно сохранен {}.".format(res))
                else:
                    self.logger.error(f"Ошибка при получении содержимого: {response.status_code}")

            except Exception as e:
                self.logger.exception(f"{type(e).__name__}, {e}")  # Выводим информацию об ошибке

        # Если файл существует и не является пустым, обрабатываем его
        cached_file_name = findInCache(file_name,"TTS",True)
        if cached_file_name and os.path.getsize(cached_file_name):
            playSound(cached_file_name, level, args)
