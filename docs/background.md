# Background

"The ATO process", as it's commonly called, is formally defined in the National Institute of Standards & Technology (NIST)'s [Risk Management Framework (RMF)](<https://csrc.nist.gov/projects/risk-management/risk-management-framework-(RMF)-Overview>):

<img alt="NIST Risk Management Framework diagram" width="500" src="https://csrc.nist.gov/CSRC/media/Projects/Risk-Management/images-media/OrgRMF_v3.png"/>

This process was developed as a result of the [Federal Information Security Management Act (FISMA)](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project). See [Introduction to ATOs](https://atos.open-control.org/) for more information.

Security compliance is time consuming (and therefore expensive) for most organizations in and around the federal government. Two particular pain points were identified:

- Select[ing] Controls that are appropriate for a given system
- The back-and-forth between delivery teams Implement[ing] and reviewers Assess[ing] Controls

Delivery teams, who may or may not have experience writing System Security Plans (SSPs), spend a lot of time working on the language for security controls. This is then sent to the assessor, who may be pointing out common mistakes. Each of these back-and-forths can take days or weeks, costing staff hours on both sides and stretching out the time before the project can actually deliver value to users.

**Our hypothesis is that we can reduce the time spent on the Select, Implement, and Assess Controls steps of the RMF through tooling.**
