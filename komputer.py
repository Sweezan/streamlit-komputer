import pickle
import streamlit as st

model = pickle.load(open('komputer.sav','rb'))

st.title('Estimasi Harga Laptop')

ram = st.number_input('Input Ram Laptop')
rom = st.number_input('Input Rom Laptop')
display_size = st.number_input('Input Ukuran Display')

predict = ''

if st.button('Cek Estimasi Harga'):
    predict = model.predict(
        [[ram, rom, display_size]]
    )
    st.write ('Estimasi Harga Laptop Sesuai dengan Spec Dollar : ', predict)
    st.write ('Estimasi Harga Laptop Sesuai dengan Spec IDR : ', predict*16.366,7)
    