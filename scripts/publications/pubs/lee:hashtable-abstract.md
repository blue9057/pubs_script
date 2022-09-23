The primary goal of ASLR is to effectively randomize a program's memory layout
so that adversaries cannot easily infer such information. As ASLR is a critical
defense against exploitation, there have been tremendous efforts to evaluate
the mechanism's security. To date, previous attacks that bypass ASLR have
focused mostly on exploiting memory leak vulnerabilities, or abusing
non-randomized data structures.

In this presentation, we leverage vulnerabilities introduced by
performance-oriented software design to reveal new ways in which ASLR can be
bypassed. In addition to describing how vulnerabilities originate from such
designs, we will present real attacks that exploit them.

First, we analyze general hash table designs for various programming languages
(JavaScript, Python, Ruby). To optimize object tracking for such languages,
their interpreters may leak address information. Some hash table
implementations directly store the address information in the table,
whileothers permit inference of address information through repeated table
scanning. We exhaustively examined several popular languages to see whether
each of them has one or both of these problems, and present how they can be
leveraged. As a concrete example, we demonstrate how address information can be
leaked in the Safari web browser by simply running some JavaScript.

Second, we present an analysis of the Zygote process creation model, which is
an Android operating system design for speeding up application launches. The
results of our examination show that Zygote weakens ASLR because all
applications are created with largely identical memory layouts. To highlight
the severity of this issue, we demonstrate two different ASLR bypass attacks
using real applications - Google Chrome and VLC Media Player.
