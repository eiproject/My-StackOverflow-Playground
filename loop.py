# def getCols(x_):
#     max_i = 6
#     max_j = 13
#     out = []
#     for i in range(1, max_i):
#         for j in range(1, max_j):
#             if j < max_j - 1:
#                 out.append((f'{x_}_{str(i).zfill(2)}_{str(j).zfill(2)}', f'{x_}_{str(i).zfill(2)}_{str(j+1).zfill(2)}'))
    
#     return out

# def getCols(x_):
#     max_i = 6
#     max_j = 13
#     return [(f'{x_}_{str(i).zfill(2)}_{str(j).zfill(2)}', f'{x_}_{str(i).zfill(2)}_{str(j+1).zfill(2)}') for i in range(1, max_i) for j in range(1, max_j) if j < max_j - 1]
# a = getCols('abc')
# print(a)

# def something(st, col2, choosen_menu, dir_path, reader_path):
#     st.title('Query Answering AI Bot')
#     query = st.text_input("Enter Text: ")

#     with col2:
#         menu = [choosen_menu,'ASHRAE']

#     choice = st.sidebar.selectbox("Choose Form",options = menu)
#     n_predictions = st.sidebar.slider(label="Number Of Predictions", min_value=1, max_value=10)

#     if choice == choosen_menu:
#         if query:
#             df = pdf_converter(directory_path=dir_path)
#             cdqa_pipeline = QAPipeline(reader=reader_path, max_df=1.0).fit_retriever(df=df)
#             prediction = cdqa_pipeline.predict(query, n_predictions=n_predictions)
#             for i, value in enumerate(prediction):
#                 answer, title, paragraph, predictionsss = value
                
#                 answer_var=st.write(answer)

# something(st, 
#     col2, 
#     choosen_menu='DEWA REGULATIONS FOR  ELECTRICAL INSTALLATIONS',
#     dir_path='./dewa/',
#     reader_path='bert_qa.joblib')

deposit = 10000
deposit_list  = []
year = 0
while deposit <= 700000:
    deposit = (deposit * pow((7.1 / 100 + 1), year))
    deposit_list.append([deposit, pow((7.1 / 100 + 1), year)])
    year += 1

print((year - 1), deposit_list)