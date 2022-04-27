# %%
import pandas as pd
import streamlit as st

# %%
#df = pd.read_csv('/Users/arturfattahov/Desktop/users_2.csv', sep='|')

# %%
st.title("Количество созданных задач")
st.write("Количество созданных задач с разделением по ролям")
uploaded_file = st.file_uploader("Выбирете файл")


use_example_file = st.checkbox(
    "Использовать пример выгрузки", False, help="Будет использована старая выгрузка"
)


if use_example_file:
    uploaded_file = "users_2.csv"


if uploaded_file is not None:
     df = pd.read_csv(uploaded_file, sep='|')
     df.columns = ['id_user', 'id_task', 'platform', 'case']  
     file_container = st.expander("Check your uploaded .csv")   
     st.write(df)
     df = df.dropna()
     st.markdown("### Обзор выгрузки")
     st.dataframe(df.head())



st.info(
    f"""
     👆 Загрузите файл с расширением csv. В файле должны стого содержаться следующие столбцы:
         - id пользователя
         - id задачи
         - платформа
         - роль пользователя
         """
)

if not uploaded_file or not use_example_file:
        st.stop()

# %%
# df = df.dropna()
# df.columns = ['id_user', 'id_task', 'platform', 'case']

# %%
df = df.sort_values(by='id_user')

# %%
df_n = df.query('platform != [" admins   ", "          "] ')
df_provider = df.query('case == " provider" & platform != " admins   "')
df_executor = df.query('case == " executor" & platform != " admins   "')
df_users = df.query('platform != " admins   "')

# %%
# фильтры
# провайдеры, которые создали хотя бы одну задачу
creat_more_one_task_prov = df_n.query('case == " provider"').nunique()

# общее число провайдеров
all_provider = df_provider['id_user'].nunique()

# заказчики, которые создали хотя бы одну задачу
creat_more_one_task_exe = df_n.query('case == " executor"').nunique()

# общее число заказчиков
all_executor = df_executor['id_user'].nunique()

# пользователи, которые создали хотя бы одну задачу
creat_more_one_task = df_n['id_user'].nunique()

# общее количество пользователей
number_users = df_users['id_user'].nunique()

# %%
st.write('Количество провайдеров, которые создали хотя бы одну задачу:', creat_more_one_task_prov[0])

# %%
st.write('Количество заказчиков, которые создали хотя бы одну задачу:', creat_more_one_task_exe[0])

# %%
st.write('Процент провайдеров, которые создали хотя бы одну задачу:', creat_more_one_task_prov[0] * 100 / all_provider)

# %%
st.write('Процент заказчиков, которые создали хотя бы одну задачу:', creat_more_one_task_exe[0] * 100 / all_executor)

# %%
st.write('Процент пользователей, которые создали хотя бы одну задачу:', creat_more_one_task * 100 / number_users)


