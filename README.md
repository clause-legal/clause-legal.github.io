# Better Call CLAUSE

**A Discrepancy Benchmark for Auditing LLMs Legal Reasoning Capabilities**

[![EACL 2026](https://img.shields.io/badge/EACL-2026-red.svg)](https://2026.eacl.org/)
[![arXiv](https://img.shields.io/badge/arXiv-2511.00340-b31b1b.svg)](https://arxiv.org/abs/2511.00340)

[Paper](https://arxiv.org/pdf/2511.00340) | [Dataset](#dataset) | [Citation](#citation)

---

## Overview

CLAUSE is a benchmark designed to evaluate the fragility of LLM legal reasoning through systematic contradiction detection in contracts. We produce over 7,500 real-world perturbed contracts from foundational datasets like CUAD and ContractNLI, featuring 10 distinct anomaly categories validated against official statutes using RAG-based grounding.

### Key Findings

- Models miss subtle errors and struggle to justify them legally
- Gemini-2.5 leads with 63%+ F1 on CUAD, but with high-recall and low-precision strategy
- Legal contradictions are consistently harder than in-text contradictions
- Even the best model achieves below 14% accuracy in legal citation matching

---

## Authors

| Manan Roy Choudhury* | Adithya Chandramouli* | Mannan Anand* | Vivek Gupta |
|:---:|:---:|:---:|:---:|
| Arizona State University | Arizona State University | Arizona State University | Arizona State University |

*Equal contribution

---

## Repository Structure

```
CLAUSE-Benchmark/
├── datasets/              # CLAUSE benchmark datasets
│   ├── CUAD_Dataset/      # Perturbations from CUAD contracts
│   └── NLI Dataset/       # Perturbations from ContractNLI
├── paper/                 # Paper source files
└── docs/                  # Project website files
```

---

## Dataset

The CLAUSE dataset is organized into two primary splits based on source corpora.

### Dataset Statistics

| Category | InText Files | InText Perturbations | Legal Files | Legal Perturbations |
|----------|-------------|--------------|-------------|-------------|
| Ambiguity | 741 | 2,417 | 805 | 2,472 |
| Inconsistency | 749 | 2,357 | 830 | 2,711 |
| Misaligned Terminology | 772 | 2,636 | 834 | 2,864 |
| Omission | 754 | 2,498 | 698 | 2,111 |
| Structural Flaws | 760 | 2,540 | 571 | 1,349 |
| **Total** | **3,776** | **12,448** | **3,738** | **11,507** |

### Perturbation Categories

1. **Ambiguity** - Vague or unclear language creating uncertainty
2. **Omission** - Deliberate removal of critical information
3. **Misaligned Terminology** - Inconsistent use of defined terms
4. **Structural Flaws** - Disrupted logical organization
5. **Inconsistencies** - Direct contradictions between sections

Each category exists in two variants:
- **In-Text**: Contradictions within the document itself
- **Legal**: Contradictions with external statutory requirements

---

## Evaluation Tasks

| Task | Description |
|------|-------------|
| Eval 1 | Binary Discrepancy Detection (Yes/No) |
| Eval 2 | Contradiction Type Classification (In-Text / Legal / None) |
| Eval 3 | Explanation-Based Detection with Span Identification and Legal Citation |

---

## Getting Started

### Download Dataset

```bash
git clone https://github.com/mannanxanand/CLAUSE-Benchmark.git
cd CLAUSE-Benchmark
```

### Data Format

Each perturbed contract includes JSON metadata:

```json
{
  "file_name": "Contract_Name.txt",
  "perturbation": [{
    "type": "Ambiguities - Ambiguous Legal Obligation",
    "original_text": "...",
    "changed_text": "...",
    "explanation": "...",
    "contradicted_law": "Lanham Act",
    "law_citation": "15 U.S. Code § 1125(a)"
  }]
}
```

---

## Citation

If you find this work useful, please cite our paper:

```bibtex
@inproceedings{roychoudhury2026clause,
    title={Better Call CLAUSE: A Discrepancy Benchmark for Auditing LLMs Legal Reasoning Capabilities},
    author={Roy Choudhury, Manan and Chandramouli, Adithya and Anand, Mannan and Gupta, Vivek},
    booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
    year={2026}
}
```

---

## Acknowledgements

We are grateful to Rui Heng Foo for his invaluable assistance with the data generation pipelines. We extend our sincere thanks to Arizona State University's Lincoln Center for Applied Ethics, along with their law professors and partners, for lending their expertise to advise on our perturbation categories and to authenticate our perturbed contracts for real-world relevance. We also thank the ASU Law and Pre-Law students for volunteering their time and expertise. Finally, we acknowledge Arizona State University for providing the computational resources that made this research possible.

---

## Contact

For questions about CLAUSE, please contact any of the authors:
- Manan Roy Choudhury: mroycho1@asu.edu
- Adithya Chandramouli: achand57@asu.edu
- Mannan Anand: maanand3@asu.edu
- Vivek Gupta: vgupta85@asu.edu
