import random
def generate_story(hero_names, places, verbs, length):
    story = []
    for _ in range(length):
        hero = random.choice(hero_names)
        place = random.choice(places)
        verb = random.choice(verbs)
        adventure = f"{hero} went to {place} to {verb}."
        story.append(adventure)
    return " ".join(story)
hero_names = ["Lazy Johnny", "Sad Lary", "Unshakable Venus"]
places = ["the tavern", "the forest", "the castle", "the mountains"]
verbs = ["fought a battle", "find a chest", "ask the toad", "sat down"]
story_length = 5
story = generate_story(hero_names, places, verbs, story_length)

print(story)
