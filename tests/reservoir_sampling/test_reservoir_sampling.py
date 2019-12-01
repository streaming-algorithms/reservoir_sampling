import pytest

from reservoir_smpling.reservoir_sampling import ReservoirSampling


class TestReservoirSampling:
    @pytest.mark.parametrize("sample_size", [
        10,
        100,
        1000
    ])
    def test_init(self, sample_size):
        reservoir_sampling = ReservoirSampling(sample_size=sample_size)
        assert reservoir_sampling.sample_size == sample_size
        assert reservoir_sampling.sample == list()
        assert reservoir_sampling.iteration == 0

    @pytest.mark.parametrize("sample_size, sample, item", [
        (5, [1, 2, 3], 4),
        (10, [], 42),
        (5, [1, 2, 3, 4], 5)
    ])
    def test_add_item(self, sample_size, sample, item):
        iteration = len(sample)
        reservoir_sampling = ReservoirSampling(sample_size=sample_size)
        reservoir_sampling.sample = sample.copy()
        reservoir_sampling.iteration = iteration
        reservoir_sampling.add_item(item=item)
        assert reservoir_sampling.iteration == iteration + 1
        assert reservoir_sampling.sample == sample + [item]
