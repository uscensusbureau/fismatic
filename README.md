# FISMAtic :zap:

_Pronounced like "automatic", but starting with "fizz"._

<img alt="Greased Lightning" src="https://r.hswstatic.com/w_907/gif/lightning-myths-9.jpg" width="450"/>

The goal of FISMAtic is to reduce the amount of time spent authoring, reviewing, and editing the security compliance documentation leading up to an Authority to Operate (ATO). We plan to build prototype(s) that:

- Automate validation of and feedback on security compliance documentation
  - Think "Clippy for ATOs" :eyes: :paperclip: :lock:
- Help compliance teams select security controls that are appropriate to a system (tailored baselines)
  - This can cut out time spent around irrelevant controls in all other steps of the compliance lifecycle

## Background

"The ATO process", as it's commonly called, is formally defined in the National Institute of Standards & Technology (NIST)'s [Risk Management Framework (RMF)](<https://csrc.nist.gov/projects/risk-management/risk-management-framework-(RMF)-Overview>):

<img alt="NIST Risk Management Framework diagram" width="500" src="https://csrc.nist.gov/CSRC/media/Projects/Risk-Management/images-media/OrgRMF_v3.png"/>

This process was developed as a result of the [Federal Information Security Management Act (FISMA)](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project).

Security compliance is time consuming (and therefore expensive) for most organizations in and around the federal government. Two particular pain points were identified:

- Select[ing] Controls that are appropriate for a given system
- The back-and-forth between delivery teams and assessors Implement/Assess[ing the] Controls

Delivery teams, who may or may not have experience writing System Security Plans (SSPs), spend a lot of time working on the language for security controls. This is then sent to the assessor, who may be pointing out common mistakes. Each of these back-and-forths can take days or weeks, costing staff hours on both sides and stretching out the time before the project can actually deliver value to users.

**Our hypothesis is that we can reduce the time spent on the Select, Implement, and Assess Controls steps of the RMF through tooling.**

## Call for collaborators

If you’ve worked in this space or are interested in collaborating, please reach out in an issue or by email. Thanks! aidan.l.feldman@census.gov
