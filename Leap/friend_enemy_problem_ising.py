from dwave.system import EmbeddingComposite, DWaveSampler

h = {}
J = {('A','K'): 0.5,
    ('B','C'): -0.5,
    ('A','C'): 0.5}

sampler = EmbeddingComposite(DWaveSampler())

sampleset = sampler.sample_ising(h, J, num_reads = 10)
print(sampleset)
