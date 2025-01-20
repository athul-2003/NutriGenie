from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
import requests
import re


# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-1.5-flash")
# model2 = genai.GenerativeModel("gemini-pro")


def get_gemini_response(prompt, input_prompt, image):
    """Generate content using the Gemini model."""
    try:
        if input_prompt:
            response = model.generate_content([prompt, input_prompt, image])
        else:
            response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    
def get_food_title(food_title_prompt, image):
    response_title = model.generate_content([food_title_prompt,image])
    return response_title.text

# Function for cleaning the recipe text


food_nutri_propmt="""Act as an experienced dietitians or qualified nutritionists and give the nutritional information of this food image and its recipe in the below format:

* Total Calories: 
* Total Fat:
* Total Carbohydrates:
* Total Protein:
* Total Fiber:
* Total Sugar:
* Total Sodium:
* Total Potassium:
* Total Calcium:
* Total Iron:
and any other relevant nutritional information that is present in the food recipe.

Also do an analysis and provide the health benefits of the food recipe and the health risks of the food recipe if any.



"""
# Function for generating nutritional information
def get_nutritional_info(recipe_text,image):
    response_nutrition = model.generate_content([food_nutri_propmt,recipe_text, image])
    return response_nutrition.text
        



def main():
    """Main function to run the Streamlit app."""

    # Initialize Streamlit app
    st.set_page_config(page_title="Gemini Application", page_icon="🌟")
    st.title("🥗 NutriGenie: 🍲")
    # st.subheader("-Recipe & Nutrition Wizard")
    st.markdown("<h5 style='text-align: center; color: lightgreen;'>-Recipe & Nutrition Wizard-</h5>", unsafe_allow_html=True)

    st.markdown("\n")

    # User input
    input_prompt = st.text_area("✨ Enter your Prompt:", key="input", help="e.g., 'What is the main ingredient in this food?'")

    prompt = "Act as an experienced Chef and generate the recipe and the ingredients used in the given food image"

    uploaded_file = st.file_uploader("📸 Upload an image of the food...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Food Image.', use_column_width=True)

    # Submit button
    if st.button("Generate Recipe 🤖"):
        if image is None:
            st.error("Please upload an image of the food to generate the recipe.")
        else:
            with st.spinner("Generating the recipe..."):
                # Generate recipe
                response_text = get_gemini_response(prompt, input_prompt, image)
                food_title_prompt="You are a food namer and you have to name the food in the image,I just want the name of the food in the image"
                food_title = get_food_title(food_title_prompt,image)
                # Display the response text
                if response_text is not None:
                    st.subheader(f"Generated Recipe for {food_title}:")
                    st.write(response_text)

                    # Positive feedback
                    st.success("Recipe successfully generated!")

                    # Retrieve nutritional information
                    st.sidebar.write("📊Insights on the Nutritional Information of the Food Recipe🍽️")
                    nutri_info=get_nutritional_info(response_text,image)
                    st.sidebar.write(nutri_info)
                
if __name__ == "__main__":
    main()
