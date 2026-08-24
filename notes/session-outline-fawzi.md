<!-- Recovered from commit 9be5a43. Fawzi wrote this outline in README.md; the merge
     that brought in the slide material replaced the file with the public README and the
     outline was lost from the working tree. Kept here so it is not lost again, and
     because three things in it are not yet in the deck. -->

# Session outline — Fawzi Mohamed, 24 August 2026

**Still to fold into the slides:**

- **GPU Scorer** — the tool for checking a project's efficiency. Module 3's efficiency
  slide carries a `TODO(verify)` asking exactly this question, and this is the answer.
- **Serving** — `https://servingdev.swissai.svc.cscs.ch` and
  `https://github.com/swiss-ai/model-launch`. Module 3's "Serving at scale" is an
  explicit placeholder because we did not know whether serving goes through the
  inference service or a Slurm job. These two links look like the answer.
- **User Lab** and **CSCS2go** — two other routes to resources at CSCS. Module 1 covers
  only the Swiss AI route, and says so, but the audience may include people arriving by
  the others.

None of the three has been verified yet, so none is on a slide.

---

# ML Project Example

The goal of this project is to create a presentation/demo of the project lifetime of an ML project of about 1h for the SwissAI Initiative
Yearly Meeting of 26 Aug 2026 in Bern ([Program](https://docs.google.com/document/d/10WrRF5sDXxmHqD3sa7UVBTItCRBj2lt4zXMKkfiFsl4/edit?usp=sharing))
as discussed in [confluence](https://confluence.cscs.ch/spaces/SRM/pages/1062307901/SwissAI+Initiative+Annual+Meeting) and in our slack [#swissai-annual-meeting-coordination](https://cscs-lugano.slack.com/archives/C0B2QUYJFNK).

# How to get resource at CSCS
## SwissAI
- small projects (6 months ≤ 32k GPUh)
- large project (12 months >= 500'000GPUh)
- large project must be *ready* to run on alps
- require tests on real HW and expected size
- GPU Scorer should be used to check their efficiency 
- data requirements should be defined
## User Lab
## CSCS2go

- project request hints
  - large projects need to be ready to use (small project first)
- when you get access to the project,
  - invite others
  - resources
  - monitor project resource usage
- set up workflows
  - FirecREST
  - jupyter
- inference l1
- hpc console
  - resources of jobs
- import data
- prepare training data (where to put it)
- training
  - alps extended images
- inference
    - https://servingdev.swissai.svc.cscs.ch
    - https://github.com/swiss-ai/model-launch
- post training
- kubernetes

- Discussion (30 min)
- planned things, suggestions
- Try to leverage material of [user day](https://confluence.cscs.ch/spaces/UP/pages/1062307425/User+Lab+Day+2026)
