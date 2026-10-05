# MESSAGE CLASS

class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# USER CLASS

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in the chatroom.")
        elif chatroom.add_user(self):  # add_user sets self.chatroom
            print(f"{self.username} joined {chatroom.name}.")
        else:
            print(f"{self.username} could not join {chatroom.name} (username taken).")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} not in any chatroom.")
        else:
            room = self.chatroom
            room.remove_user(self)  # remove_user clears self.chatroom
            print(f"{self.username} left {room.name}.")

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# CHATROOM CLASS

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if any(u.username == user.username for u in self.users):
            return False
        self.users.append(user)
        user.chatroom = self
        return True

    def remove_user(self, user):
        self.users.remove(user)
        user.chatroom = None

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # shows message to all the users
        print()

    def show_chat_history(self):
        print(f"--- Chat history for {self.name} ---")
        for message in self.messages:
            print(message)
        print()


# EXAMPLE USAGE

if __name__ == "__main__":
    room = ChatRoom("Python lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone")
    u2.send_message("Hi Alice")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up??!!")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()