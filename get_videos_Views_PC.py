from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

# WINDOW_SIZE = "1920,1080"
options = Options()
options.headless = True

# driver = webdriver.Chrome(r"C:\ChromeDriver\chromedriver.exe", options=options)

driver = webdriver.Chrome(options=options)

videos = [
    "https://youtu.be/VuvTXqm0RN0",  # ازاى ابدأ - كيف أبدأ ؟ الجزء الأول
    "https://youtu.be/j-NjsCtd4gc",  # Drawing Ibrahim Adil | The Guru رسم ابراهيم عادل
    "https://youtu.be/XvkWjKglw54",  # Drawing Portrait with Cross line (T) Technique
    "https://youtu.be/dQ-rghO0NL4",  # The cross letter "T" determines the head pose التقاطع فى البورتريه
    "https://youtu.be/FMC7w5Z6CDM",  # Pose building رسم وضعية الجسم بالخطوات
    "https://youtu.be/FQI5nEjY8CU",  # Basic Shapes الأشكال الهندسية
    "https://youtu.be/DXfm0gURlEk",  # Drawing Katrin Zeta Jones
    "https://youtu.be/nJeSId62A0s",  # Simply drawing a horse رسم حصان بشكل مبسط
    "https://youtu.be/4wAbIlG-L5A",  # Portrait on Strathmore newsprint
    "https://youtu.be/6rZ9bZFFYUs",  # Mo Salah Part 1 - مو صلاح الجزء الأول
    "https://youtu.be/FZR3PFYhXQ8",  # 22 Drawing with Charcoal | تدريب على الرسم باستخدام الفحم
    "https://youtu.be/0qQoSs5yBhE",  # 24 How to draw anime | طرق سهلة لرسم الانيمى
    "https://youtu.be/lgsAp0GqTTs",  # 25 How to Draw a Pose | كيفية رسم وضع ثابت وآخر متحرك
    "https://youtu.be/x0PbRRCk_V4",  # 26 How to draw a portrait | كيفية رسم بورتريه بالخطوات
    "https://www.youtube.com/watch?v=9WrZc0Jy8sA",  # Python Code to Import YouTube Video Captions
    "https://www.youtube.com/watch?v=XBawcyY4mBM&t=228s",
    # Text to Speech with Python Code|نطق النص باستخدام لغة بايثون
    "https://www.youtube.com/watch?v=GjnQFczsT34",  # Image to Pencil Sketch Using Python
    "https://www.youtube.com/watch?v=Mr33nlIGfL4",  # Let's Hack Wikipedia with Python
    "https://youtu.be/1cDaxMEAq50",  # Go hard or go home
    "https://youtu.be/F8pGbV1ejAk",  # Python | match case
    "https://youtu.be/pW-P4U1D-Ec",
    "https://youtu.be/8wtsTgul6s8",
    "https://youtu.be/fH8YOdxX6cI",
    "https://youtu.be/L5LjDYlcM-k"
]

for i in range(300):
    random_video = random.randint(0, len(videos)-1)
    driver.get(videos[random_video])
    print(f"========================================\n{driver.title}\n========================================")
    print("Watching for {} time".format(i))
    sleep_time = random.randint(60, 200)
    time.sleep(sleep_time)

driver.quit()
