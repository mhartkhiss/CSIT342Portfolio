import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps

# Set page configuration
st.set_page_config(page_title="My Portfolio", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Portfolio", "Contact"]
selection = st.sidebar.radio("Go to", pages)

# Home Page
if selection == "Home":
    st.title("Welcome to My Portfolio!")
    st.write("Hello! I'm Mhart Khiss Degollacion, a BSIT student in CIT-U. This is a brief showcase of my skills, and experience as student.")

# About Me Page
elif selection == "About Me":

    st.title("About Me")
    
    # Open the image
    image = Image.open("mkz.png")
    
    # Resize the image
    image = image.resize((150, 150))
    
    # Create a circular mask
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)
    
    # Apply the mask to the image
    circular_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    
    # Display the image
    st.image(circular_image, caption="Mhart Khiss Degollacion", use_column_width=False)
    
    st.subheader("Biography")
    st.write("I'm Mhart Khiss Degollacion, born in Cebu City. I'm currently studying in Cebu Institute of Technology - University, taking up Bachelor of Science in Information Technology. I'm a passionate student who loves to learn new things, explore new technologies, and solve problems.")
    st.subheader("Interests")
    st.write("I love watching Anime. I also enjoy playing video games, reading books (sometimes), and coding.")

# Portfolio Page
elif selection == "Portfolio":
    st.title("Portfolio")
    st.subheader("Projects")
    
    st.write("### Project 1: SpeakForge")
    st.write("SpeakForge is a mobile application that aims to help people with speech difficulties to communicate with others. The app converts text to speech and vice versa. It also has a feature that allows users to save their conversations. This was our project in AppDev subject.")
    st.markdown("https://github.com/mhartkhiss/SpeakForge-AppDev-")
    
    st.write("### Project 2: Chatify")
    st.write("Chatify was my project in Mobile App Development subject. It is a chat application that allows users to send messages to each other. It has a built-in translator that translates messages to the user's preferred language.")
    st.markdown("https://github.com/mhartkhiss/Chatify")

# Contact Page
elif selection == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me through the following channels:")
    st.write("- Email: makizz999@gmail.com")
    st.write("- Facebook: fb.com/makizz09")
    st.write("- GitHub: https://github.com/mhartkhiss")
