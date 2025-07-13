import re
from typing import List
from functools import partial
from pydantic import BaseModel, Field

def chinese_sentence_split(text:str) -> List[str]:

    """
    Splits a given Chinese text into a list of sentences based on common Chinese sentence delimiters.
    Args:
        text (str): The input text to be split into sentences.
    Returns:
        List[str]: A list of sentences extracted from the input text.
    """
    
    # Define the regular expression pattern for Chinese sentence delimiters
    pattern = re.compile(r'(?<=[。！？；])|[\n]+')
    
    # Split the text using the pattern
    sentences = pattern.split(text)
    
    # Remove any empty strings from the list
    sentences = [sentence for sentence in sentences if sentence.strip()]
    
    return sentences


def langchain_recursive_split(text:str, *args, **kwargs) -> List[str]:
    """
    Splits the given text into a list of strings using the RecursiveCharacterTextSplitter from langchain_text_splitters.
    Args:
        text (str): The text to be split.
        *args: Additional positional arguments to be passed to RecursiveCharacterTextSplitter.
        **kwargs: Additional keyword arguments to be passed to RecursiveCharacterTextSplitter.
    Returns:
        List[str]: A list of strings resulting from the split operation.
    """
    
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except:
        raise ImportError("langchain_text_splitters is not installed. Please install it using `pip install langchain-text-splitters`.")
    
    splitter = RecursiveCharacterTextSplitter(
        *args, **kwargs
    )

    return splitter.split_text(text)


def langchain_recursive_chinese_split(
    text:str, 
    chunk_size:int = 250,
    chunk_overlap = 0) -> List[str]:
    
    """
    Splits the given Chinese text into chunks using a recursive splitting function.
    This function uses a partial application of `langchain_recursive_split` with specific
    separators and parameters tailored for Chinese text. The text is split based on 
    various punctuation marks and newlines, ensuring that each chunk is of a specified 
    size and overlap.
    Args:
        text (str): The Chinese text to be split.
    Returns:
        List[str]: A list of text chunks.
    """
    
    split_fn = partial(
        langchain_recursive_split, 
        separators=["\n\n", "\n", "。","!","？","！","；",";"],
        length_function=len,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        keep_separator=True
    )
    
    return split_fn(text)
