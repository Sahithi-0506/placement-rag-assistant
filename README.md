# Placement Intelligence RAG Assistant

## Overview

Placement Intelligence RAG Assistant is an advanced hybrid Retrieval-Augmented Generation (RAG) system designed to answer placement-related analytical queries from large placement datasets and PDF documents.

Unlike traditional chatbot-based RAG systems, this project combines:

- Semantic Retrieval
- Structured Reasoning
- Query Routing
- Metadata Filtering
- Conflict Detection
- Trend Analysis
- Multimodal Chart Reasoning

to provide accurate and context-aware answers for complex placement intelligence queries.

The system runs fully offline using local embeddings, ChromaDB vector storage, and Ollama local language models.

---

# Problem Statement

Traditional RAG systems struggle with:

- Table understanding
- Numerical filtering
- Multi-condition reasoning
- Trend analysis
- Analytical comparisons
- Conflict detection
- Hallucination prevention

This project solves these challenges by integrating structured reasoning tools with retrieval pipelines.

---

# Key Features

## Core RAG Features

- PDF ingestion pipeline
- Text chunking using LangChain
- ChromaDB vector database
- HuggingFace local embeddings
- Ollama local LLM integration
- Streamlit chatbot interface
- Semantic retrieval pipeline

---

## Advanced RAG Features

### Structured Table Extraction
Extracts placement company records directly from PDF tables using pdfplumber.

### Metadata-Based Retrieval
Uses metadata filtering for accurate structured retrieval.

### Query Routing
Classifies queries into:
- Structured queries
- Multi-company queries
- Out-of-context queries
- Analytical reasoning queries

### Multi-Hop Reasoning
Supports:
- CGPA filtering
- Backlog filtering
- Package comparison
- Bond analysis
- Eligibility reasoning

### Trend Reasoning
Handles:
- Package growth analysis
- Year-wise comparison
- Hiring trend reasoning

### Conflict Detection
Detects conflicting placement data such as:
- Official CGPA vs portal CGPA
- Inconsistent package values

### Multimodal Chart Reasoning
Extracts hiring chart data and answers chart-based analytical questions.

### Hallucination Prevention
Rejects unsupported queries outside the dataset.

---

# System Architecture

```text
PDF Dataset
     ↓
PDF Extraction
     ↓
Chunking + Structured Table Extraction
     ↓
ChromaDB Vector Store
     ↓
Query Router
     ↓
 ┌───────────────────────────┐
 │                           │
 ↓                           ↓
RAG Retrieval         Reasoning Engine
 │                           │
 ↓                           ↓
Ollama LLM           Analytical Computation
 └─────────────┬─────────────┘
               ↓
        Final Response
```

---

# Tech Stack

| Component | Technology |
|---|---|
| Language Model | Phi3 Mini (Ollama) |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Embeddings |
| Frontend | Streamlit |
| PDF Extraction | pdfplumber |
| Programming Language | Python |
| Local Inference | Ollama |

---

# Project Structure

```text
placement-rag-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── Placement_RAG_Dataset_Enhanced.pdf
│
├── chroma_db/
│
├── src/
│   ├── load_pdf.py
│   ├── chunking.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── rag_chain.py
│   ├── query_router.py
│   ├── reasoning_engine.py
│   ├── structured_data_extractor.py
│   ├── table_loader.py
│   └── test files
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd placement-rag-assistant
```

---

## Create Environment

```bash
conda create -n rag-env python=3.10
conda activate rag-env
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

---

## Pull Local Model

```bash
ollama run phi3:mini
```

---

# Create Vector Database

```bash
python -m src.ingest
```

---

# Run Streamlit Application

```bash
streamlit run app.py
```

---

# Sample Queries

## Direct Retrieval

- What is the CGPA requirement for TCS?
- What is the package offered by Google?

---

## Multi-Company Queries

- Which companies require CGPA above 8.0?
- List all companies that allow at least 2 backlogs.

---

## Analytical Queries

- Which zero-bond companies offer more than 40 LPA?
- Which Python-focused company offers highest package?

---

## Eligibility Reasoning

- A student with 7.6 CGPA and 1 backlog wants the highest paying company. Which company should they apply for?

---

## Trend Reasoning

- Which company package grew the most from 2021 to 2024?

---

## Conflict Detection

- Explain the Amazon CGPA conflict.

---

## Multimodal Chart Reasoning

- How many SDE roles does Amazon hire?
- How many intern roles does Oracle hire?

---

# Completed Modules

| Module | Status |
|---|---|
| PDF Ingestion | Completed |
| Chunking Pipeline | Completed |
| ChromaDB Integration | Completed |
| Embedding Pipeline | Completed |
| Ollama Integration | Completed |
| Query Routing | Completed |
| Metadata Filtering | Completed |
| Structured Table Extraction | Completed |
| Multi-Hop Reasoning | Completed |
| Trend Analysis | Completed |
| Conflict Detection | Completed |
| Multimodal Chart Reasoning | Completed |
| Hallucination Prevention | Completed |
| Streamlit Chat UI | Completed |

---

# Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Reranking
- Context Compression
- OCR-based Image Understanding
- True Vision-Language Models
- Agentic Workflow Orchestration
- Source Attribution UI

---

# Conclusion

Placement Intelligence RAG Assistant demonstrates how advanced RAG systems can move beyond simple semantic retrieval and support:

- Analytical reasoning
- Structured computation
- Trend analysis
- Conflict detection
- Multimodal reasoning
- Hallucination control

This project represents an advanced hybrid RAG architecture combining retrieval pipelines with reasoning tools for accurate placement intelligence analysis.