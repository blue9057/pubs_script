Apple iOS devices are considered by many to be more secure than other mobile
offerings. In evaluating this belief, we investigated the extent to which
security threats were considered when performing everyday activities such as
charging a device. The results were alarming: despite the plethora of defense
mechanisms in iOS, we successfully injected arbitrary software into
current-generation Apple devices running the latest operating system (OS)
software. All users are affected, as our approach requires neither a jailbroken
device nor user interaction.

In this presentation, we demonstrate how an iOS device can be compromised
within one minute of being plugged into a malicious charger. We first examine
Apple’s existing security mechanisms to protect against arbitrary software
installation, then describe how USB capabilities can be leveraged to bypass
these defense mechanisms. To ensure persistence of the resulting infection, we
show how an attacker can hide their software in the same way Apple hides its
own built-in applications.

To demonstrate practical application of these vulnerabilities, we built a proof
of concept malicious charger, called Mactans, using a BeagleBoard. This
hardware was selected to demonstrate the ease with which innocent-looking,
malicious USB chargers can be constructed. While Mactans was built with
limited amount of time and a small budget, we also briefly consider what more
motivated, well-funded adversaries could accomplish. Finally, we recommend
ways in which users can protect themselves and suggest security features Apple
could implement to make the attacks we describe substantially more difficult to
pull off.
