from pdfdata import parse_pdf, pdf_doc_extract_span_df, pdf_doc_extract_span_list, pdf_text_to_jsonnl
from pprint import pprint

# parse pdf as dictionary
pdf_parsed = parse_pdf('pdfs/0641-20.pdf')
res        = pdf_doc_extract_span_list(pdf_parsed)

pprint(res, depth=3)

# parse pdf as list of spans
pdf_parsed = parse_pdf('pdfs/0641-20.pdf')
res        = pdf_doc_extract_span_df(pdf_parsed)

pprint(res[0])

# transform pdf text to jsonnl
pdf_text_to_jsonnl('pdfs/0641-20.pdf', '0641-20.jsonnl')