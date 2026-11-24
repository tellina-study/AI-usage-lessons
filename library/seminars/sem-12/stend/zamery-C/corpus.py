"""Корпус замера Кейса C (Семинар 12, issue #351) — курация сессией производства,
2026-11-24. Три класса по определениям владельца (дословно):

у1′ (курение): «в кадре либо человек курит: сигарета, вейп или трубка, зажжённая, во рту
или в руке; либо присутствует изображение курения — плакат, реклама на стене, кадр на
экране».
е1 (еда/напитки): «человек ест или пьёт, либо накрытый стол как главный сюжет кадра».
с1 (слайды): «в кадре читаемый экран или проекция с НАШИМ учебным материалом».

Курация — просмотр глазами, Open Images V7, лицензии CC BY 2.0 (train) / потоковая сверка
(val/test — унаследовано из гейта Вехи 1). Пути ниже — локальный кэш /tmp/s12-corpora
(детерминированно пересобирается download.py по спискам id; бинарники в гит не кладём,
кроме снимков, попадающих на кадры — см. README §«Бинарники»).
"""

ROOT = "/tmp/s12-corpora/oiv7/images"

# ---------------------------------------------------------------------------
# КУРЕНИЕ (у1′) — два среза Open Images: val/test (пул "C-smoking", n=29,
# human-verified Cigarette) и train-добор (пул "C-smoking-train", n=45).
# Курация по месту (эта сессия, 2026-11-24): смотрено ВСЕ 29 + 29 новых из 45
# (16 уже были просмотрены планировщиком в dobor-kureniya-C.md).
# ---------------------------------------------------------------------------

SMOKE_VALTEST_DIR = f"{ROOT}/C-smoking"
SMOKE_TRAIN_DIR = f"{ROOT}/C-smoking-train"
SMOKE_NEG_DIR = f"{ROOT}/C-smoking-negtrain"

# valtest: позитив (реальная сцена или трубка) — 8 из 29
SMOKE_VALTEST_POS = [
    "15fba4beb52be52e",  # сигарета во рту, держит рукой
    "2f75c267eaae09c1",  # лит сигарета крупно в пальцах
    "5a72ab259fd5b1c1",  # рука держит сигару/сигариллу (стилизовано)
    "b7199832d9292db7",  # рука держит сигару (Black Card Circle)
    "bb2ef38b94a0ad64",  # рука держит докуренную сигару, пепел виден
    "c90736fcc9178e57",  # человек, сигара во рту (клоунский нос)
    "d40df2c9c3502418",  # человек в костюме, сигарета в руке
    "db28538e45492009",  # картина/иллюстрация — портрет человека с сигаретой во рту (изображение курения)
]
# valtest: спорное (не считается ни позитивом, ни чистым негативом)
SMOKE_VALTEST_DISPUTED = [
    "df84409947ebac1f",  # рука держит коробку сигар закрытой, не держит сигару к курению
]
# valtest: жёсткий негатив (предмет курения БЕЗ человека — «ведро окурков» и его сёстры)
SMOKE_VALTEST_HARDNEG = [
    "193d76cd49bb8a7c", "22878e150531f81b", "2f9d652e8c4f646d", "4230170c98d9d730",
    "47847d1252634266", "59239ec9f2ae25c2", "5b69ca533d637c35", "5e58244e8c2b53f8",
    "5fd250e28fbd65d9", "66d785c363ff444d", "66e9d024ea9701c5", "6e64f997d2d451ee",
    "7f60ed58af09f235", "843f37af2b6b18d7", "982094dae613c947", "c174e3f7549f52cd",
    "dd3f4b9e08d54a5a", "e6df75e921a95b69", "ec30b1516bf8210c", "f3c1512f7bb2a051",
]

