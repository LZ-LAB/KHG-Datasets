# Knowledge-Hypergraph-Datasets
Knowledge Hypergraph Datasets - Analysis and Processing

We compare and analyze the publicly available datasets from various top conferences (journals) in the field of knowledge hypergraph research in recent years (e.g., JF17K, WikiPeople, FB-AUTO, M-FB15K, their fixed-arity sub-datasets), and there exists a lot of inconsistent information (e.g., the number of entities, the number of relations, the ratio of train/test/valid dataset division, etc.).
We believe in this phenomenon, making it confusing for researchers.

This has resulted in a lack of convincing and fair performance comparisons in the experimental results of many published papers in the field of knowledge hypergraphs.
Many of the classic works from these top conferences (journals) still directly cite each other despite the dataset mismatch.

By analyzing several public datasets (JF17K, WikiPeople, FB-AUTO, M-FB15K) that have been used most frequently in recent years, we conducted data standard processing, fixed-arity extraction process **(running code: Data Processing.py)**, and generated the corresponding id number of entities and relations **(running code: tuple2id.py)**.
We proofread the processed datasets in detail, and have verified that all are accurate and can convincingly and fairly support researchers to carry out experimental work. The file **"Datasets Information.xlsx"** shows all the details of the datasets.
