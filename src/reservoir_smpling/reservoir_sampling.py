from random import randint


class ReservoirSampling:
    def __init__(self, sample_size):
        self.sample_size = sample_size
        self.sample = list()
        self.iteration = 0

    def add_item(self, item):
        self.iteration += 1
        if len(self.sample) < self.sample_size:
            self.sample.append(item)
        else:
            odds = randint(low=0, high=self.iteration)
            if odds < self.sample_size:
                self.sample[odds] = item

    def retrieve_sample(self):
        return self.sample
