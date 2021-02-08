from pdfdata import *
from pprint import pprint

# parse pdf as dictionary
pdf_parsed = parse_pdf('pdfs/Rechnung-Muster-1.pdf')
res        = pdf_doc_extract_span_list(pdf_parsed)

pprint(res, depth=3)

# parse pdf as list of spans
pdf_parsed = parse_pdf('pdfs/Rechnung-Muster-1.pdf')
res        = pdf_doc_extract_span_df(pdf_parsed)

pprint(res[0])

pdf_parsed = parse_pdf('pdfs/Rechnung-Muster-1.pdf')
res        = pdf_doc_extract_block_line_df(pdf_parsed)


pdf_parsed = parse_pdf('pdfs/Rechnung-Muster-1.pdf')
res        = pdf_doc_extract_block_df(pdf_parsed)
