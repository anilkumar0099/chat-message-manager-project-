from collections import deque
from datetime import datetime

# -------------------------------
# Message class (stores text + timestamp)
# -------------------------------
class Message:
    def __init__(self, text):
        self.text = text
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] {self.text}"


# -------------------------------
# Chat Manager (Queue + Stack)
# -------------------------------
class ChatManager:
    def __init__(self):
        self.message_queue = deque()   # Queue for chat history
        self.undo_stack = []           # Stack for undo
        self.redo_stack = []           # Stack for redo

    def send_message(self, text):
        msg = Message(text)
        self.message_queue.append(msg)
        self.undo_stack.append(msg)
        self.redo_stack.clear()   # clear redo when new msg is sent
        print(f"Sent: {msg}")

    def display_chat(self):
        if not self.message_queue:
            print("\n Chat is empty.\n")
            return
        print("\n Chat History:")
        for msg in self.message_queue:
            print(msg)
        print()

    def undo(self):
        if not self.undo_stack:
            print(" No messages to undo.")
            return
        msg = self.undo_stack.pop()
        self.message_queue.remove(msg)
        self.redo_stack.append(msg)
        print(f" Undo: Removed '{msg.text}'")

    def redo(self):
        if not self.redo_stack:
            print(" No messages to redo.")
            return
        msg = self.redo_stack.pop()
        self.message_queue.append(msg)
        self.undo_stack.append(msg)
        print(f" Redo: Restored '{msg.text}'")


# -------------------------------
# Interactive Menu
# -------------------------------
def main():
    chat = ChatManager()

    while True:
        print("\n===== Chat Manager =====")
        print("1. Send Message")
        print("2. Show Chat History")
        print("3. Undo Last Message")
        print("4. Redo Last Undo")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter your message: ")
            chat.send_message(text)

        elif choice == "2":
            chat.display_chat()

        elif choice == "3":
            chat.undo()

        elif choice == "4":
            chat.redo()

        elif choice == "5":
            print("👋 Exiting Chat Manager. Goodbye!")
            break

        else:
            print(" Invalid choice! Please try again.")


# -------------------------------
# Run program
# -------------------------------
if __name__ == "__main__":
    main()

