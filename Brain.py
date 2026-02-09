# NBC-1 : Nexus Bucky Core (Basic Brain)
# Owner: Kishore

class NBCBrain:
    def __init__(self):
        self.name = "Nexus Bucky Core"
        self.version = "NBC-1"
        self.owner = "Kishore"

        # Memory (offline – simple)
        self.memory = {
            "values": [
                "Never give up",
                "Learning from failure",
                "Care for family"
            ],
            "focus": [
                "Education",
                "Life guidance",
                "Anime facts",
                "Basic AI concepts"
            ]
        }

    def think(self, user_input):
        user_input = user_input.lower()

        if "sad" in user_input or "failure" in user_input:
            return "I am with you. Failure is only a step, not the end."

        if "anime" in user_input:
            return "Anime teaches discipline, sacrifice, and never giving up."

        if "ai" in user_input:
            return "AI is logic + data + learning. You are learning step by step."

        if "hello" in user_input or "hi" in user_input:
            return "Hello Kishore. I am listening."

        return "Tell me more. I am here for you."


# Run brain in terminal (testing)
if __name__ == "__main__":
    brain = NBCBrain()
    print("NBC-1 Brain Online. Type 'exit' to stop.\n")

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("NBC-1 going offline.")
            break
        reply = brain.think(user)
        print("NBC-1:", reply)
