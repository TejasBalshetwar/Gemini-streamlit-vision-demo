# Gemini-streamlit-vision-demo 

This Python script demonstrates the integration of Google's Gemini API with Streamlit to generate textual content based on a provided prompt and an uploaded image.

## Setup and Usage
1. Clone the repository.
2. Install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up a `.env` file containing necessary environment variables, including the Google API key (`GOOGLE_API_KEY`).
4. Run the application:
    ```bash
    streamlit run script_name.py
    ```
5. Input text in the designated field and upload an image (JPG, JPEG, or PNG).
6. Click the "Tell me about the image" button to generate content based on the provided text and image.

## Code Structure
- `script_name.py` contains the code for the Gemini application.
- `requirements.txt` lists the required Python packages and versions.
- The `get_gemini_response()` function uses the Gemini API to generate content.
- `input_image_setup()` processes the uploaded image for Gemini API usage.
- The Streamlit interface prompts users for text input and image upload.

Feel free to explore and modify the code as needed!
