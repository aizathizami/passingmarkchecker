import streamlit as st
y = 50
st.header("Mark Checking Demo")


readme = st.checkbox("readme")

if readme:

    st.write("""
        This is a mark checking demo. You may get the codes via [github](https://github.com/aizathizami/passingmarkchecker.git)
        """)

    st.write ("For more info, please contact:")

    st.write("<a href='https://www.linkedin.com/in/aizat-hizami-b57345b9/'>Aizat Hizami </a>", unsafe_allow_html=True)
    

st.write("Please enter your mark. To stop the algorithm, enter x .\n\n")
         
mark = st.text_input('Enter the mark here', '50')
         
         
try:
    val = float(mark)
            
    if (val > 100 or val < 0):
        st.write("\nPlease enter a valid mark.\n")
                
    elif val >= y:
        st.write("\nYou passed your exam. Keep it up!\n")
       
    else:
        st.write("\nUnfortunately, you did not pass your exam. Work harder. You can make it.\n")

            
except ValueError:
    st.write("\nPlease enter a number.\n")
