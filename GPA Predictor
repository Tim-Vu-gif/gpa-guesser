import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Student_performance_data _.csv")

X = df.drop(['StudentID', 'GPA', 'GradeClass'], axis=1)
y = df['GPA']

categorical_cols = ['Gender','Ethnicity','ParentalEducation','Tutoring','ParentalSupport',
                            'Extracurricular','Sports','Music','Volunteering']

X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

feature_columns = X.columns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

error = mean_squared_error(y_test, y_pred)
score = model.score(X_test, y_test)

st.title("🎓GPA Guesser")

st.markdown("### Enter student info below to predict GPA:")
col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12 =  st.columns(12)
#columns
with st.expander("📋 Basic Info"):
    Age = st.number_input('Age', min_value=5, max_value=99,step=1)
    Gender = st.radio('Gender', ('Male','Female'),horizontal=True)
    Ethnicity = st.radio('Ethnicity', ('Asian', 'White', 'African','Hispanic','Other'),horizontal=True)
with st.expander("🏫 Academic Info"):
    ParentalEducation = st.radio('Parental Education', ('HighSchool','Bachelors','Masters','Other'),horizontal=True)
    StudyTimeWeekly = st.number_input('StudyTimeWeekly',step=1)
    Absences = st.number_input('Absences',step=1)
with st.expander("🎯 Activities"):
    Tutoring = st.radio('Tutoring', ('Yes','No') ,horizontal=True)
    ParentalSupport = st.radio('Parental Support', ('Yes','No'),horizontal=True)
    Extracurricular = st.radio('Extracurricular', ('Yes','No'),horizontal=True)
    Sports = st.radio('Sports', ('Yes','No'),horizontal=True)
    Music =st.radio('Music', ('Yes','No'),horizontal=True)
    Volunteering = st.radio('Volunteering', ('Yes','No'),horizontal=True)

new = pd.DataFrame(columns=feature_columns)
new.loc[0] = 0

new.at[0, "Age"] = Age
new.at[0, "StudyTimeWeekly"] = StudyTimeWeekly
new.at[0, "Absences"] = Absences

if "Gender_Female" in new.columns and Gender == "Female":
    new.at[0, "Gender_Female"] = 1

temp_eth = pd.get_dummies(pd.DataFrame({'Ethnicity':[Ethnicity]}), columns=['Ethnicity'], drop_first=True)
for col in temp_eth.columns:
    if col in new.columns:
        new.at[0, col] = int(temp_eth.loc[0, col])

temp_edu = pd.get_dummies(pd.DataFrame({'ParentalEducation':[ParentalEducation]}),
                          columns=['ParentalEducation'], drop_first=True)
for col in temp_edu.columns:
    if col in new.columns:
        new.at[0, col] = int(temp_edu.loc[0, col])

yesno = {
    "Tutoring": Tutoring,
    "ParentalSupport": ParentalSupport,
    "Extracurricular": Extracurricular,
    "Sports": Sports,
    "Music": Music,
    "Volunteering": Volunteering}

for col, val in yesno.items():
    dummy = f"{col}_1"
    if dummy in new.columns and val == "Yes":
        new.at[0, dummy] = 1

scaled_new = scaler.transform(new)
pred = model.predict(scaled_new)[0]

st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        box-shadow: 2px 2px 8px gray;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stButton>button {
        background-color: #1976d2; /* calm blue */
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: 500;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.15);
        transition: all 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #125ea8;  /* slightly darker blue */
        transform: translateY(-2px);  /* lift on hover */
        box-shadow: 0px 6px 12px rgba(0,0,0,0.25);  /* stronger shadow */
        cursor: pointer;
    }

    .stButton>button:active {
        transform: translateY(0px);  /* button goes back when clicked */
        box-shadow: 0px 3px 6px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)


if st.button("Predict"):
    st.subheader(pred)
    st.balloons()

if st.button("🔄 Convert GPA to 10-point system"):
    gpa_10 = pred * 10 / 4
    st.success(f"Converted GPA: {gpa_10:.2f} / 10")
