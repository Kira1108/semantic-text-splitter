# Semantic Splitter
A text chunking library that uses AI to intelligently split documents based on semantic meaning rather than just character count.    

## Install
```bash
git clone this_repo
cd semantic-text-splitter
pip install -e .
```

## Features
Semantic chunking - Splits documents at natural semantic boundaries    
Azure OpenAI integration - Leverages Azure's GPT-4o model for intelligent splitting    
Smart planning - Creates a tailored chunking plan based on document structure    
DOCX support - Handles Microsoft Word documents with full formatting awareness    

## Usage
```python
from semantic_splitter.split_pipelines import SemanticPipeline
pipe = SemanticPipeline()
chunks = pipe.split_docx("file.docx")
```

```python
from semantic_splitter.split_pipelines import SemanticPipeline
pipe = SemanticPipeline(trim_long_chunks=True)
chunks = pipe.split_text("Your long text here")
```

### Overall Process
The Semantic Splitter uses a three-stage pipeline approach to split documents semantically rather than by arbitrary character counts:

- Document Reading
- Planning & Analysis
- Anchor Finding & Splitting

#### Stage 1: Document Reading
The pipeline begins with the DocxReader class that extracts content from DOCX files while preserving document structure. This ensures that the semantic analysis has access to the original document formatting, which provides important context for intelligent splitting.

#### Stage 2: Planning
The SplitPlanner class examines the document and creates a tailored plan for splitting:

It uses Azure OpenAI's GPT-4o model to analyze the document structure    
It identifies if the document has natural section headers (like "1.1", "2.3", etc.)    
It determines the appropriate granularity for splitting based on content type   
It creates a splitting strategy optimized for that specific document   
The planning prompt instructs the model to:   

- Identify section header patterns
- Determine optimal splitting granularity
- Create a brief content summary
- Keep the plan concise (under 300 Chinese characters)

#### Stage 3: Anchor Finding & Splitting
Using the plan from stage 2, the AnchorFinder class:

Identifies optimal "anchor sentences" where the text should be split
Ensures each resulting chunk will be 500-1000 Chinese characters
Returns a structured list of anchor sentences quoted exactly from the original text
The SemanticPipeline then:

Takes these anchor sentences and marks them as chunk boundaries by inserting <new-chunk> markers
Splits the document at these markers
Cleans up the resulting chunks by stripping whitespace and removing empty chunks
Returns the final list of semantically coherent text chunks

## Key Technologies Used
Azure OpenAI: Provides the GPT-4o model that powers the semantic analysis
Instructor: Framework for structured outputs from the LLM
Pydantic: Used for validation and structured data models
This approach ensures that documents are split at natural semantic boundaries, preserving the context and meaning of each chunk while maintaining reasonable chunk sizes for further processing.