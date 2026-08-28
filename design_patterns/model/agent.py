from design_patterns.model.bigram_model import BigramModel


class Agent:
    def __init__(self, name:str, style: str):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0
        self.brain = BigramModel()

    def introduce(self) -> str:
        return f"Hi, I'm {self.name} and I'm a {self.style} agent."

    def respond(self, query: str) -> str:
        if not self.premium and self.query_count >= 3:
            return "Free tier limit reached"
        self.query_count += 1
        words = query.split()
        last_word = words[-1]
        return self.brain.generate(last_word, 15)

    def learn(self, text: str) -> None:
        """
        Learns from the provided text
        """
        self.brain.train(text)
