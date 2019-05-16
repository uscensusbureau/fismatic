# FISMAtic Research Round One Summary

May 13, 2019

# Background

The Census Innovation & Operational Efficiency Program (IOE) awarded funding to the FISMAtic project to:

> ...improve the [Authority to Operate (ATO)] process by (1) reducing costs, (2) speeding time to completion, and (3) improving consistency with machine learning, natural language processing and computer vision.

_FISMAtic Business Case_

See the [Appendix](#appendix) for details about the interview process.

# Terms

- **Assessors:** Those that are responsible for checking the compliance of systems; sit in an agency's Security team.
- **ATO package:** The SSP and other documentation needed to get an ATO.
- **Authority to Operate (ATO):** The approval for a government system to be run in production, and the compliance process for getting there.
- **Compliance:** Ensuring that a system meets minimum security requirements.
- **Program teams** : Those who are trying to build/launch a system.
- **Security:** The sum of processes and features safeguarding systems and data.
- **System Security Plan (SSP):** The primary document in an ATO package, the bulk of which contains the [NIST 800-53 security controls](https://nvd.nist.gov/800-53/Rev4).

# Major findings

## A) Program teams are not well-equipped to complete ATOs.

> The templates have 'NIST language' and you have no idea what that really means.

Program teams are often lacking compliance experience. The templates are long and hard to understand, if they are provided at all.

> There is no other domain in all my work in government where plentiful examples are not available … makes me furious … can't emphasize this enough.

ATO packages are considered sensitive, so are not easily accessible to program teams going through ATOs. The lack of access to examples came up in the interviews more than any other topic.

## B) Prioritization of security/compliance work is critical.

> Compliance is a byproduct of good security.

For the program teams, systems need to be designed with security in mind. This means having security experience in the team, if not involving the assessment teams themselves early on (rather than only at the end). Unfortunately, compliance teams are generally overloaded as is, so there is a tension here.

> Distill [compliance work] down to the points and facts that matter.
>
> Help [program teams] climb ladders, rather than pole vault.

Instead of treating all security controls as equal, a number of interviewees on both sides got value out of prioritizing controls or parts of the systems that had the largest security implications. This can happen at time of control selection, and/or during assessment.

## C) Low (perceived) value of compliance work by program teams.

> [Compliance] feels like a bureaucratic checkbox...I want to build secure systems.
>
> How much of all of this is putting lipstick on a pig?

Program teams interviewed citied caring about security and privacy, but there was a perceived lack of value of compliance work, particularly the documentation and the assessors themselves. They saw that compliance work being distinct from the security of the systems they were building

> I've heard of good assessors...but my experience [in three agencies] has been really poor.

Security experience of assessors can vary greatly. Program teams had positive experiences when the assessors had technical background, and they could therefore talk through potential solutions with the program teams.

> [Assessments are often] veering into art of security rather than the science of it.
>
> What's the interpretation of the control of the system you're building in the organization you're building it? That's the root of all evil with SSPs.

Despite the thousands of pages of NIST documentation that surround ATO processes, there is a high degree of subjectivity in SSPs and assessments in terms of what is considered "good".

> I don't think [assessors] look at 95% of what I give them...I find mistakes later that they should have caught.

Assessment teams often hand program teams the compliance documentation requirements/templates, and only re-engage once the first draft is complete. There can be many months of turnaround time before and after this point, as the effort to complete (especially without experience – see [A](#a-program-teams-are-not-well-equipped-to-complete-atos)) and review the documentation is high.

## D) Compliance processes work best when there is close collaboration.

About half of the interviews mentioned the value of close collaboration and trust between the program teams and the assessors. The following terms were used about assessors in these cases:

> Mutual understanding
>
> Ground-truthing
>
> Your SSP Sherpa
>
> Here on a fact-finding mission, not to convict
>
> Emotional support
>
> Hand-holding

Unfortunately, a program team getting their assessor's time can be challenging, as noted in [B](#b-prioritization-of-securitycompliance-work-is-critical). Multiple interviews also cited the importance of both sides being up front about their experience and shortcomings, rather than seeing the other side as an opponent.

## E) There is power and confusion in inheritance.

[Paraphrased] Using OpenControl took authoring time from nine months for the first system, to four months for the second, then down to two months for the third. I have a goal of two weeks.

SSPs are generally Word documents that can be hundreds of pages in length. Interviewees estimated that only 10-40% of the content in those documents are unique to the system they correspond to; the rest is either boilerplate in the template, or is copied-and-pasted. There were two reasons cited for the latter:

- Many controls are fulfilled by the agency and underlying platforms/services (enterprise hosting, single sign-on, etc.)
- It's easier to find a similar system that's been approved and copy from their SSP than to write from scratch (see [A](#a-program-teams-are-not-well-equipped-to-complete-atos))

As noted in the quote above, leveraging this inheritance in authoring an SSP (through [OpenControl](https://github.com/opencontrol/schemas#why-opencontrol) or another tool) can result in massive reduction in time to ATO. The downsides are:

- SSP authors can copy-and-paste too much (to save themselves time/headache and try and get approved), misrepresenting their systems, causing confusion and delays.
- It's hard for reviewers to tease out the information specific to that system from the inherited systems that are out of scope.

## F) There are compliance tools, but they are under-leveraged.

To complete ATOs, program team members and assessors in many agencies write in Word documents, then versions of the document ricochet back and forth with comments and edits. Interviewees cited difficulty keeping track of who was editing and merging those edits together.

> Everybody's [compliance] tool had 20% of reality.

There are various commercial and open source tools available to help with compliance documentation workflows, including inheritance (see [E](#e-there-is-power-and-confusion-in-inheritance)). Even so, the majority of agencies aren't using them to their full extent, if at all. It's unclear how much of this is due to awareness vs cost vs features.

# Potential paths forward

These are not mutually exclusive.

## Automated feedback

This has been referred to as "Clippy for ATOs", and was the proposal in the original Business Case. This could be anything from a [linter](https://stackoverflow.com/questions/8503559/what-is-linting) with simple business rules up through natural language processing to give feedback on the quality of the content.

Pros:

- This was the Solution funded by IOE
- Reduces the feedback cycles

Cons (specifically asked for feedback on this idea, hence the longest list for this one):

- Requires access to a large set of SSPs in a machine-readable form
  - _"To succeed, you need a corpus of SSPs, [you need to be able to extract the content], and you need to be able to bring in powerful analytical tools."_
  - GSA (at least twice) and DHS worked on text extraction from SSPs, which was laborious.
- Likely challenging to give substantive feedback
  - _"Seems like it will be a lot of work for little reward."_
  - See subjectivity in [C](#c-low-perceived-value-of-compliance-work-by-program-teams).
- Even from human reviewers, there is often more noise than signal
- Only possible for a machine learning-driven system to give feedback that's "you're like the other SSPs out there, or not
- High effort for low value, relative to other options

## Surface SSP/control examples

The highest-cited need from interviewees was having approved/good examples to draw from for inspiration/clarification, if not copying from directly. These examples can be hand-picked, purpose-written, or drawn dynamically from a larger set (perhaps from similar systems?).

Pros:

- The highest-cited request from interviewees
- A step along the way to automated feedback and surfacing inheritable systems
- MVP possible without writing any code

Cons:

- SSPs being considered sensitive likely an obstacle to making their controls broadly accessible
- May require manual control selection/review/scrubbing

## Surface inheritable systems/controls

Agencies have platforms and other General Support Systems (GSS's) that can be leveraged by program teams to reduce their technical and compliance burden. These providers, along with their compliance information, can be surfaced and more strongly encouraged.

Pros:

- [Makes the right thing the easy thing](https://www.youtube.com/watch?v=xqT8e6_yzLg)
- Reduces surface area (and thus security risk, operational burden, etc.) of downstream systems
- MVP possible without writing any code

Cons:

- Only useful if those platforms are in place
- Only desirable by program teams if those platforms will make their lives better

## Get security and compliance experience into program teams

This can happen through training existing program team members, adding new staff, or embedding existing assessors (though more may be needed).

Pros:

- Directly addresses a top finding from the research
- Results in better security

Cons:

- Difficult to do this across all projects comprehensively
- It's expensive

## Reduce the documentation burden

This can happen through tailoring/prioritizing controls, either agency-wide, per-system, or over time (example: [GSA LATO](https://gsablogs.gsa.gov/innovation/2014/12/10/it-security-security-in-an-agile-development-cloud-world-by-kurt-garbars/)).

Pros:

- Less work for program teams and assessors
- High-priority controls can still be covered
- Census's Office of Information Security (OIS) requested a tool to help with control selection when FISMAtic was first pitched, so meeting a known internal need

Cons:

- Harder if common platforms aren't being utilized
- Reduces the number of compliance checks, which could let issues slip through the cracks

# Appendix

Over 3-4 weeks, the xD team conducted thirteen interviews using these questions:

- Intro
- What’s your role?
- How many ATOs have you been involved with?
- What role(s) have you played (formally or informally) as part of ATOs?
- For system owners: What value have you gotten from people on the assessment side?
- What are your challenges around the SSP?
- What are the most common problems that cause back-and-forth delays?
- What could make these interactions easier?
- If you had access to a large number of SSPs in a machine-readable format and the time/skills/tools to analyze them, what would be the top five things you’d want to know from them?
- Do you know of tools that give feedback?
- Who else should I talk to?

The interviews were conducted with people from the following organizations:

- [Centers for Medicare and Medicaid (CMS)](https://www.cms.gov/)
- [CivicActions](https://civicactions.com/)
- [Epigen Technology](http://epigentechnology.com/)
- [GovReady](https://govready.com/)
- [General Services Administration (GSA)](https://gsa.gov)
- [National Geospatial-Intelligence Agency (NGA)](https://www.nga.mil/)
- [Onyx Point](https://www.onyxpoint.com/)
- [Telos](https://www.telos.com/)
- [United States Air Force](https://www.airforce.com/)

Interviewees represented various stakeholder positions in the ATO process, with current and former roles including:

- Chief Data Officer (CDO)
- Chief Information Security Officer (CISO)
- Information Systems Security Manager (ISSM)
- Lead Architect
- Startup Founder/CEO
- System Owner

They had each been involved with a number of ATOs, ranging anywhere from three to 200. All quotes in this document are taken directly from interviews.
