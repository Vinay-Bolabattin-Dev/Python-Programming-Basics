class caption_formatter:
    def __init__(self, hook_text):
        self.hook_text=hook_text

    def generate_caption(self, topic):
        return f"{self.hook_text}\n#{topic}"