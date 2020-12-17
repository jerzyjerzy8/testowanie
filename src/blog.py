class BlogPostHistory:
    FILENAME = 'posts.txt'
    SEPARATOR = ','

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def save(self):
        with open(self.FILENAME, 'a+') as f:
            data = f'{self.title}{self.SEPARATOR}{self.desc}'
            f.write(data)

    def change_title(self, title):
        self.title = title
        try:
            self.save()
        except OSError:
            raise Exception('Nie mogę zapisać!')

    def change_desc(self, desc):
        self.desc = desc
        try:
            self.save()
        except OSError:
            raise Exception('Nie mogę zapisać!')

    def get_properties(self):
        return self.title, self.desc
