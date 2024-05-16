import numpy as np 
import pandas as pd
import streamlit as st
import seaborn as sns
from sklearn.linear_model import LinearRegression


# Заголовок вашего веб-приложения
st.title('Линейная регрессия')

# Пример вывода текста и данных
st.write('Приложение Streamlit для визуализации линейной регрессии по заданным x и y')

# загрузчик для датафрейма
appload_file = st.file_uploader('Загрузка данных', type=['csv'])

#

if appload_file is not None:
    df = pd.read_csv(appload_file)

    if df is not None:
        # здесь весь код
        # кнопки выбора где икс и где игрек
        columns = list(df.columns)

        # дать выбор только из числовых колонок
        numerical_columns = df.select_dtypes(include=[np.number]).columns
        x_column = st.selectbox('Выберите переменную x', numerical_columns)
        y_column = st.selectbox('Выберите переменную y', numerical_columns)


        # построим линейную регрессию
        X = df[[x_column]]
        Y = df[y_column]


        model_lr = LinearRegression().fit(X, Y)

        # выведем на экран параментры модели 
        w_0 = model_lr.intercept_
        w_1 = model_lr.coef_

        st.write(f'Коэффициент пересечения {round(w_0, 3)}, коэф наклона {round(w_1[0], 3)}')

        # нарисовать график x от y 
        st.set_option('deprecation.showPyplotGlobalUse', False)
        sns.regplot(data=df, x=x_column, y=y_column, order=1)
        st.pyplot()



