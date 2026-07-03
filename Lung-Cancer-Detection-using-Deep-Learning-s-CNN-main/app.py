import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your model
model_path = 'lungs_cancer_detector_simple_CNN.h5'
loaded_model = tf.keras.models.load_model(model_path)

# Define the Streamlit app
def main():
    st.title("X-ray Classifier for Lung Cancer")

    # Upload image
    uploaded_file = st.file_uploader("Upload an X-ray image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        # st.image(uploaded_file, caption='Uploaded X-ray Image', use_column_width=True)

        # Button to make a prediction
        if st.button("Make Prediction"):
            # Preprocess the image
            img = image.load_img(uploaded_file, target_size=(250, 250))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = img / 255.0  # Normalize the image (adjust this if needed)

            # Use your model to make predictions
            prediction = loaded_model.predict(img)

            # Define a threshold for classification (adjust as needed)
            threshold = 0.5

            # Display the prediction result
            if prediction >= threshold:
                st.error("Lung Cancer Detected")
            else:
                st.success("Normal")
        st.image(uploaded_file, caption='Uploaded X-ray Image', use_column_width=True)


if __name__ == "__main__":
    main()
