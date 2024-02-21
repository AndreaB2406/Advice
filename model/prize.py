class Prize:
    def __init__(self, id, title, description, image):
        self.id = id
        self.title = title
        self.description = description
        self.image = image

    def prize_to_dict(self):
        dictionary = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image
        }
        return dictionary