# train (добор): 10 исходных "чистых" + 1 трубка (планировщик) + 17 новых сцен/картинок
# (эта сессия) = 27 сцен + 6 изображений (плакаты/мем) = 33 позитива
SMOKE_TRAIN_POS_SCENE = [
    "0003380d95eaf99c", "0007a0dde58cd382", "0030ef716179c502", "0032a741dee9449b",
    "00388903eae56d69", "003ceac72cb29c12", "005095df542144d7", "0054fa940b942d58",
    "00579fe21142c431", "005c55202efbfdfc",
    "0372d1ed244de778", "00876da7b281d83d", "01b3fa4d58dcf9d3", "0096c39550048994",
    "038d9492135ff628", "04675cd1a612eca0", "01321b89db43a992", "0285d0cf30462c3e",
    "01c5af0058738ac5", "01e95b47d925938f", "03cf8d97304216a7", "030f47c0b7f00d8b",
    "01b07e6cf5803e5b", "0391a5072165aaca", "0411503afc48de41", "01cc6f7af3d2473e",
    "03b90f52e565bb6c",
]
SMOKE_TRAIN_POS_IMAGE = [
    "00154a65750ba41c",  # винтажная табачная реклама (трубка)
    "001d028a021c9c00",  # винтажная табачная реклама
    "0214841d8f27d4aa",  # Prince Albert — иллюстрированная реклама трубочного табака
    "00b425b6d0d57e23",  # клубный флаер, иллюстрация курящей женщины
    "01297bdd91d0a88e",  # фотопринт на стене (постановочный, не сцена в кадре)
    "0252f924309f1995",  # мем/композит — футболист с сигаретой (графика)
]
SMOKE_TRAIN_DISPUTED = [
    "00241d2d17854006", "00255392a087eceb", "00755995df29da87",
    "021daf9fc3a80591", "0189426ecfd8f61b", "014382bcc5e2d950",
]
SMOKE_TRAIN_HARDNEG = [
    "0445b4d76ac14531", "0220ab040afff51d", "01b14dd11981549a",
    "012947d2d021dd50", "0166a717de146cd3",
]
SMOKE_TRAIN_MINOR_EXCLUDED = ["0082f53c622d1607"]  # несовершеннолетний — исключён из корпуса целиком

SMOKE_POS = [(SMOKE_VALTEST_DIR, i) for i in SMOKE_VALTEST_POS] + \
            [(SMOKE_TRAIN_DIR, i) for i in (SMOKE_TRAIN_POS_SCENE + SMOKE_TRAIN_POS_IMAGE)]
SMOKE_HARDNEG = [(SMOKE_VALTEST_DIR, i) for i in SMOKE_VALTEST_HARDNEG] + \
                [(SMOKE_TRAIN_DIR, i) for i in SMOKE_TRAIN_HARDNEG]
SMOKE_DISPUTED = [(SMOKE_VALTEST_DIR, i) for i in SMOKE_VALTEST_DISPUTED] + \
                 [(SMOKE_TRAIN_DIR, i) for i in SMOKE_TRAIN_DISPUTED]

# общие верифицированные train-негативы (confidence=0 на Cigarette/Smoking), 68 скачано
import os as _os
SMOKE_GENERAL_NEG = []
if _os.path.isdir(SMOKE_NEG_DIR):
    SMOKE_GENERAL_NEG = [(SMOKE_NEG_DIR, f[:-4]) for f in sorted(_os.listdir(SMOKE_NEG_DIR)) if f.endswith(".jpg")]

SMOKE_NEG = SMOKE_HARDNEG + SMOKE_GENERAL_NEG

# ---------------------------------------------------------------------------
# ЕДА И НАПИТКИ (е1) — пул "C-fooddrink" (n=20), курация этой сессией.
# Находка: 5 "Eating"-меток — животные, не человек (бизнес-грязь, не предмет без
# человека, а вид без человека вовсе); 4 — несовершеннолетние, исключены из корпуса.
# ---------------------------------------------------------------------------

