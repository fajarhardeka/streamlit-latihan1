#Import Library yang digunakan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Belajar Analisis Data <<< ini title')
st.header("Pengembangan Dasboard <<< ini header")
st.subheader("Explanatory Data Analytics <<< subheader")


st.markdown(
     """
    # Markdown() <<< ini markdown
    Hello, para calon praktisi data masa depan! anjayyyy :sunglasses: <<< ini juga bagian markdown
     """   
)

st.subheader(
   'penggunaan untuk menunjukan kode'
)
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.subheader('Penggunaan streamlit untuk mathematical expression: ')
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
st.latex(r"""\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
""")
st.latex(r"""\def\arraystretch{1.5}
   \begin{array}{c:c:c}
   a & b & c \\ \hline
   d & e & f \\
   \hdashline
   g & h & i
\end{array}
""")

st.subheader(
   'dataframe()'  
)
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.dataframe(data=df, width=500, height=150)

st.subheader(
   'table()'  
)
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.subheader(
   'metric()'
)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")     

st.subheader(
   'Json()'
)
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.subheader(
   'Chart, pyplot()'
)
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)



st.caption('Copyright (c) 2023 <<< ini caption')


