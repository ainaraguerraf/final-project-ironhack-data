import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_excel("data_final_encoded.xlsx")

# Reverse dictionaries for decoding
user_age_decoded = {0: 'young', 1: 'adult', 2: 'old'}
user_way_decoded = {0: 'alone', 1: 'in couple', 2: 'in group', 3: 'in family'}
sentiment_decoded = {0: 'artsy', 1: 'adventurous', 2: 'relax', 3: 'curious', 4: 'history freak'}
destination_decoded = {1: "Madrid", 2: "Vigo", 3: "La Palma", 4: "Euskadi", 5: "Barcelona"}
cat_sites_decoded = {
    1: 'historic building, museums and archaeological rests',
    2: 'town, parks or lookouts',
    3: 'points of interest, like squares and sculptures',
    4: 'experiences, cultural centers, theaters and music',
    5: 'religious',
    6: 'contemporary buildings and art galleries',
    7: 'route and urban routes',
    8: 'food, music, seaside, sport and others'
}

# Prepare data for model training
X_content = df[["age_encoded", "way_encoded", "sentiment_encoded", "destination_encoded", "rating"]]
y_content = df["cat_sites_reduced_encoded"]

# Train test split
X_train_content, X_test_content, y_train_content, y_test_content = train_test_split(
    X_content, y_content, test_size=0.2, random_state=42
)

# Initialize the model
rf_content = RandomForestClassifier(n_estimators=100, random_state=42)

# Model training
rf_content.fit(X_train_content, y_train_content)

# Streamlit app
def main():
    # add background image
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )

    add_bg_from_local('5.png')

    # Custom CSS styles for title and click effect
    custom_css = """
    <style>
    /* Set title color to pink */
    .title-wrapper {
        color: pink;
    }

    /* Set click effect color to light green */
    .css-1g8ra89:hover {
        background-color: lightgreen !important;
        color: black !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    new_title = '<p style= color:Grey; font-size: 280px;"> Project by Nara Guerra 👽</p>'
    st.markdown(new_title, unsafe_allow_html=True)


    st.title("Find the :pink[best places] with this personalised browser")

    st.markdown("Enter your preferences to get the site category you can't missed in Spain and top places to visit.")

    # User input form
    with st.form(key='site_recommender_form'):
        user_sentiment_input = st.selectbox("Select your mood for this travel:", [""] + list(sentiment_decoded.values()))
        user_age_input = st.selectbox("Select your age group:", [""] + list(user_age_decoded.values()))
        user_way_input = st.selectbox("Select your way of travel:", [""] + list(user_way_decoded.values()))
        user_destination_input = st.selectbox("Select your destination in Spain:", [""] + list(destination_decoded.values()))
        user_rating_input = st.slider("Rate for this experience (1-5):", 1, 5, 3)
        submit_button = st.form_submit_button(label='Get Recommendations')

    # Perform predictions and show the results when the form is submitted
    if submit_button:
        # Convert user inputs to encoded values
        user_age_encoded = list(user_age_decoded.keys())[list(user_age_decoded.values()).index(user_age_input)]
        user_way_encoded = list(user_way_decoded.keys())[list(user_way_decoded.values()).index(user_way_input)]
        user_sentiment_encoded = list(sentiment_decoded.keys())[list(sentiment_decoded.values()).index(user_sentiment_input)]
        user_destination_encoded = list(destination_decoded.keys())[list(destination_decoded.values()).index(user_destination_input)]

        # Make the prediction using the model
        user_category_encoded = rf_content.predict([[user_age_encoded, user_way_encoded, user_sentiment_encoded, user_destination_encoded, user_rating_input]])[0]
        user_category = cat_sites_decoded[user_category_encoded]

        # Display results at the bottom of the page
        st.markdown("## Results")
        st.write("#### Category more adequate to you:", user_category)

        # Get top three sites to visit
        top_sites_names = get_top_three_sites_by_category(df, user_category_encoded, user_destination_encoded)
        st.markdown("## Places you shouldn't miss:")
        for idx, site_name in enumerate(top_sites_names):
            st.write(f"{idx+1}. {site_name}")

        # Display sites on a map
        st.subheader("Map of these sites")
        map_data = df[df['name'].isin(top_sites_names)][['latitud', 'longitud', 'name']]
        map_data.rename(columns={'latitud': 'LAT', 'longitud': 'LON'}, inplace=True)
        st.map(map_data)

def get_top_three_sites_by_category(df, user_category_encoded, user_destination_encoded):
    # Filter sites of this category and destination
    category_sites = df[(df['cat_sites_reduced_encoded'] == user_category_encoded) & (df['destination_encoded'] == user_destination_encoded)]

    # Sort the sites by the column "rating" in descending order
    sorted_sites = category_sites.sort_values(by='rating', ascending=False)

    # Take the top three sites with the highest ratings and get only the "name" column
    top_three_sites = sorted_sites.head(3)['name']

    return top_three_sites.tolist()

if __name__ == "__main__":
    main()

# This app was put together with the inconditional help of Streamlit documentation, Streamlit topics where users can ask questions that are answered by thi community and Chat GPT.