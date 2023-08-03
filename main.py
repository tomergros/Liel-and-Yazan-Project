import streamlit as st

# Add custom CSS to make the content right-to-left and set the overall style
st.markdown(
    """
    <style>
        body {
            direction: rtl;
            background-color: #f7f7f7;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        .section {
            background-color: #ffffff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3, h4, h5, h6 {
            text-align: center;
            margin-bottom: 20px;
        }
        p {
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Section 1
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h1>זיהוי בריונות ברשתות החברתיות באמצעות בינה מלאכותית</h1>', unsafe_allow_html=True)
st.markdown('<h3>יזן מרעי וליאל יעקב</h3>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('בשנים האחרונות פלטפורמת הרשתות החברתיות תפסה תאוצה וכיום היא תופסת מקום משמעותי בחיים של כמעט כל אחד מאיתנו.')
st.markdown('הרשתות החברתיות מספקות דרך קלה ונוחה ליצירת קשר ושיתוף עם הסביבה שלנו וגם עם אנשים זרים מכל רחבי העולם.')
st.markdown('למעשה, כיום התקשורת המרכזית עם הסביבה שלנו מנוהלת דרך הרשתות החברתיות.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 2
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>רקע</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('עם זאת, ולמרות היתרונות שבדבר, קיים גם חיסרון לא מבוטל- בריונות. בריונות ברשת היא הטרדה או העלבת אדם על ידי שליחת הודעה,')
st.markdown('פרסום פוסט, תמונה או סירטון בעלי אופי פוגע או מאיים. תופעה זו משפיעה על כל המשתמשים ברשתות.')
st.markdown('ועלולה לגרום לנזק לבריאות הנפשית והפיזית של הקורבנות.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 3
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>מטרות</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('מטרת המחקר שלנו היא לאתר טקסטים פוגעניים ברשתות החברתיות על מנת למנוע מצבים של פגיעה במשתמשים ברשתות החברתיות.')
st.markdown('נעשה זאת באמצעות בינה מלאכותית.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 4
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>NLP MODELS</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('תחילה, ערכנו ניסוי לקביעת האלגוריתם המספק את התוצאות הכי טובות בין מספר מודלים שונים.')
st.markdown('ביצענו השוואה בין שלושה אלגוריתמי סיווג: Naive bayes, LSTM ו- BERT.')
st.markdown('את הבדיקות ערכנו על אותו סט נתונים המורכב מציוציי טוויטר ומסווג לתגובות פוגעניות ותגובות שאינן פוגעניות.')
st.markdown('סט הנתונים מכיל 7,945 תגובות לא פוגעניות ו-16,250 תגובות פוגעניות מקטגוריות שונות בשפה האנגלית.')
st.markdown('נוכחנו לגלות שמודל BERT מספק את התוצאות הטובות ביותר.')
st.markdown('תוצאות סיווג המודלים')
st.markdown('Naive Bayes &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; BERT &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; LSTM')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 5
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>Multilingual Bert</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('לאור התוצאות, בחרנו להשתמש לסט הנתונים בעברית וערבית במודל Multilingual Bert.')
st.markdown('זוהי גרסה של מודל BERT והיא מיודעת לעיבוד שפה טבעית במגוון שפות.')
st.markdown('המודל אומן על מאגר נתונים בשפות שונות. למודל זה מבנה דומה למודל BERT והוא מורכב משני שלבים עיקריים:')
st.markdown(' - Masked word אשר עוזר ללמידת קשרים בין מילים ו- Transformer layers על מנת ליצור ייצוגים למילים.')
st.markdown('מודל זה, משמש למגוון משימות בתחום עיבוד השפה, בין היתר ניתוח רגש של טקסטים בשפות שונות.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 6
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>דוגמא מתוך סט הנתונים בעברית וערבית בנפרד</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('סט הנתונים')
st.markdown('את הנתונים אנו אוספים מהרשת החברתית פייסבוק.')
st.markdown('אנו ממשיכים לאסוף נתונים בעבודה עצמית ומשתדלים לשמור על איזון בין שתי הקטגוריות של תגובות פוגעניות ושאינן פוגעניות.')
st.markdown('כמו כן, אנו מגוונים את הנתונים הנאספים מהרשת החברתית פייסבוק ומגוונים את סוגי הבריונות, למשל: פוליטיקה, גזענות,')
st.markdown('דת, מין וכו\' על מנת ליצור סט נתונים אותנטי ורחב ככל שנצליח.')
st.markdown('בכוונתנו להוסיף מקורות לאיסוף הנתונים כגון: אינסטגרם וטיקטוק. כידוע, ברשתות אלו שימושם של בני הנוער גדול משימושם בפייסבוק.')
st.markdown('לכן, בכדי שסט הנתונים יהיה עדכני, רלוונטי ותואם לבני הנוער- נאסוף נתונים גם משם.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 7
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>מדדים להערכות ביצועים</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('מדדים להערכות ביצועים')
st.markdown('את הערכות הביצועים שהתקבלו נשווה באמצעות שני מדדים: F1 score- זהו מדד לניתוח סטטיסטי של סיווג בינארי. הוא')
st.markdown('מחושב באופן הבא:')
st.markdown('- Recall (רגישות)- מספר התוצאות החיוביות שזוהו נכונה חלקי מספר כל הדגימות שהיו אמורות להיות מזוהות')
st.markdown('כחיוביות.')
st.markdown('- Precision- התוצאות החיוביות שהמודל זיהה נכון חלקי מספר כל התוצאות החיוביות (כולל אלו שלא זוהו כראוי). F1 score')
st.markdown('הוא ממוצע משוקלל של recall ו- precision')
st.markdown('- Accuracy (דיוק)- זהו המדד הפשוט ביותר. הוא מחשב את היחס בין הסיווגים הנכונים לבין סך כל הסיווגים.')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 8
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>הערכת ביצועים על סט הנתונים בעברית</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('[Insert the performance results for the Hebrew data here]')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 9
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>הערכת ביצועים על סט הנתונים בערבית</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('[Insert the performance results for the Arabic data here]')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 10
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2>הערכת ביצועים על סט הנתונים בעברית + ערבית</h2>', unsafe_allow_html=True)
st.markdown('<p>', unsafe_allow_html=True)
st.markdown('[Insert the performance results for the Hebrew + Arabic data here]')
st.markdown('</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
