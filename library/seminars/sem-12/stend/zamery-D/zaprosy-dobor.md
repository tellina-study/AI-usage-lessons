# Запросы добора — кейс D, круг 3 (issue #351)

62 новых запроса на 61 добранный снимок (один снимок, `8cb7d659`, из первых сорока —
чтобы довести общее число ровно до ста). Вместе с 38 запросами первого круга — **100**.

Три класса сохранены:
- **К-слово** — запрос говорит словами, которые РЕАЛЬНО есть в рассказе модели
  (проверено по `opisaniya-101.json`);
- **К-пересказ** — та же сцена другими словами, лексика рассказа намеренно не
  используется;
- **К-деталь** — деталь, которая ЕСТЬ в человеческой разметке и которую рассказ
  НЕ назвал (проверено по обоим файлам).

Единственность верного ответа проверена программой (`proverka_edinstvennosti.py`)
и прочитана глазами: совпадения различающего слова в разметке других снимков
корпуса разобраны поимённо.

| № | класс | RU | EN | ответ |
|---|---|---|---|---|
| 4.1 | К-пересказ | взрослые слушатели пишут от руки за одноместными партами в несколько рядов | adult learners writing by hand at single desks in several rows | 01f26ca5 |
| 4.2 | К-слово | класс с голубыми стенами и старыми компьютерами на заднем плане | a classroom with blue walls and old computers in the background | 0329b7ef |
| 4.3 | К-деталь | чёрный зонт и бумажный пакет с ручками лежат в пустом классе | a black umbrella and a paper bag with handles in an empty classroom | 03cb58df |
| 4.4 | К-деталь | пустой класс с потолочным вентилятором на пять лопастей | an empty classroom with a five-blade ceiling fan | 0b3445ee |
| 4.5 | К-слово | спикер объясняет программу запуска, зрительница снимает его на смартфон | a speaker explaining a launch programme while a woman films him on a phone | 0e4332e5 |
| 4.6 | К-пересказ | занятие, на котором один из сидящих тянет руку вверх | a class where one of the seated people raises a hand | 1102e183 |
| 4.7 | К-пересказ | докладчик в костюме за массивной деревянной кафедрой, слушателей в кадре нет | a man in a suit behind a massive wooden lectern, no audience in frame | 128f5826 |
| 4.8 | К-деталь | проекция веб-формы с текстом на французском языке | a projected web form with text in French | 145e02a1 |
| 4.9 | К-пересказ | единственный человек в переговорной смотрит на доску с выкладками | the only person in a meeting room looking at a board of equations | 163fe17e |
| 4.10 | К-слово | школьница объясняет свою научно-исследовательскую работу у стенда | a schoolgirl explaining her research project at a poster stand | 24955fd6 |
| 4.11 | К-деталь | на экране исходный код на языке C с вызовом printf | source code in C with a printf call on the screen | 2c0dbd6d |
| 4.12 | К-деталь | флипчарт, на котором красным маркером написано Greenpeace | a flipchart with Greenpeace written in red marker | 30dc8f6e |
| 4.13 | К-деталь | зал, где на задник крупно написано 100% design shanghai | a hall with 100% design shanghai written large on the backdrop | 14bad13e |
| 4.14 | К-пересказ | ряды складных столов в пустом учебном зале, в дальней стене яркая дверь | rows of folding tables in an empty training room with a bright door in the far wall | 0493f305 |
| 4.15 | К-слово | контрольный центр управления космическими миссиями с рядами красных кресел | a mission control centre with rows of red seats | 05162223 |
| 4.16 | К-пересказ | большое международное заседание сверху, докладчик показан на экране трансляцией | a large international assembly from above with the speaker shown on a broadcast screen | 1d810b4d |
| 4.17 | К-пересказ | пустой кинотеатр с красными портьерами и засвеченным белым экраном | an empty cinema with red drapes and a blank white screen | 004e67c0 |
| 4.18 | К-деталь | настольная табличка с именем Paco Ragageles | a desk nameplate reading Paco Ragageles | 0e6e608a |
| 4.19 | К-пересказ | выступление с трибуны, за спиной двое сидят в президиуме | a speech from a tribune with two men seated at the presidium behind | 190d1af3 |
| 4.20 | К-слово | женщина выступает на фоне задника North Central College | a woman speaking in front of a North Central College backdrop | 1fd783e4 |
| 4.21 | К-слово | мужчина у микрофона на фоне синего баннера FDP Düsseldorf | a man at a microphone against a blue FDP Düsseldorf banner | 2e6df1ce |
| 4.22 | К-деталь | доска, на которой написано Install / Uninstall | a whiteboard with Install / Uninstall written on it | 1eb99df4 |
| 4.23 | К-деталь | конференц-телефон звездообразной формы на столе переговорной | a star-shaped conference phone on a meeting table | 38af0f20 |
| 4.24 | К-деталь | кружка с надписью Natural History Museum of Los Angeles | a mug reading Natural History Museum of Los Angeles | 3a739b0a |
| 4.25 | К-слово | зал с роллапом Kennedy Center Conversations | a room with a Kennedy Center Conversations banner | 0319000d |
| 4.26 | К-деталь | лист с пунктами Porter's generic и Ansoff's growth vector | a sheet listing Porter's generic and Ansoff's growth vector | 069dc9e7 |
| 4.27 | К-слово | рисунок двух профилей головы с надписью exhale | a drawing of two head profiles with the word exhale | 186adccd |
| 4.28 | К-слово | меловая доска с формулами и рисунками теории узлов | a chalkboard with formulas and knot theory diagrams | 05bd562a |
| 4.29 | К-пересказ | человек спиной к камере чертит мелом одну фигуру на почти пустой доске | a person with their back to the camera drawing a single shape in chalk on a nearly empty board | 071c6356 |
| 4.30 | К-деталь | флипчарт со строкой Create an animal в списке функций | a flipchart with the line Create an animal in a feature list | 1973cd54 |
| 4.31 | К-слово | доска с хронологией и табличкой Erase Daily | a board with a timeline and an Erase Daily sign | 22926e7f |
| 4.32 | К-слово | доска с заметками про Skype и Google Docs | a whiteboard with notes about Skype and Google Docs | 235a6e57 |
| 4.33 | К-слово | меловая вывеска с надписями мороженое, эспрессо и десерты | a chalkboard sign reading ice cream, espresso and desserts | 18ccdc56 |
| 4.34 | К-деталь | поднос с пятью чашками, рядом лежат звёздочки бадьяна | a tray of five cups with star anise lying beside them | 0071f62f |
| 4.35 | К-слово | белая кружка с рисунком белки и птицы | a white mug drawn with a squirrel and a bird | 05063174 |
| 4.36 | К-слово | чашка капучино с логотипом Segafredo | a cappuccino cup with the Segafredo logo | 0656563f |
| 4.37 | К-деталь | кофе по-восточному в чеканном медном подстаканнике | Turkish coffee in an embossed copper cup holder | 01c715ad |
| 4.38 | К-деталь | школьная библиотека с табличкой Mr. Jim Morris Library | a school library with a Mr. Jim Morris Library sign | 09f08ac7 |
| 4.39 | К-слово | библиотека с рукописной табличкой American Literature, Poetry, Drama | a library with a handwritten American Literature, Poetry, Drama sign | 0a951714 |
| 4.40 | К-деталь | книжный магазин с плакатами William Gibson | a bookshop with William Gibson posters | 11789876 |
| 4.41 | К-слово | книжная полка с томом La Conquista de la Civilización | a bookshelf with a volume titled La Conquista de la Civilización | 147de698 |
| 4.42 | К-деталь | девушка снимает книгу с полки, где стоят книги про оперу | a girl taking a book from a shelf of books about opera | 19aa0e0a |
| 4.43 | К-слово | проход между стеллажами с табличкой Fiction | an aisle between shelves with a Fiction sign | 11c10d9d |
| 4.44 | К-пересказ | лаборатория без людей, на стене периодическая таблица в рамке | an empty laboratory with a framed periodic table on the wall | 0bc70153 |
| 4.45 | К-деталь | лаборант в защитном щитке, на стене табличка Thermo | a lab worker in a face shield with a Thermo sign on the wall | 10dfe877 |
| 4.46 | К-пересказ | четверо в белых халатах позируют у стола с цветными штативами для пробирок | four people in lab coats posing at a bench with coloured tube racks | 11cd7194 |
| 4.47 | К-пересказ | двое в одноразовых шапочках разбирают раковины в синих лотках | two people in hairnets sorting shells in blue trays | 26f3e4d6 |
| 4.48 | К-пересказ | работники в комбинезонах у линии, наполняющей стаканчики | workers in coveralls at a line filling small cups | 2944a2f2 |
| 4.49 | К-деталь | женщина пипетирует над чашками Петри с красной средой | a woman pipetting over Petri dishes with red medium | 57ca2239 |
| 4.50 | К-деталь | мастер в бандане у торцовочной пилы | a craftsman in a bandana at a mitre saw | 6598fc49 |
| 4.51 | К-деталь | столярная мастерская со станком Wadkin и деревянными колёсами | a woodworking shop with a Wadkin machine and wooden wheels | 67310c81 |
| 4.52 | К-пересказ | двое склонились над оптическим столом с линзами и зеркалами | two people leaning over an optical table with lenses and mirrors | 7348dec4 |
| 4.53 | К-пересказ | необработанная рама велосипеда зажата в ремонтной стойке | a bare bicycle frame clamped in a repair stand | 806c7b43 |
| 4.54 | К-деталь | занятие за ноутбуками, рядом лежит книга с надписью ТЕТРИС | a class at laptops with a book titled ТЕТРИС lying nearby | 5387c89f |
| 4.55 | К-пересказ | поршневой самолёт с трёхлопастным винтом выставлен в ангаре | a propeller aircraft with a three-blade prop on display in a hangar | 07a41b00 |
| 4.56 | К-слово | старинный театр, на экране одно слово Questions | an ornate theatre with the single word Questions on the screen | 027b1638 |
| 4.57 | К-пересказ | одинокий зритель в пустом зале под потолком с точечными огнями | a lone viewer in an empty hall under a ceiling of pinpoint lights | 0b37c87f |
| 4.58 | К-пересказ | полукруглый парламентский зал с красными скамьями и лестницей по центру | a semicircular parliamentary chamber with red benches and a central staircase | 0dd052cc |
| 4.59 | К-слово | круглый зал заседаний, в центре играет струнный ансамбль | a round assembly hall with a string ensemble playing in the centre | 12419790 |
| 4.60 | К-пересказ | пустой зал с оранжевыми креслами и белым реечным потолком | an empty hall with orange seats and a white slatted ceiling | 2106a1f6 |
| 4.61 | К-деталь | зал, где на экране логотип CiU | a hall with the CiU logo on the screen | 2ec2e501 |
| 4.62 | К-пересказ | два металлических подноса с кофе по-восточному и рахат-лукумом | two metal trays with Turkish coffee and Turkish delight | 8cb7d659 |
