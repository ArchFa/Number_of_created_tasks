# %%
import pandas as pd
import streamlit as st

# %%
#df = pd.read_csv('/Users/arturfattahov/Desktop/users_2.csv', sep='|')

# %%
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     df = pd.read_csv(uploaded_file, sep='|')
     df = df.dropna()
     df.columns = ['id_user', 'id_task', 'platform', 'case']  
     file_container = st.expander("Check your uploaded .csv")   
     st.write(df)
else:
    st.info(
        f"""
             👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
             """
    )

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
# print('Количество провайдеров, которые создали хотя бы одну задачу:', creat_more_one_task_prov[0])
# print('Количество заказчиков, которые создали хотя бы одну задачу:', creat_more_one_task_exe[0])



# display('Процент провайдеров, которые создали хотя бы одну задачу: {:.0f}%'
#         .format(creat_more_one_task_prov[0] * 100 / all_provider))

# display('Процент заказчиков, которые создали хотя бы одну задачу: {:.0f}%'
#         .format(creat_more_one_task_exe[0] * 100 / all_executor))

# display('Процент пользователей, которые создали хотя бы одну задачу: {:.0f}%'
#         .format(creat_more_one_task * 100 / number_users))

# %%
tt = creat_more_one_task_prov[0] * 100 / all_provider
mm = creat_more_one_task_exe[0] * 100 / all_executor
ii = creat_more_one_task * 100 / number_users

# %%
st.write('Количество провайдеров, которые создали хотя бы одну задачу:', creat_more_one_task_prov[0])

# %%
st.write('Количество заказчиков, которые создали хотя бы одну задачу:', creat_more_one_task_exe[0])

# %%
st.write('Процент провайдеров, которые создали хотя бы одну задачу:', tt)

# %%
st.write('Процент заказчиков, которые создали хотя бы одну задачу:', mm)

# %%
st.write('Процент пользователей, которые создали хотя бы одну задачу:', ii)


