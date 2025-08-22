# 💬 Chat Message History Manager

A simple Python project to manage chat messages with **undo/redo functionality** using **Queue** and **Stack** data structures.  
It also tracks message timestamps to maintain a proper chat history.

---

## 🚀 Features
- ✅ Store incoming messages in **Queue** (FIFO order)
- ✅ **Undo** last sent message using **Stack**
- ✅ **Redo** previously undone messages
- ✅ Track each message with **timestamp**
- ✅ Display full chat history

---

## 🛠️ Tech Requirements
- **Queue** → for incoming message storage  
- **Stack** → for undo/redo actions  
- **Datetime** → for timestamp tracking  


---

## 📖 How It Works
1. **Send Message** → Adds message to the queue and records timestamp.  
2. **Undo** → Removes the last message from the chat and moves it to the redo stack.  
3. **Redo** → Restores the undone message back to the chat.  
4. **Show Messages** → Displays the entire chat history with timestamps.

---

## Example Usage
```bash
python chat_manager.py

## Output Example:

Message sent: Hello! at 2025-08-22 17:05:23
Message sent: How are you? at 2025-08-22 17:05:30

Chat History:
2025-08-22 17:05:23 - Hello!
2025-08-22 17:05:30 - How are you?

Undo: Removed 'How are you?'

Chat History:
2025-08-22 17:05:23 - Hello!

Redo: Restored 'How are you?'

Chat History:
2025-08-22 17:05:23 - Hello!
2025-08-22 17:05:30 - How are you?

