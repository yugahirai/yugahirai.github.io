---
title: 'Multi-Yoked Surface Codes'
date: 2026-10-06
taxonomies:
  tags: [placeholder]
---

![Concept of multi-yoked surface codes](/figs/2026-10-06-multi-yoked_surface_codes/concept_multi_yoked_surface_codes.png)

Today, my new paper on reducing the cost of a surface code logical qubit has been published as an arXiv paper [arXiv:2610.04613](https://arxiv.org/abs/2610.04613).

The idea is to yoke the yoked surface codes recursively. The figure at the top of this page shows the yoked-yoked-yoked surface codes in which the surface codes are concatenated three times. We call such codes multi-yoked surface codes. Concatenating the surface codes recursively has already been studied often; however, a framework for concatenating all the logical qubits in the inner codes remains largely unexplored and this may be the key technique for realizing our multi-yoked surface codes. See the paper for more details.

We have achieved surface codes that are up to 4.5× denser. However, we believe even higher density is possible. The main obstacle is our limited computational resources. To achieve higher density, we need to concatenate many qubits, and simulating such codes quickly becomes computationally expensive. So, we need to invent a way to approximate the simulation without significant loss of accuracy. 