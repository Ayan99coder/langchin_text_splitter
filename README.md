# LangChain Text Splitter Examples

Examples of document and text chunking with LangChain. The project demonstrates
character-based, recursive, language-aware, PDF, and embedding-based semantic
text splitting.

## Examples

| File | Description |
| --- | --- |
| `length_based_textSplitter.py` | Splits a PDF with `CharacterTextSplitter` and `RecursiveCharacterTextSplitter`. |
| `document_structured_textSplitter.py` | Splits Python and Markdown text using language-aware recursive separators. |
| `semantic_meaning_based.py` | Creates semantic chunks using Gemini embeddings and `SemanticChunker`. |

## Requirements

- Python 3.10 or newer
- A Google Gemini API key for the semantic chunking example

Install the dependencies:

```bash
pip install langchain-text-splitters langchain-community langchain-experimental langchain-google-genai python-dotenv pypdf
```

## Configuration

Create a `.env` file in the project root for the semantic example:

```env
GOOGLE_API_KEY=your_google_api_key
```

The `.env` file is ignored by Git and must not be committed.

## Running the examples

Run any example from the project root:

```bash
python length_based_textSplitter.py
python document_structured_textSplitter.py
python semantic_meaning_based.py
```

`length_based_textSplitter.py` expects `Ayan_Resume_Updated.pdf` to be present
in the project root.

## Concepts covered

- Character-based splitting with configurable chunk size and overlap
- Recursive splitting using paragraph, line, and word boundaries
- Language-specific splitting for Python and Markdown
- PDF loading with `PyPDFLoader`
- Semantic chunking based on embedding similarity
- Chunk metadata and document-oriented splitting

## Notes

These scripts print their results directly to the console and are intended as
learning examples. Chunk size, overlap, and semantic breakpoint settings can be
adjusted in each file for different document types.
