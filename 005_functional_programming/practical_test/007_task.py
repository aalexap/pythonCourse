# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#         Примеры:
#         1234565 seconds = 14:6:56:5

sec = 123423565
days = int(sec / 86400)
hours = int(int(sec % 86400) / 3600)
minutes = int(int(hours % 3600) / 60)
sec_and = minutes / 60

print(f'{days}:{hours}:{minutes}:{minutes}:{sec_and}')
