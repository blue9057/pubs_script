User input plays an essential role in computer security because
it can control system behavior and make security decisions in the system.
System output to users, or user output, is also important because
it often contains security-critical information that
must be protected regarding its integrity and confidentiality,
such as passwords and user’s private data.
Despite the importance of user input and output (I/O),
modern computer systems often fail to provide
necessary security guarantees on them,
which could result in serious security breaches.

This dissertation aims to build trust in the user I/O in computer systems
to keep the systems secure from attacks on the user I/O.
To this end,
we analyze the user I/O paths on popular platforms including
desktop operating systems, mobile operating systems,
and trusted execution environments such as Intel SGX,
and identified that threats and attacks on the user I/O
can be blocked by guaranteeing three key security properties of user I/O:
integrity, confidentiality, and authenticity.

First, GYRUS addresses the integrity of user input by
matching the user’s original input with the content of
outgoing network traffic to authorize user-intended network transactions.
Second, M-AEGIS addresses the confidentiality of user I/O by
implementing an encryption layer on top of user interface layer that
provides user-to-user encryption.
Third, the A11Y ATTACK addresses the importance of
verifying user I/O authenticity by demonstrating twelve new attacks,
all of which stem from missing proper security checks that
verify input sources and output destinations on
alternative user I/O paths in operating systems.
Finally, to establish trust in the user I/O in a commodity computer system,
I built a system called SGX-USB,
which combines all three security properties
to ensure the assurance of user I/O.
SGX-USB establishes a trusted communication channel between
the USB controller and an enclave instance of Intel SGX.
The implemented system supports common user input devices such as
a keyboard and a mouse over the trusted channel,
which guarantees the assurance of user input.

Having assurance in user I/O allows
the computer system to securely handle commands and data from
the user by eliminating attack pathways to a system’s I/O paths.
