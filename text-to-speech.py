import tkinter as tk
import pyttsx3

# Function to convert text to speech
def convert_to_speech():
    text = text_entry.get("1.0", "end-1c")  # Get the text from the text box
    if text.strip():  # Ensure the text is not empty
        engine = pyttsx3.init()  # Initialize the TTS engine
        
        # Set properties for speech rate and volume
        rate = engine.getProperty('rate')  # Get the current speech rate
        engine.setProperty('rate', rate - 50)  # Set rate (default is 200)
        volume = engine.getProperty('volume')  # Get the current volume level
        engine.setProperty('volume', volume + 0.2)  # Increase volume (default is 1.0)
        
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
    else:
        # If no text is entered
        error_label.config(text="Please enter some text.")

# Create the GUI
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create and place the label for the instructions
label = tk.Label(root, text="Enter the text you want to convert to speech:")
label.pack(pady=10)

# Create and place the text box for user input
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create and place the button to trigger speech conversion
convert_button = tk.Button(root, text="Convert to Speech", command=convert_to_speech)
convert_button.pack(pady=10)

# Create and place an error label (if any)
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
