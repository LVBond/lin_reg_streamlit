import numpy as np 
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn.linear_model import LinearRegression

st.title('Градиентный спуск')

# Пример вывода текста и данных
st.write('Приложение Streamlit для визуализации градиентного спуска с выбором learning rate ')




def loss(w):
    
    return w ** 2 + 3