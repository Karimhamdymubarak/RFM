import pandas as pd
import streamlit as st
import sklearn

df = pd.read_csv("Clustereddata.csv")

def get_recommendations(user , dataframe , num_of_recom):
    try:
        cluster = dataframe[dataframe["CustomerID"] == int(user)]["Cluster"].unique()[0]
        df_cluster = dataframe[dataframe["Cluster"] == cluster]
        df_cluster = df_cluster.groupby("MerchantName")["TransactionValue"].sum().nlargest(num_of_recom)
        for index , mer in enumerate(df_cluster.index) :
            st.text(f"Recommmended Merchant Number {index + 1 } for User {user} is {mer}")
    except:
        st.text(f"The User {user} is not exist on the dataset")

def main():
    st.title("Smart RFM Recommendations")
    user = st.text_input(label="UserID")
    num_of_recom = st.selectbox("num_of_recom" , list(range(1,11)) )
    if st.button("Recommend"):
        get_recommendations(user, df , num_of_recom)
main()
    
