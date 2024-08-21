from PyPDF2 import *

def extract_pdf_text(pdf,/,start=0,stop=None,step=1):
    """
    Extracts cleaned text from the specified pages of a PDF.

    :param pdf: Path to the PDF file.
    :param start: Starting page number (0-indexed).
    :param stop: Ending page number (exclusive). Defaults to None, meaning until the last page.
    :param step: Step size between pages.
    :return: List of cleaned words extracted from the PDF.
    """
    try:
        pdf_file = PdfReader(pdf)
    except FileNotFoundError as error_msg:
        import sys
        print(error_msg)
        sys.exit(1)
    
    valid_words = []
    pages = len(pdf_file.pages)
    if stop is None or stop > pages:
        stop = pages
        
    for i in range(start,stop,step):
            page_text = pdf_file.pages[i].extract_text().split()
            word_list = [''.join([letter for letter in word.lower() if letter.isalpha()]) for word in page_text if len(word) > 1]

            valid_words.extend(word_list)

    return valid_words

def words_frequencies(content):
    """
    Computes word frequencies based on the list of words.

    :param words: List of words.
    :return: Dictionary with words as keys and their frequencies as values.
    """
    words_freq = {}
    total_content = len(content)
    if total_content == 0:
        return words_dreq
    
    probability_increment = 1/total_content
    for word in content:
        words_freq[word] = words_freq.get(word,0) + probability_increment

    return words_freq

def compare_pdfs(pdf1,pdf2,/,*,start1=0,stop1=None,step1=1,start2=0,stop2=None,step2=1):
	"""
    Compares the similarity between two PDFs based on word frequencies.

    :param pdf1: Path to the first PDF file.
    :param pdf2: Path to the second PDF file.
    :param start1: Starting page number for the first PDF.
    :param stop1: Ending page number for the first PDF.
    :param step1: Step size between pages for the first PDF.
    :param start2: Starting page number for the second PDF.
    :param stop2: Ending page number for the second PDF.
    :param step2: Step size between pages for the second PDF.
    :return: Similarity score based on the overlap of word frequencies.
    """
    words_freq1 = words_frequencies(extract_pdf_text(pdf1,start1,stop1,step1))
    words_freq2 = words_frequencies(extract_pdf_text(pdf2,start2,stop2,step2))
    
    similarity = sum(words_freq1.get(word,0) for word in words_freq2)

    return similarity
