import gradio as gr
import subprocess
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM

# Install the flash-attn package with specific options
subprocess.run(
    'pip install flash-attn --no-build-isolation',
    env={'FLASH_ATTENTION_SKIP_CUDA_BUILD': "TRUE"},
    shell=True
)

# Initialize Florence model
device = "cuda" if torch.cuda.is_available() else "cpu"
florence_model = AutoModelForCausalLM.from_pretrained(
    'microsoft/Florence-2-base',
    trust_remote_code=True
).to(device).eval()
florence_processor = AutoProcessor.from_pretrained(
    'microsoft/Florence-2-base',
    trust_remote_code=True
)

# Define a function to generate a caption for the input image
def generate_caption(image):
    # Ensure the input is a PIL Image
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    # Process the input image and text
    inputs = florence_processor(
        text="<MORE_DETAILED_CAPTION>",
        images=image,
        return_tensors="pt"
    ).to(device)

    # Generate text using the model
    generated_ids = florence_model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        early_stopping=False,
        do_sample=False,
        num_beams=3,
    )
    
    # Decode the generated text
    generated_text = florence_processor.batch_decode(
        generated_ids,
        skip_special_tokens=True  # Changed to True to avoid special tokens
    )[0]

    # Post-process the generated text
    parsed_answer = florence_processor.post_process_generation(
        generated_text,
        task="<MORE_DETAILED_CAPTION>",
        image_size=(image.width, image.height)
    )
    
    prompt = parsed_answer["<MORE_DETAILED_CAPTION>"]  # Extract the caption
    print("\n\nGeneration completed!: " + prompt)
    return prompt

# # Create Gradio interface
# io = gr.Interface(
#     fn=generate_caption,  # Function to call
#     inputs=[gr.Image(label="Input Image")],  # Input type
#     outputs=[
#         gr.Textbox(label="Output Prompt", lines=2, show_copy_button=True)
#         # Optionally, you can uncomment the next line to show generated images if needed
#         # gr.Image(label="Output Image")
#     ]
# )

# # Launch the Gradio interface
# io.launch(debug=True)

# Create Gradio interface
# io = gr.Interface(
#     fn=generate_caption,  # Function to call
#     inputs=[gr.Image(label="Input Image")],  # Input type
#     outputs=[
#         gr.Textbox(label="Output Prompt", lines=2, show_copy_button=True)
#         # Optionally, uncomment the next line to show generated images if needed
#          gr.Image(label="Output Image")
#     ],
#     title="Image Caption Generator - Owner: Pushkar Sharma"  # Add owner name here
# )

io = gr.Interface(
    fn=generate_caption,  # Function to call
    inputs=[gr.Image(label="Input Image")],  # Input type
    outputs=[
        gr.Textbox(label="Output Prompt", lines=2, show_copy_button=True),  # Added comma here
        #gr.Image(label="Output Image")
    ],
    title="Image Caption Generator - Owner: Pushkar Sharma"  # Add owner name here
)


# Launch the Gradio interface with public access
io.launch(debug=True, share=True)
