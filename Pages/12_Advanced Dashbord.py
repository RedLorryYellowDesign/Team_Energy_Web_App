import streamlit as st
import numpy as np
import pandas as pd
with st.container():
    st.empty()



df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
