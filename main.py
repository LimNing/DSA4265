# main
import pickle
import streamlit as st
 
# loading the trained model
# pickle_in = open('classifier.pkl', 'rb') 
# classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <style>
      .stApp {
        background: #0d2233;
      }
      td {
        text-align: center;
      }
    </style>
    <div style ="padding:13px"> 
    <h1 style ="color:lightgrey;text-align:center;">Ship Emission Efficiency</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    TechnicalEfficiency = st.number_input("Technical Efficiency")
    CO2Between = st.number_input("CO₂ emissions from all voyages between ports under a MS jurisdiction [m tonnes]")
    CO2Depart = st.number_input("CO₂ emissions from all voyages which departed from ports under a MS jurisdiction [m tonnes]") 
    CO2To = st.number_input("CO₂ emissions from all voyages to ports under a MS jurisdiction [m tonnes]")
    CO2Within = st.number_input("CO₂ emissions which occurred within ports under a MS jurisdiction at berth [m tonnes]")
    TimeSea = st.number_input("Annual Total time spent at sea [hours]")
    CO2Dist = st.number_input("Annual average CO₂ emissions per distance [kg CO₂ / n mile]")
    CO2Transport = st.number_input("Annual average CO₂ emissions per transport work (mass) [g CO₂ / m tonnes · n miles]")
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        # result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)

    html_temp2 = """ 
    <table style="margin-left:auto; margin-right:auto;">
      <tr>
        <th>Group</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>A</td>
        <td></td>
      </tr>
      <tr>
        <td>B</td>
        <td></td>
      </tr>
      <tr>
        <td>C</td>
        <td></td>
      </tr>
      <tr>
        <td>D</td>
        <td></td>
      </tr>
      <tr>
        <td>X</td>
        <td></td>
      </tr>
    </table>
    """
      
    # display the front end aspect
    st.markdown(html_temp2, unsafe_allow_html = True) 
     
if __name__=='__main__': 
    main()