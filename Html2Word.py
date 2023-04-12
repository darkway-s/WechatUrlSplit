import docx
import html2text

# Load the HTML content into a string variable
with open('test.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Convert the HTML content to plain text
text_converter = html2text.HTML2Text()
text_converter.ignore_links = True
plain_text = text_converter.handle(html_content)

# Create a new Word document
doc = docx.Document()

# Add the plain text content to the document as a new paragraph
doc.add_paragraph(plain_text)

# Save the resulting document
doc.save('output.docx')
