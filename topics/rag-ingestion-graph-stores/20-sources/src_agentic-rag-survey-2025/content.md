Excerpts from arXiv:2501.09136 (v4 HTML).

Abstract:

> Retrieval-Augmented Generation (RAG) has emerged as a solution, enhancing LLMs by integrating real-time data retrieval to provide contextually relevant and up-to-date responses. Despite its promise, traditional RAG systems are constrained by static workflows and lack the adaptability required for multi-step reasoning and complex task management. Agentic Retrieval-Augmented Generation (Agentic RAG) transcends these limitations by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns — reflection, planning, tool use, and multi-agent collaboration — to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows through operational structures ranging from sequential steps to adaptive collaboration. [The paper] introduces a principled taxonomy of Agentic RAG architectures based on agent cardinality, control structure, autonomy, and knowledge representation.

Five-paradigm taxonomy (from the v4 HTML body):

> Naïve RAG represents the foundational implementation of retrieval-augmented generation [...] relying on simple keyword-based retrieval techniques, such as TF-IDF and BM25, to fetch documents from static datasets.
>
> Advanced RAG systems build upon the limitations of Naïve RAG by incorporating semantic understanding and enhanced retrieval techniques [...] leveraging dense retrieval models, such as Dense Passage Retrieval (DPR), and neural ranking algorithms.
>
> Modular RAG represents the latest evolution in RAG paradigms, emphasizing flexibility and customization [by decomposing] the retrieval and generation pipeline into independent, reusable components.
>
> Graph RAG extends traditional Retrieval-Augmented Generation systems by integrating graph-based data structures [and] leverages the relationships and hierarchies within graph data to enhance multi-hop reasoning.
>
> Agentic RAG represents a paradigm shift by introducing autonomous agents capable of dynamic decision-making and workflow optimization [through] iterative refinement and adaptive retrieval strategies to address complex, real-time, and multi-domain queries.

Sources: https://arxiv.org/abs/2501.09136 and https://arxiv.org/html/2501.09136v4