FOOD_DIR = f"{ROOT}/C-fooddrink"
FOOD_POS = [
    "159de001bfb786cc", "15e9b294ab1c9bb8", "4cc6594e5a81162a", "5218a7258cd54dd0",
    "7223abf5fc60cbb4", "70a61cf7d0a51719", "b8dbe2c5a8a33cbe", "e3ca366459aaf6a6",
    "e4f6f67849b772de",
]
FOOD_DISPUTED = ["6fdf51d6dafe5500", "ae959e75982f7893"]
FOOD_ANIMAL_NEG = [
    "37cdf8492162cf2e",  # мандрил ест цветы
    "3f48de9fc0ac6c7c",  # як пасётся
    "900092a93d030a2a",  # орикс пасётся
    "e80140fde875ac3b",  # тапиры
    "f7675857876745bb",  # лев ест тушу антилопы
]
FOOD_MINOR_EXCLUDED = ["6a2f8c186f7b9147", "b94f40cd91558896", "f0520cf6a9eaff69", "5510464f3352ae95"]

# негативы «люди на мероприятии, не едят» — переиспользуем срез B (та же разметка
# глазами, что сделала сессия кейса B; обоснование переиспользования — PEREDELKA §9,
# единый корпус фотографий на кейсы B и C)
B_SCENE_DIRS = ["B-classroom", "B-coffee", "B-conference", "B-lecture",
                "B-meeting", "B-seminar", "B-speaking", "B-whiteboard"]
FOOD_B_NEG = []
for d in B_SCENE_DIRS:
    p = f"{ROOT}/{d}"
    if _os.path.isdir(p):
        FOOD_B_NEG += [(p, f[:-4]) for f in sorted(_os.listdir(p)) if f.endswith(".jpg")]

FOOD_POS_FULL = [(FOOD_DIR, i) for i in FOOD_POS]
FOOD_NEG = [(FOOD_DIR, i) for i in FOOD_ANIMAL_NEG] + FOOD_B_NEG

# ---------------------------------------------------------------------------
# СЛАЙДЫ (с1), ступень 1 (экран/проекция в кадре, НЕ «наш ли материал») — пул
# "C-slides" (n=22, Open Images Presentation/Projection screen). Спот-чек 6/22:
# 3 читаемых экрана, 3 экрана пустых/нечитаемых — обе группы остаются
# business-негативом по с1 целиком (чужой материал), но дают стадии 1 трудный/
# лёгкий случай (экран пустой vs экран с крупным текстом).
# ---------------------------------------------------------------------------

SLIDES_DIR = f"{ROOT}/C-slides"
SLIDES_SCREEN_PRESENT = []
if _os.path.isdir(SLIDES_DIR):
    SLIDES_SCREEN_PRESENT = [(SLIDES_DIR, f[:-4]) for f in sorted(_os.listdir(SLIDES_DIR)) if f.endswith(".jpg")]
# читаемый подмножество (спот-чек глазами этой сессии)
SLIDES_READABLE = {"0cd992ac5ca38878", "1f8cabb4593744bc", "216f77a3366db4d1"}
SLIDES_BLANK = {"0941817c92716021", "11a303c2b9360432", "5161f0efe9c9f131"}

# негатив ступени 1 (экрана в кадре нет вовсе) — переиспользуем те же B-сцены
SLIDES_SCREEN_ABSENT = FOOD_B_NEG


def all_unique_images():
    """Возвращает множество уникальных (dir, id) по всему корпусу — для расчёта,
    сколько реальных vision-вызовов нужно (один вызов на уникальный кадр, флаги
    по трём классам разом)."""
    s = set()
    for lst in (SMOKE_POS, SMOKE_NEG, SMOKE_DISPUTED, FOOD_POS_FULL, FOOD_NEG,
                SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT):
        s.update(lst)
    return sorted(s)


if __name__ == "__main__":
    print("smoke pos", len(SMOKE_POS), "neg", len(SMOKE_NEG), "disputed", len(SMOKE_DISPUTED))
    print("food pos", len(FOOD_POS_FULL), "neg", len(FOOD_NEG))
    print("slides screen-present", len(SLIDES_SCREEN_PRESENT), "screen-absent", len(SLIDES_SCREEN_ABSENT))
    print("unique images total", len(all_unique_images()))
