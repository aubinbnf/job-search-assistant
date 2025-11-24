# Job Search Assistant

An intelligent CV generation tool that creates tailored resumes by matching your experiences with job requirements using semantic analysis and RAG (Retrieval Augmented Generation).

## Overview

Most job application tools prioritize quantity over quality. This project takes a different approach: it deeply understands your profile and generates highly targeted CVs that genuinely match each job offer.

## Key Features

### 1. Rich Profile Management
- Comprehensive user profile system capturing education, work experience, projects, skills, and achievements
- Detailed storage of academic courses, internships, publications, and technical competencies
- Structured data model optimized for semantic matching

### 2. Intelligent Job Offer Analysis
- Automatic parsing and extraction of job requirements
- Identification of key competencies, technologies, and expectations
- Structured representation of job offers for precise matching

### 3. RAG-Based Experience Matching
- Semantic embeddings of your experiences using transformer models
- Vector similarity search to identify most relevant experiences for each job
- Intelligent ranking and scoring of profile elements based on job requirements

### 4. Automated CV Generation
- Dynamic CV creation highlighting the most relevant experiences
- LaTeX-based professional formatting
- Multiple templates (classic, modern, ATS-optimized)
- Maintains authenticity while optimizing presentation

## Why This Approach?

**Quality over Quantity**: Instead of mass-applying to thousands of jobs, this tool helps you create perfectly tailored applications for positions that genuinely match your profile.

**Transparency**: Unlike black-box tools, you understand exactly why certain experiences are highlighted and how your profile matches each offer.

**Technical Depth**: Leverages state-of-the-art NLP techniques (embeddings, RAG, LLM generation) to provide intelligent matching rather than simple keyword matching.

## Technical Stack

- **Backend**: Python, LangChain
- **Embeddings**: Sentence Transformers
- **Vector Database**: FAISS / ChromaDB
- **LLM**: Claude API / OpenAI API
- **CV Generation**: LaTeX with Jinja2 templating
- **Interface**: Streamlit

## Differentiation

Existing tools (JobCopilot, LazyApply, etc.) focus on automation and volume. This project focuses on:
- Deep semantic understanding of profiles and offers
- Intelligent experience selection and prioritization
- Transparent matching explanations
- High-quality, customized outputs
- Open-source and free

## Project Status

**In Development** - MVP targeting core functionality: profile management, RAG-based matching, and LaTeX CV generation.