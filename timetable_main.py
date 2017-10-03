import time
import ctypes

dict_day = {
    'Sunday': 'java',
    'Monday': 'java',
    'Tuesday': 'cpp',
    'Wednesday': 'java',
    'Thusday': 'python',
    'Friday': 'cpp',
    'Saturday': 'python'
}

today = time.strftime('%A')
today_target = 'D:\\Moe\\Wallpaper\\kaggle\\' + dict_day[today] + '.png'

SPI_SETWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(
    SPI_SETWALLPAPER, 0,
    today_target, 0)
