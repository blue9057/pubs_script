Intel Software Guard Extensions (SGX) provides
a strongly isolated memory space,
known as an enclave, for a user process,
ensuring confidentiality and integrity against software and hardware attacks.
Even the operating system and hypervisor cannot access the enclave because
of the hardware-level isolation.
Further, hardware attacks are neither able to disclose plaintext data from
the enclave because its memory is always encrypted nor modify it because
its integrity is always verified using an integrity tree.
When the processor detects any integrity violation,
it locks itself to prevent further damages;
that is, a system reboot is necessary.
The processor lock seems a reasonable solution against
such a powerful hardware attacker;
however, if a software attacker has a way to trigger integrity violation,
the lock could result in a severe denial-of-service (DoS) attack.

In this paper,
we introduce the SGX-Bomb attack that launches the Rowhammer attack against
enclave memory to trigger the processor lockdown.
The SGX-Bomb attack is simple yet alarming.
Inside an enclave, this attack first finds
conflicting row addresses at the same DRAM bank, and then
repeatedly accesses them while bypassing the cache.
If arbitrary bit flips have occurred inside the enclave because of
the Rowhammer attack,
any read attempts to the enclave memory results in a failure of
integrity check so that the processor will be locked,
and the system should be rebooted.
The SGX-Bomb attack is a serious threat especially to
the public cloud providers who are supposed to
run unknown enclave programs received from their clients,
which might shut down their servers shared with other clients.
We evaluate the effectiveness of the SGX-Bomb attack in
a real environment with DDR4 DRAM;
it takes 283 s to hang the entire system with the default DRAM refresh rate,
64 ms.
