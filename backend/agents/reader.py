# reader.py
from utils.pdf_utils import extract_text_from_pdf

try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
except Exception:
    RecursiveCharacterTextSplitter = None


class SimpleSplitter:
    """A tiny fallback splitter that breaks text into chunks by size."""
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str):
        res = []
        i = 0
        L = len(text)
        while i < L:
            end = min(i + self.chunk_size, L)
            res.append(text[i:end])
            i = end - self.chunk_overlap if end < L else end
        return res


class ReaderAgent:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        if RecursiveCharacterTextSplitter is not None:
            self.splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )
        else:
            self.splitter = SimpleSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def read_pdf(self, path: str):
        raw = extract_text_from_pdf(path)
        cleaned = self.clean_text(raw)
        chunks = self.splitter.split_text(cleaned)
        # produce small topic-ish chunks
        return chunks

    def clean_text(self, text: str) -> str:
        # simple cleaning, can be extended
        text = text.replace("\r", "\n")
        return text
