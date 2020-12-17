class AvgCalculator:
    def __init__(self, filename):
        self.filename = filename

    def _get_content(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return [line.split(',') for line in lines]

    def _ensure_casted_data(self):
        data = self._get_content()
        new_data = []
        for x in data:
            new_data.append([int(n) for n in x])
        return new_data

    def calculate(self):
        numbers = self._ensure_casted_data()
        return [sum(x)/len(x) for x in numbers]

    def get_data(self):
        return self._get_content()
