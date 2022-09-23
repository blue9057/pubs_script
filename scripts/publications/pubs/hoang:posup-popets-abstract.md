The ability to query and update over encrypted data is
an essential feature to enable breach-resilient
cyber-infrastructures.
Statistical attacks on searchable encryption (SE)
have demonstrated the importance of
sealing information leaks in access patterns.
In response to such attacks,
the community has proposed the Oblivious Random Access Machine (ORAM).
However, due to the logarithmic communication overhead of ORAM,
the composition of ORAM and SE is known to be
costly in the conventional client-server model,
which poses a critical barrier toward its practical adaptations.

In this paper, we propose a novel hardware-supported
privacy-enhancing platform called Practical Oblivious
Search and Update Platform (POSUP),
which enables oblivious keyword search and
update operations on large datasets with high efficiency.
We harness Intel SGX to realize
efficient oblivious data structures for oblivious search/update purposes.
We implemented POSUP and evaluated its performance on
a Wikipedia dataset containing ≥ 2^29 keyword-file pairs.
Our implementation is highly efficient,
taking only 1 ms to access a 3 KB block with Circuit-ORAM.
Our experiments have shown that POSUP offers up to
70× less end-to-end delay with 100× reduced
network bandwidth consumption compared with
the traditional ORAM-SE composition without secure hardware.
POSUP is also at least 4.5× faster for
up to 99.5% of keywords that can be searched compared with
state-of-the-art Intel SGX-assisted search platforms.
