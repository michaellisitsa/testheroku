from math import sqrt
#from handcalcs import handcalc
import handcalcs
import streamlit as st

@handcalcs.handcalc(override="long",jupyter_display=False)
def quadratic(a,b,c):
    x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return locals()

a = st.slider("Value for a:", 1,5, 5)
b = st.slider("Value for b:", -10, 10, -5)
c = st.slider("Value for c:", -20,0, -5)

st.write("Quadratic equation in x:")
st.latex(f"{a}x^2 + {b}x + {c} = 0")

vals = quadratic(a,b,c)
#latex_code, vals = quadratic(a,b,c)
st.latex(vals[0])
st.write("Vals from returned dict:")
#st.write(vals[0])
st.write("x_1:", vals[1]["x_1"], "x_2:", vals[1]["x_2"])