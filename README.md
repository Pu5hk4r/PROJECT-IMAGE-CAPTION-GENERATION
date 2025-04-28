# 🖼️ PROJECT: IMAGE CAPTION GENERATOR
![screenshot1](https://github.com/Pu5hk4r/PROJECT-IMAGE-CAPTION-GENERATION/blob/main/imageCaption.png)
![screenshot2](https://github.com/Pu5hk4r/PROJECT-IMAGE-CAPTION-GENERATION/blob/main/hjhpng.png)

This project uses the **Florence-2 transformer model** to generate captions for uploaded images. With an intuitive **Gradio** web interface, users can upload images and receive contextually accurate captions in real time.

---

## ✨ Features

- 🔥 **Pre-trained Transformer Model**: Leverages the power of Florence-2 for robust caption generation.
- 🖥️ **Interactive Web Interface**: Built with Gradio for easy interaction and seamless image uploads.
- ⚡ **Optimized Performance**: Utilizes Flash Attention and CUDA for faster processing.
- 🛠️ **End-to-End Workflow**: From image preprocessing to caption generation, all steps are automated.

---

## 🛠️ Tech Stack

### 🧩 Languages and Frameworks
- 🐍 Python
- 🔥 PyTorch

### 📚 Libraries
- 🖼️ **Gradio**: For building the web interface.
- 🤗 **Hugging Face Transformers**: For loading and utilizing the pre-trained Florence-2 model.
- 🖌️ **PIL (Python Imaging Library)**: For image preprocessing.
- 🚀 **CUDA**: For GPU-accelerated computations.
- ⚡ **Flash Attention**: For faster transformer attention calculations.

---

## 🔥 Project Workflow

1. 🖼️ **Image Preprocessing**  
   - Images are uploaded via the web interface.  
   - Converted to a compatible format using **PIL**.

2. 🧠 **Model Loading**  
   - The Florence-2 pre-trained transformer is loaded.  
   - Used for feature extraction and text generation.

3. 📝 **Caption Generation**  
   - Captions are generated based on the visual and contextual features of the image.

4. 📋 **Output Display**  
   - The generated caption is displayed to the user via the **Gradio interface**.

---

