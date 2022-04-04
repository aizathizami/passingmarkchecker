import pandas as pd
import streamlit as st


st.title('Passing Mark Checker')

st.sidebar.write("""
A demo of passing mark checker algorithm
""")

st.sidebar.write ("For more info, please contact:")

st.sidebar.write("<a href='https://www.linkedin.com/in/aizat-hizami-b57345b9/'>Aizat Hizami </a>", unsafe_allow_html=True)


y = 50 # minimum passing score

while True:
    x = input("Please enter your mark. To stop the algorithm, enter x .\n\n")

    if x== "x":
      print ("\nThank you for using our service.\n")
      break
      
    else:
        try:
          val = int(x)
          
          if (val > 100 or val < 0):
            print("\nPlease enter a valid mark.\n")
                
    elif val >= y:
                  print("\nYou passed your exam. Keep it up!\n")
                
                else:
                  print("\nUnfortunately, you did not pass your exam. Work harder. You can make it.\n")
                  
        except ValueError:
        print("\nPlease enter a number.\n")
