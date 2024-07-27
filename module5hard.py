# Классы и объекты
import time


class UrTube:
    """
    Атриубты UrTube:
    users(список объектов User),
    videos(список объектов Video),
    current_user(текущий пользователь, User)
    """

    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[self.users.index(nickname)].password == hash(password):
                self.current_user = self.users[self.users.index(nickname)]
            else:
                print('Пароль не верен.')
        else:
            print(f"Пользователь {nickname} не существует")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, track):
        video_list = []
        for video in self.videos:
            if video.title.lower().find(track.lower()) != -1:
                video_list.append(video.title)
        return video_list

    def watch_video(self, track):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif track in self.videos:
            track_number = self.videos.index(track)
            if self.videos[track_number].adult_mode is True and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                while self.videos[track_number].time_now < self.videos[track_number].duration:
                    time.sleep(1)  # задержка времени
                    self.videos[track_number].time_now += 1
                    print(self.videos[track_number].time_now, end=' ')
                self.videos[track_number].time_now = 0
                print("Конец видео")


class Video:
    """
    Атриубуты Video:
    title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other

    def __str__(self):
        return self.title


class User:
    """
    Атриубуты User:
    nickname(имя пользователя, строка),
    password(в хэшированном виде, число),
    age(возраст, число)
    """

    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return self.username == other


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
# Выходим и входим новым пользователем
ur.log_out()
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
