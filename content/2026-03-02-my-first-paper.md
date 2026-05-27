---
title: 'The First Paper : "No More Hooks in the Surface Code: Distance-Preserving Syndrome Extraction for Arbitrary Layouts at Minimum Depth"'
date: 2026-03-2
taxonomies:
  tags: [placeholder]
---

Today, my first quantum computing paper has been published as an arXiv paper [arXiv:2603.01628](https://arxiv.org/abs/2603.01628). You must check it out!

This idea came to me at the QIP26 conference in Latvia in January. At the conference dinner, while drunk, I had been designing a new circuit to realize hook-error-free syndrome extraction in the surface code, because my colleagues who are pursuing their Ph.Ds were talking about a quantum algorithm I wasn't familiar with. I used Crumble, software that tracks stabilizers by placing quantum gates wherever you like. At the time, I wanted to reduce the resources for a logical H gate in the surface code, but errors oriented in both spatial and temporal directions reduce the fault distance by a factor of 3/4 or 1/2. In this process, I accidentally noticed that the hex-grid syndrome extraction circuit, first introduced by Gidney et al. in [this paper](https://quantum-journal.org/papers/q-2023-11-07-1172/), can remove hook errors effectively. However, they only proposed a hex-grid implementation in which X tiles move toward the X boundary and Z tiles move toward the Z boundary, so to apply this technique to arbitrary layouts in the square-tiling surface code, I needed to construct another variant in which X tiles move toward the Z boundary and Z tiles move toward the X boundary. I finally found the actual circuit implementation at the QIP conference dinner. Fortunately, with this circuit, all surface code operations using only square tilings become fault-tolerant.

The results were uploaded to arXiv within a month.