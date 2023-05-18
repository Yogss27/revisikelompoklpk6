import streamlit as st
import math




def calculate_pH(ion_concentration):
    pH = -1 *(math.log10(ion_concentration))
    return pH

def main():
    st.title("Simple pH Meter")

    st.write("Masukkan konsentrasi ion (dalam mol/Liter):")
    ion_concentration = st.number_input("",min_value=0.0, format="%.4f")

    if st.button("Hitung pH"):
        pH = calculate_pH(ion_concentration)
        st.write(f"pH dari larutan dengan konsentrasi ion {ion_concentration} mol/L adalah {pH:.2f}")

        if pH<7:
            st.write("Larutan termasuk dalam asam")
        elif pH>7:
            st.write("Larutan termasuk dalam basa")
        else:
            st.write("Larutan bersufat netral")

if __name__ == "__main__":
    main()


import streamlit as st


st.subheader('Penjelasan Molaritas')
st.caption('molaritas adalah konsentrasi jumlah zat terlarut per satuan volume. Molaritas menunjukan berapa banyak mol zat terlarut dalam satu liter zat pelarut (mol/liter). Pada umumnya jumlah zat pelarut akan lebih besar disbanding jumlah zat terlarut.')
st.caption('ion hidrogen adalah atom hidrogen yang memiliki nomor yang berbeda dari elektron daripada normal. Bermuatan positif ion hidrogen disebut kation, dan negatif disebut anion.')

st.subheader('keterangan')
st.caption('0 - 7 larutan termasuk dalam asam') 
st.caption('7 larutan bersifat netral')
st.caption('7 - 14 larutan termasuk dalam basa')