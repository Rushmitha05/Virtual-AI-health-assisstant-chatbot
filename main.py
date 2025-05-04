import tkinter as tk
import time
import threading
import datetime

# Extended symptom database for health problems
symptoms_data = {
    "headache": ("Rest, hydrate, avoid screens", "Paracetamol, Ibuprofen"),
    "stomach pain": ("Warm compress, light food", "Buscopan, Gelusil"),
    "cough": ("Warm water, honey, rest", "Cough syrup, Benadryl"),
    "cold": ("Steam inhalation, rest", "Paracetamol, Cetirizine"),
    "sore throat": ("Gargle with salt water", "Lozenges, warm fluids"),
    "vomiting": ("Rest, clear fluids", "Ondansetron, Domperidone"),
    "fever": ("Rest, stay hydrated, cool compress", "Paracetamol"),
    "throat pain": ("Ginger tea, honey", "Lozenges, pain relievers"),
    "hand pain": ("Rest, apply warm compress", "Pain relief gel, Ibuprofen"),
    "leg pain": ("Stretching, massage", "Pain relievers, warm compress"),
    "back pain": ("Good posture, stretching", "Pain relievers, heat pads"),
    "neck pain": ("Gentle stretching, good posture", "Pain relief cream, Ibuprofen"),
    "fatigue": ("Rest, stay hydrated, healthy diet", "Vitamin supplements, Iron"),
    "dizziness": ("Rest, stay hydrated", "Ginger tea, Ibuprofen"),
    "muscle pain": ("Warm bath, stretching", "Pain relievers, warm compress"),
    "allergy": ("Avoid allergens, take antihistamines", "Cetirizine, Loratadine"),
    "diarrhea": ("Stay hydrated, eat bland food", "Loperamide, Oral rehydration salts"),
    "constipation": ("Increase fiber intake, drink water", "Isabgol, mild laxatives"),
    "stress": ("Relaxation exercises, meditation", "Antidepressants, therapy"),
    "insomnia": ("Create a sleep routine, reduce screen time", "Melatonin, Sleep aids"),
    "chest pain": ("Call a doctor immediately, rest", "Consult a doctor immediately"),
    "heart pain": ("Seek medical attention right away", "Consult a doctor immediately")
}

# Common small talk intents
small_talk = {
    "hi": "Hi there! 😊 How can I assist you today?",
    "hello": "Hello! I'm here to help. What would you like to know?",
    "hey": "Hey! Need any help?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "how r u": "I'm good! What can I do for you today?",
    "what's up": "All good here! How can I support you?",
    "nothing": "Alright, just let me know when you're ready. 😊",
    "no": "Okay, take your time. I'm right here.",
    "bye": "Take care! Don't hesitate to come back anytime. 👋",
    "thank you": "You're very welcome! Stay safe. 😊",
    "thanks": "Happy to help! 👍",
    "thank u": "No problem! I'm here whenever you need me.",
    "ok": "Great! Let me know if you have any more questions.",
    "okay": "Okay, I'm all ears if you need anything.",
    "good morning": "Good morning! Hope you have a healthy day!",
    "good night": "Good night! Take care and sleep well.",
    "good afternoon": "Good afternoon! How can I assist you?",
    "who are you": "I'm your health assistant bot. Here to help you anytime!",
    "what is your name": "You can call me HealthBot. 😊",
    "can you help me": "Absolutely! Just tell me what's bothering you.",
    "i'm fine": "Glad to hear that! 😊",
    "i don't know": "That's okay. You can tell me how you're feeling anytime.",
    "hmm": "I see you're thinking! Let me know if you need any help.",
    "mm": "Got it! Anything else you want to ask?",
    "what time is it": lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
    "what is the date": lambda: f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.",
    "what's the weather": "I can't check the weather right now, but make sure to check your weather app for the latest updates!",
    "set an alarm": "I cannot set alarms, but you can use your phone or a smart assistant to do that.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what are you doing": "I'm here to help you with your health and answer any questions. 😊",
    "how's the weather": "I can't check the weather right now, but make sure to check your weather app for the latest updates!"
}

# Spelling corrections
corrections = {
    "stomch": "stomach",
    "troat": "throat",
    "throath": "throat",
    "head pain": "headache",
    "head ache": "headache",
    "sorethroat": "sore throat",
    "muscle ache": "muscle pain",
    "feeling tired": "fatigue"
}

# Main bot logic
def bot_response(user_input):
    user_input = user_input.lower()

    # Apply corrections
    for wrong, right in corrections.items():
        if wrong in user_input:
            user_input = user_input.replace(wrong, right)

    # Small talk
    for phrase in small_talk:
        if phrase in user_input:
            response = small_talk[phrase]
            if callable(response):  # If the response is a function (e.g., time, weather)
                return response()
            return response

    # Symptom check
    for symptom in symptoms_data:
        if symptom in user_input:
            remedy, med = symptoms_data[symptom]
            return f"I'm sorry to hear you're having {symptom}. 💊\nRemedy: {remedy}\nMedication: {med}"

    # General fallback
    return "Hmm... I didn't quite get that. Could you rephrase or tell me what you're feeling?"

# GUI Functions
def display_message(message):
    chat_box.config(state='normal')
    chat_box.insert(tk.END, message + "\n\n")
    chat_box.config(state='disabled')
    chat_box.see(tk.END)

def handle_input():
    user_msg = input_entry.get().strip()
    if not user_msg:
        return
    display_message("🧑 You: " + user_msg)
    input_entry.delete(0, tk.END)

    def bot_reply():
        time.sleep(0.5)
        reply = bot_response(user_msg)
        display_message("🤖 Bot: " + reply)

    threading.Thread(target=bot_reply).start()

# GUI Setup
root = tk.Tk()
root.title("Assistant Chatbot")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="🩺 AI Assistant Chatbot", font=("Helvetica", 16, "bold"), bg="#4a90e2", fg="white", pady=10).pack(fill=tk.X)

chat_box = tk.Text(root, font=("Arial", 12), wrap=tk.WORD, state='disabled', bg="white", fg="black", height=25)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(fill=tk.X, padx=10, pady=5)

input_entry = tk.Entry(input_frame, font=("Arial", 12), width=50)
input_entry.pack(side=tk.LEFT, padx=(0, 10), pady=5, expand=True, fill=tk.X)

# Enable Enter key to send
input_entry.bind("<Return>", lambda event: handle_input())

send_btn = tk.Button(input_frame, text="Send", font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", command=handle_input)
send_btn.pack(side=tk.RIGHT, pady=5)

# Initial greeting
def greet_user():
    display_message("🤖 Bot: Hello! I'm your assistant. How can I help you today?")

threading.Thread(target=greet_user).start()

root.mainloop()
