import tkinter as tk
from tkinter import scrolledtext
from Intent2 import Intents
from Generate_Response import chatbot_response

'''
Reference
- Pattern/Intent:
    - https://github.com/Ramakm/AI-Chatbot/blob/main/intents.json
    - https://www.kaggle.com/datasets/elvinagammed/chatbots-intent-recognition-dataset
    - OpenAI. (2024). ChatGPT (3.5) [Large language model]. https://chat.openai.com
- Deep Neural Networking Code
    - https://www.tensorflow.org/guide/keras/sequential_model#when_to_use_a_sequential_model
    - https://www.tensorflow.org/guide/keras/working_with_rnns#train_the_model_with_randomly_generated_data
    - https://medium.com/@ramakrushnamohapatra/create-an-ai-chatbot-from-scratch-738ea385d108
    - OpenAI. (2024). ChatGPT (3.5) [Large language model]. https://chat.openai.com
'''

# Logic --> Define Global Var
last_text_length = 0
conversation_history = ""

# Logic --> Resize Query Text Field
def resize_input_text(event, txt_query):
    # Determine and change the line number of the text field
    lines = txt_query.get("1.0", "end-1c").count("\n") + 1
    txt_query.config(height=lines)

# Logic --> Display Chatbot Response
def add_response(event, txt_chat, response):
    # Specify global vars
    global conversation_history
    global last_text_length

    # Debugging
    print(f"[add_response] CH: {len(conversation_history)}")
    print(f"[add_response] LTXT: {last_text_length}")

    # If new conversation character deteced, officially start the function logic
    if len(conversation_history) > last_text_length:
        # Define response
        conversation = f"EdChat: {response}\n\n"
        # Turn on the chat edit-ability
        txt_chat.configure(state="normal")

        # Insert chatbot response to the chat
        txt_chat.insert(tk.END, conversation)
        # Turn off the chat edit-ability
        txt_chat.configure(state="disabled")

        # Keep track of global var
        conversation_history += conversation
        last_text_length = len(conversation_history)

# Logic --> Display Input Query to Chat Section
def add_message(event, txt_query, txt_chat):
    # Specify global vars
    global conversation_history
    global last_text_length

    # Get user input
    user_input = txt_query.get("1.0", tk.END).strip()
    if user_input:
        # Define complete user input
        conversation = ""
        conversation += f"User: {user_input}\n\n"
        txt_chat.configure(state="normal")
        # Insert user input to the chat
        txt_chat.insert(tk.END, conversation)
        # Clear old user input
        txt_query.delete("1.0", tk.END)
        txt_chat.configure(state="disabled")

        # Keep track of global var
        conversation_history += conversation

        # Trigger the executing ruled_based chatbot functionality
        response = rule_based_chatbot(user_input)

        # Trigger the calling of Chatbot Response
        add_response(None, txt_chat, response)

        # Slider auto-scrolling
        txt_chat.yview_moveto(1.0)

# Logic --> Clear Chat Conversation for both query and response   
def clear_conversation(event, txt_chat):
    # Specify global var
    global conversation_history
    global last_text_length

    if conversation_history:
        # Delete chat conversation
        txt_chat.configure(state="normal")
        txt_chat.delete("1.0", tk.END)
        txt_chat.configure(state="disabled")

        # Keep track of global var
        conversation_history = ""
        last_text_length = 0

        # Debugging
        print(f"[clear_conversation] CH: {len(conversation_history)}")
        print(f"[clear_conversation] LTXT: {last_text_length}")

# Logic --> Execute AI-based chatbot
def AI_based_chatbot(query_message):
    return chatbot_response(query_message)

# UI --> Define Global Config Var
backgroundColor = "royal blue"
textColor = "white"
padX = 10
padY = 5
fontTitle = ("Helvetica", 20, "bold")
fontText = ("Helvetica", 14)
columnSpan = 2

# UI --> Set Up Window
window = tk.Tk()
window.title("EdChat")
window.configure(bg=backgroundColor)

# UI --> Configure Window Resizing
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# UI --> Set up Title Element
frm_title = tk.Frame(master=window)
frm_title.grid(row=0, column=0, columnspan=columnSpan, padx=padX, pady=padY, sticky="ew")

lbl_title = tk.Label(master=frm_title, text="EdChat", font=fontTitle, fg=textColor, bg=backgroundColor)
lbl_title.pack(expand=True, fill=tk.BOTH)

# UI --> Set up Chat Element
frm_chat = tk.Frame(master=window)
frm_chat.grid(row=1, column=0, columnspan=columnSpan, padx=padX, pady=padY, sticky="nsew")

txt_chat = scrolledtext.ScrolledText(master=frm_chat, font=fontText, state="disabled", fg=textColor, bg=backgroundColor)
txt_chat.pack(expand=True, fill=tk.BOTH)

# UI --> Set up Query Element
frm_query = tk.Frame(master=window, bg= backgroundColor)
frm_query.grid(row=2, column=0, columnspan=columnSpan, padx=padX, pady=padY, sticky="ew")

txt_query = tk.Text(master=frm_query, font=fontText, wrap="word", highlightbackground=backgroundColor, height=1)
txt_query.pack(side=tk.LEFT, expand=True, fill="both")

btn_submit = tk.Button(master=frm_query, text="Submit", highlightbackground=backgroundColor, height=1)
btn_submit.pack(side=tk.LEFT, padx=(5, 0))

btn_clear = tk.Button(master=frm_query, text="Clear Conversation", highlightbackground=backgroundColor, height=1)
btn_clear.pack(side=tk.LEFT, padx=(5, 0))

# Logic --> Define Event Handling Actions
# txt_chat.bind("<Configure>", lambda event, txt_chat=txt_chat: add_response(event, txt_chat))
txt_query.bind("<KeyRelease>", lambda event, txt_query=txt_query: resize_input_text(event, txt_query))
btn_submit.bind("<Button>", lambda event, txt_query=txt_query, txt_chat=txt_chat: add_message(event, txt_query, txt_chat))
btn_clear.bind("<Button>", lambda event, txt_chat = txt_chat: clear_conversation(event, txt_chat))

# UI --> Event Listening
window.mainloop()




