import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# Load the data
df = pd.read_csv("/laptop_details_eda.csv")


# Define the features and target variables
X = df[['Rating', 'Brand Name', 'Ram_size', 'Ram_type', 'Operating system', 'Disk_type', 'Disk_size']]
y = df['MRP']

# Initialize a Random Forest Regressor with default parameters
rf_regressor = RandomForestRegressor(random_state=42)

# Fit the model to the entire dataset
rf_regressor.fit(X, y)

# Define a dictionary that maps brand names to numeric codes
brand_map = {'lenovo': 6, 'asus': 2, 'hp': 5, 'dell': 3, 'redmibook': 10, 'realme': 9, 'acer': 0,
             'msi': 7, 'vaio': 12, 'gigabyte': 4, 'nokia': 8, 'ultimus': 11, 'alienware': 1}
operating_map = {'windows 11 operating system': 1, 'windows 10 operating system': 0}
ram_type_map = {'ddr4': 0, 'ddr5': 1, 'lpddr5': 2, 'lpddr4': 3, 'lpddr3': 4}
disk_type_map = {'ssd': 1, 'hdd': 0}
disk_size_map = {'8 gb': 4, '16 gb': 1, '4 gb':3, '32 gb': 2, '128 gb': 0}
# Define a function to make predictions
def predict_price(rating, brand_name, ram_size, ram_type, operating_system, disk_type, disk_size):
    brand_code = brand_map[brand_name]  # get the numeric code for the selected brand
    operating_code = operating_map[operating_system]
    ram_type_code = ram_type_map[ram_type]
    disk_type_code = disk_type_map[disk_type]
    disk_size_code = disk_size_map[disk_size]
    x_input = pd.DataFrame({'Rating': [rating], 'Brand Name': [brand_code], 'Ram_size': [ram_size], 
                            'Ram_type': [ram_type_code], 'Operating system': [operating_code], 'Disk_type': [disk_type_code], 
                            'Disk_size': [disk_size_code]})
    return rf_regressor.predict(x_input)[0]



# Create a Streamlit app
def main():
    
    st.title("Laptop Price Predictor")
    
    # define the brand names array
    brands = ['lenovo', 'asus', 'hp', 'dell', 'redmibook', 'realme', 'acer','msi', 'vaio', 'gigabyte', 'nokia', 'ultimus', 'alienware']
    ram_size = [4,8,16,32,64,128]
    disks = ['8 gb', '16 gb', '4 gb', '32 gb', '128 gb']
    operatings = ['windows 11 operating system', 'windows 10 operating system']
    # Create input fields for the features
    rating = st.slider("Rating", min_value=1.0, max_value=5.0, step=0.1)
    

    brand_name = st.selectbox('Brand Name', ['Select a Brand Name'] + brands)
    ram_size = st.selectbox('RAM Size', ['Select a Ram Size'] + ram_size)
    ram_type = st.selectbox("RAM Type", ['Select a RAM Type'] + list(ram_type_map.keys()))
    operating_system = st.selectbox('Operating System', ['Select an Operating System'] + operatings)
    disk_type = st.selectbox("Disk Type", ['Select a Disk Type'] + list(disk_type_map.keys()))
    disk_size = st.selectbox('Disk Size', ['Select a Disk Size'] + disks)


    if st.button("Predict Price"):
        # Make a prediction using the input values
        predicted_price = predict_price(rating, brand_name, ram_size, ram_type, operating_system, disk_type, disk_size)

        # Show the predicted price to the user
        st.subheader(f"Predicted Price: ${predicted_price:.2f}")

if __name__ == '__main__':
    main()
    
