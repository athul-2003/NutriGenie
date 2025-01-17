# 🥗 NutriGenie: Recipe & Nutrition Wizard 🍲

## Overview
**NutriGenie** is an AI-powered Streamlit application that uses Google's Gemini model to provide comprehensive recipes, nutritional information, and health insights based on uploaded food images. The app is designed to assist chefs, nutritionists, and food enthusiasts by simplifying recipe generation and offering detailed nutritional analysis.

## Features
- **Food Image Recognition:** Upload an image of a food item to get a tailored recipe.
- **Recipe Generation:** Generates a recipe along with the list of ingredients.
- **Nutritional Insights:** Provides detailed nutritional information such as calories, fat, protein, carbohydrates, and more.
- **Health Analysis:** Offers health benefits and risks of the food recipe.
- **Custom Queries:** Allows users to ask specific questions about the food item.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/athul-2003/NutriGenie.git
   cd NutriGenie
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirement.txt
   ```
3. Set up the environment variable for the Gemini API key:
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```
     GOOGLE_API_KEY=your_gemini_api_key
     ```

## Usage
1. Run the application:
   ```bash
   streamlit run Nutri-app.py
   ```
2. Open the app in your browser using the URL provided by Streamlit (default: `http://localhost:8501`).
3. Upload an image of food and let NutriGenie work its magic!

## How It Works
1. **Image Upload:** Users upload a food image through the interface.
2. **Recipe Generation:** The app uses the Gemini model to generate a recipe based on the image and user input.
3. **Nutritional Analysis:** Nutritional details and health insights are provided for the generated recipe.
4. **Custom Queries:** Users can ask specific questions about the food item for additional insights.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web app framework.
- **Google Gemini API**: Used for generative AI capabilities.
- **Pillow (PIL)**: Image processing.
- **dotenv**: For managing environment variables.

## File Structure
```
Nutrigenie/
├── Nutri-app.py               # Main application file
├── requirement.txt     # Python dependencies
├── .env                 # Environment variables (not included in repo)
└── README.md            # Project documentation
```

## Example Workflow
1. Upload an image of a food item (e.g., a salad).
2. Get the name of the dish and a detailed recipe.
3. View the nutritional breakdown in the sidebar.
4. Explore the health benefits and risks of the food recipe.

## Demo
[**Watch Demo Video**](https://github.com/user-attachments/assets/26be7f84-f750-478a-92f1-5ca7bd51136d)  

## Disclaimer
It's difficult to give precise nutritional information for any dish without knowing the exact weight of each ingredient used. The nutritional content will vary considerably depending on portion sizes and the specific types and amounts of ingredients included. The nutritional insights provided by NutriGenie are approximations and should not be considered precise analyses. To get exact values, one would need to measure and weigh each ingredient precisely and then use a nutrition analysis tool.

## Future Enhancements
- **Language Support:** Extend the app to support multiple languages.
- **Diet Customization:** Allow users to specify dietary restrictions (e.g., vegan, gluten-free).
- **Integration:** Connect with external APIs for more detailed nutritional data.
- **Mobile Compatibility:** Optimize for mobile devices.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue to discuss your ideas first.

## Acknowledgments
- Google Gemini API for enabling AI-powered recipe generation.
- Streamlit for providing an intuitive platform for building web applications.

---

⭐️ Don't forget to give this repo a star if you found it helpful!
