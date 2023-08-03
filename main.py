import streamlit as st

# Add custom CSS to make the content right-to-left
st.markdown(
    """
    <style>
        body {
            direction: rtl;
        }
        h1, h2, h3, h4, h5, h6, p {
            text-align: center;
        }
        .section {
            margin: 2rem 0;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .section1 { background-color: #eef2f5; }
        .section2 { background-color: #f9f1e7; }
        .section3 { background-color: #e7f0f9; }
        .section4 { background-color: #f1e7f5; }
        .section5 { background-color: #e7f9f0; }
        .section6 { background-color: #f0e7f9; }
        .section7 { background-color: #e7f5f1; }
        .section8 { background-color: #f9e7f0; }
        .section9 { background-color: #f5e7f1; }
        .section10 { background-color: #e7f1e5; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Section 1
st.markdown('<div class="section section1">', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center;"dir="rtl">זיהוי בריונות ברשתות החברתיות באמצעות בינה מלאכותית</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center;"dir="rtl">יזן מרעי וליאל יעקב</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 2
st.markdown('<div class="section section2">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">רקע</h2>', unsafe_allow_html=True)

background_text = """
בשנים האחרונות פלטפורמת הרשתות החברתיות תפסה תאוצה וכיום היא תופסת מקום משמעותי בחיים של כמעט כל אחד מאיתנו. 
הרשתות החברתיות מספקות דרך קלה ונוחה ליצירת קשר ושיתוף עם הסביבה שלנו וגם עם אנשים זרים מכל רחבי העולם. 
למעשה, כיום התקשורת המרכזית עם הסביבה שלנו מנוהלת דרך הרשתות החברתיות.

עם זאת, ולמרות היתרונות שבדבר, קיים גם חיסרון לא מבוטל- בריונות. בריונות ברשת היא הטרדה או העלבת אדם על ידי שליחת הודעה, 
פרסום פוסט, תמונה או סירטון בעלי אופי פוגע או מאיים. תופעה זו משפיעה על כל המשתמשים ברשתות. 
ועלולה לגרום לנזק לבריאות הנפשית והפיזית של הקורבנות.
"""

st.write(background_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 3
st.markdown('<div class="section section3">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">מטרות</h2>', unsafe_allow_html=True)

objectives_text = """
מטרת המחקר שלנו היא לאתר טקסטים פוגעניים ברשתות החברתיות על מנת למנוע מצבים של פגיעה במשתמשים ברשתות החברתיות.
נעשה זאת באמצעות בינה מלאכותית.

קיימות הצעות רבות אשר צלחו את האתגר בשפות שנות ובעיקרן השפה האנגלית.
לאחר שהצלחנו לקבל תוצאות טובות בשפה האנגלית, אנו עובדים על אלגוריתם המבוסס על מודל Multilingual Bert אשר יוכל לנתח 
טקסטים בשפות עברית וערבית.

בנוסף, אנו עובדים על כריית נתונים בשתי השפות הללו. הנתונים נלקחים מהרשת החברתית פייסבוק, על מנת ליצור סט נתונים 
המשלב את שתי השפות.

שפות אלו נחשבות קשות יותר לביצוע עיבוד טקסט ובנוסף, הפתרונות המוצעים בשפות אלו מעטים מאוד.

בכוונתנו להצליח, לאחר אימון והשגת הערכות ביצוע טובות, לבנות פונקציה אשר תקבל משפט חדש ותחזיר את ההסתברות של 
השייכות שלו לכל אחת מהקטגוריות. המטרה המרכזית היא שהמודל יפעל על השפות עברית וערבית יחדיו.
"""

st.write(objectives_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 4
st.markdown('<div class="section section4">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">NLP MODELS</h2>', unsafe_allow_html=True)

nlp_models_text = """
תחילה, ערכנו ניסוי לקביעת האלגוריתם המספק את התוצאות הכי טובות בין מספר מודלים שונים.

ביצענו השוואה בין שלושה אלגוריתמי סיווג: Naive bayes, LSTM ו- BERT.

את הבדיקות ערכנו על אותו סט נתונים המורכב מציוציי טוויטר ומסווג לתגובות פוגעניות ותגובות שאינן פוגעניות.

סט הנתונים מכיל 7,945 תגובות לא פוגעניות ו-16,250 תגובות פוגעניות מקטגוריות שונות בשפה האנגלית.

נוכחנו לגלות שמודל BERT מספק את התוצאות הטובות ביותר.

תוצאות סיווג המודלים
Naive Bayes                                 BERT                                LSTM 
"""

st.write(nlp_models_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 5
st.markdown('<div class="section section5">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">Multilingual Bert</h2>', unsafe_allow_html=True)

multilingual_bert_text = """
לאור התוצאות, בחרנו להשתמש לסט הנתונים בעברית וערבית במודל Multilingual Bert.

זוהי גרסה של מודל BERT והיא מיודעת לעיבוד שפה טבעית במגוון שפות.

המודל אומן על מאגר נתונים בשפות שונות. למודל זה מבנה דומה למודל BERT והוא מורכב משני שלבים עיקריים:

- Masked word אשר עוזר ללמידת קשרים בין מילים ו- Transformer layers על מנת ליצור ייצוגים למילים.

מודל זה, משמש למגוון משימות בתחום עיבוד השפה, בין היתר ניתוח רגש של טקסטים בשפות שונות.
"""

st.write(multilingual_bert_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 6
st.markdown('<div class="section section6">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">דוגמא מתוך סט הנתונים בעברית וערבית בנפרד</h2>', unsafe_allow_html=True)

example_data_text = """
סט הנתונים
את הנתונים אנו אוספים מהרשת החברתית פייסבוק.

אנו ממשיכים לאסוף נתונים בעבודה עצמית ומשתדלים לשמור על איזון בין שתי הקטגוריות של תגובות פוגעניות ושאינן פוגעניות.

כמו כן, אנו מגוונים את הנתונים הנאספים מהרשת החברתית פייסבוק ומגוונים את סוגי הבריונות, למשל: פוליטיקה, גזענות, 
דת, מין וכו' על מנת ליצור סט נתונים אותנטי ורחב ככל שנצליח.

בכוונתנו להוסיף מקורות לאיסוף הנתונים כגון: אינסטגרם וטיקטוק. כידוע, ברשתות אלו שימושם של בני הנוער גדול משימושם בפייסבוק. 
לכן, בכדי שסט הנתונים יהיה עדכני, רלוונטי ותואם לבני הנוער- נאסוף נתונים גם משם.
"""

st.write(example_data_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 7
st.markdown('<div class="section section7">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">מדדים להערכות ביצועים</h2>', unsafe_allow_html=True)

performance_metrics_text = """
מדדים להערכות ביצועים
את הערכות הביצועים שהתקבלו נשווה באמצעות שני מדדים: F1 score- זהו מדד לניתוח סטטיסטי של סיווג בינארי. הוא 
מחושב באופן הבא:

- Recall (רגישות)- מספר התוצאות החיוביות שזוהו נכונה חלקי מספר כל הדגימות שהיו אמורות להיות מזוהות 
כחיוביות.

- Precision- התוצאות החיוביות שהמודל זיהה נכון חלקי מספר כל התוצאות החיוביות (כולל אלו שלא זוהו כראוי). F1 score 
הוא ממוצע משוקלל של recall ו- precision

- Accuracy (דיוק)- זהו המדד הפשוט ביותר. הוא מחשב את היחס בין הסיווגים הנכונים לבין סך כל הסיווגים.
"""

st.write(performance_metrics_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 8
st.markdown('<div class="section section8">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">הערכת ביצועים על סט הנתונים בעברית</h2>', unsafe_allow_html=True)

hebrew_performance_text = """
[Insert the performance results for the Hebrew data here]
"""

st.write(hebrew_performance_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 9
st.markdown('<div class="section section9">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">הערכת ביצועים על סט הנתונים בערבית</h2>', unsafe_allow_html=True)

arabic_performance_text = """
[Insert the performance results for the Arabic data here]
"""

st.write(arabic_performance_text)
st.markdown('</div>', unsafe_allow_html=True)

# Section 10
st.markdown('<div class="section section10">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;"dir="rtl">הערכת ביצועים על סט הנתונים בעברית + ערבית</h2>', unsafe_allow_html=True)

hebrew_arabic_performance_text = """
[Insert the performance results for the Hebrew + Arabic data here]
"""

st.write(hebrew_arabic_performance_text)
st.markdown('</div>', unsafe_allow_html=True)
