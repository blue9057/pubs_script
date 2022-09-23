Patching all vulnerabilities for a modern, complex software system (i.e.,
Windows, iOS) is often difficult due to the volume of bugs and response time
requirements. Instead, software vendors usually devise quick workarounds to
mitigate the exploitation of a given vulnerability. However, those patches are
sometimes incomplete, and attackers can utilize different attack vectors to
re-exploit a patched vulnerability. iOS is no exception.

In this presentation, we will disclose our process for jailbreaking the latest
version of iOS (version 7.1.1), running on any iOS device including the iPhone
5s as well as older iPads and iPods. We start by finding new ways to exploit
vulnerabilities with incomplete patches. We then use these vulnerabilities to
discover new avenues of attack. Finally, we chain together these
vulnerabilities and new attacks to run unsigned code out of the sandbox with
root permissions and to defeat mandatory code signing. We include a detailed
disclosure of several new vulnerabilities and the exploit techniques that we
developed.
