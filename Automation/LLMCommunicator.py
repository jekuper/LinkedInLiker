import re
import random


class LLMCommunicator:
    def __init__(self):
        pass

    def Get_reaction(self, post_text, likes_text, available_reactions):
        try:
            if likes_text is not None and "You" in likes_text:
                return None
        
            if likes_text is not None:
                # Extract the first integer from the likes_text string
                match = re.search(r'\d+', likes_text)
                if match:
                    likes_count = int(match.group())
                    # Check if the likes count is lower than 20
                    if likes_count < 20:
                        return available_reactions[0]["label"]
                    else:
                        # Return available_reactions[0]["label"] with a 10% probability
                        if random.random() < 0.03:
                            return available_reactions[0]["label"]
                        else:
                            return None
            return None
        except Exception:
            return None