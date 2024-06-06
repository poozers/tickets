import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title('CSV Viewer and Ticket Analysis')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write(df)

    # Optionally, display the DataFrame as a table
    st.dataframe(df)

    # Optionally, display some statistics
    st.write("Data Summary:")
    st.write(df.describe())

    # Assume the CSV has a 'time' column with date-time info and a 'ticket_id' or similar column
    if 'time' in df.columns and 'ticket_id' in df.columns:
        # Convert the 'time' column to datetime
        df['time'] = pd.to_datetime(df['time'])

        # Extract the hour from the time column
        df['hour'] = df['time'].dt.hour

        # Group by hour and count the number of tickets
        ticket_counts = df.groupby('hour').count()['ticket_id'].reset_index()
        ticket_counts.columns = ['hour', 'ticket_count']

        # Plot the number of tickets per hour using Plotly
        fig = px.bar(ticket_counts, x='hour', y='ticket_count', title='Number of Tickets per Hour', labels={'hour': 'Hour of the Day', 'ticket_count': 'Number of Tickets'})

        # Display the plot
        st.plotly_chart(fig)
    else:
        st.write("The CSV file must contain 'time' and 'ticket_id' columns.")
