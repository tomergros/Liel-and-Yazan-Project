import streamlit as st

# Function to add center alignment Markdown tag
def centered_text(text):
    return f'<p style="text-align: center;">{text}</p>'

# Section 1
st.markdown(centered_text('<h1>זיהוי בריונות ברשתות החברתיות באמצעות בינה מלאכותית</h1>'))
st.subheader('יזן מרעי וליאל יעקב')

# Section 2
st.markdown(centered_text('<h2>רקע</h2>'))
background_text = """
בשנים האחרונות פלטפורמת הרשתות החברתיות תפסה תאוצה וכיום היא תופסת מקום משמעותי בחיים של כמעט כל אחד מאיתנו. 
הרשתות החברתיות מספקות דרך קלה ונוחה ליצירת קשר ושיתוף עם הסביבה שלנו וגם עם אנשים זרים מכל רחבי העולם. למעשה, 
כיום התקשורת המרכזית עם הסביבה שלנו מנוהלת דרך הרשתות החברתיות.

עם זאת, ולמרות היתרונות שבדבר, קיים גם חיסרון לא מבוטל- בריונות. בריונות ברשת היא הטרדה או העלבת אדם על ידי שליחת הודעה, 
פרסום פוסט, תמונה או סירטון בעלי אופי פוגע או מאיים. תופעה זו משפיעה על כל המשתמשים ברשתות. ועלולה לגרום לנזק לבריאות הנפשית 
והפיזית של הקורבנות.
"""
st.markdown(centered_text(background_text))

# Section 3
st.markdown(centered_text('<h2>טרות</h2>'))
objectives_text = """
מטרת המחקר שלנו היא לאתר טקסטים פוגעניים ברשתות החברתיות על מנת למנוע מצבים של פגיעה במשתמשים ברשתות החברתיות.
נעשה זאת באמצעות בינה מלאכותית.

קיימות הצעות רבות אשר צלחו את האתגר בשפות שנות ובעיקרן השפה האנגלית.
לאחר שהצלחנו לקבל תוצאות טובות בשפה האנגלית, אנו עובדים על אלגוריתם המבוסס על מודל Multilingual Bert אשר יוכל לנתח טקסטים 
בשפות עברית וערבית.

בנוסף, אנו עובדים על כריית נתונים בשתי השפות הללו. הנתונים נלקחים מהרשת החברתית פייסבוק, על מנת ליצור סט נתונים המשלב 
את שתי השפות.

שפות אלו נחשבות קשות יותר לביצוע עיבוד טקסט ובנוסף, הפתרונות המוצעים בשפות אלו מעטים מאוד.

בכוונתנו להצליח, לאחר אימון והשגת הערכות ביצוע טובות, לבנות פונקציה אשר תקבל משפט חדש ותחזיר את ההסתברות של השייכות 
שלו לכל אחת מהקטגוריות. המטרה המרכזית היא שהמודל יפעל על השפות עברית וערבית יחדיו.
"""
st.markdown(centered_text(objectives_text))

# Section 4
st.markdown(centered_text('<h2>NLP MODELS</h2>'))
models_text = """
תחילה, ערכנו ניסוי לקביעת האלגוריתם המספק את התוצאות הכי טובות בין מספר מודלים שונים.

ביצענו השוואה בין שלושה אלגוריתמי סיווג: Naive bayes, LSTM ו- BERT.

את הבדיקות ערכנו על אותו סט נתונים המורכב מציוציי טוויטר ומסווג לתגובות פוגעניות ותגובות שאינן פוגעניות.

סט הנתונים מכיל 7,945 תגובות לא פוגעניות ו-16,250 תגובות פוגעניות מקטגוריות שונות בשפה האנגלית.

נוכחנו לגלות שמודל BERT מספק את התוצאות הטובות ביותר.
"""
st.markdown(centered_text(models_text))

# Section 5
st.markdown(centered_text('<h2>Multilingual Bert</h2>'))
multilingual_bert_text = """
לאור התוצאות, בחרנו להשתמש לסט הנתונים בעברית וערבית במודל Multilingual Bert.

זוהי גרסה של מודל BERT והיא מיודעת לעיבוד שפה טבעית במגוון שפות.

המודל אומן על מאגר נתונים בשפות שונות. למודל זה מבנה דומה למודל BERT והוא מורכב משני שלבים עיקריים:

Masked word אשר עוזר ללמידת קשרים בין מילים ו- Transformer layers על מנת ליצור ייצוגים למילים.

מודל זה, משמש למגוון משימות בתחום עיבוד השפה, בין היתר ניתוח רגש של טקסטים בשפות שונות.
"""
st.markdown(centered_text(multilingual_bert_text))

# Section 6
st.markdown(centered_text('<h2>Example from the dataset in Hebrew and Arabic</h2>'))
example_data_text = """
סט הנתונים
את הנתונים אנו אוספים מהרשת החברתית פייסבוק.

אנו ממשיכים לאסוף נתונים בעבודה עצמית ומשתדלים לשמור על איזון בין שתי הקטגוריות של תגובות פוגעניות ושאינן פוגעניות.

כמו כן, אנו מגוונים את הנתונים הנאספים מהרשת החברתית פייסבוק ומגוונים את סוגי הבריונות, למשל: פוליטיקה, גזענות, דת, מין וכו' 
על מנת ליצור סט נתונים אותנטי ורחב ככל שנצליח.

בכוונתנו להוסיף מקורות לאיסוף הנתונים כגון: אינסטגרם וטיקטוק. כידוע, ברשתות אלו שימושם של בני הנוער גדול משימושם 
בפייסבוק. לכן, בכדי שסט הנתונים יהיה עדכני, רלוונטי ותואם לבני הנוער- נאסוף נתונים גם משם.
"""
st.markdown(centered_text(example_data_text))

# Section 7
st.markdown(centered_text('<h2>Performance Metrics</h2>'))
performance_metrics_text = """
את הערכות הביצועים שהתקבלו נשווה באמצעות שני מדדים: F1 score- זהו מדד לניתוח סטטיסטי של סיווג בינארי. 
הוא מחושב באופן הבא:

- Recall (רגישות)- מספר התוצאות החיוביות שזוהו נכונה חלקי מספר כל הדגימות שהיו אמורות להיות מזוהות כחיוביות.

- Precision- התוצאות החיוביות שהמודל זיהה נכון חלקי מספר כל התוצאות החיוביות (כולל אלו שלא זוהו כראוי). F1 score הוא 
ממוצע משוקלל של recall ו- precision

- Accuracy (דיוק)- זהו המדד הפשוט ביותר. הוא מחשב את היחס בין הסיווגים הנכונים לבין סך כל הסיווגים.
"""
st.markdown(centered_text(performance_metrics_text))

# Section 8
st.markdown(centered_text('<h2>Performance Evaluation on the Hebrew Dataset</h2>'))
hebrew_performance_text = """
...
"""
st.markdown(centered_text(hebrew_performance_text))

# Section 9
st.markdown(centered_text('<h2>Performance Evaluation on the Arabic Dataset</h2>'))
arabic_performance_text = """
...
"""
st.markdown(centered_text(arabic_performance_text))

# Section 10
st.markdown(centered_text('<h2>Performance Evaluation on the Hebrew + Arabic Dataset</h2>'))
hebrew_arabic_performance_text = """
...
"""
st.markdown(centered_text(hebrew_arabic_performance_text))
