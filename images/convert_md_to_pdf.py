#!/usr/bin/env python3
"""
Convert Markdown to PDF - Simple and robust version
"""
import html
from fpdf import FPDF
from pathlib import Path
import re
from datetime import datetime

md_file = Path("DEVELOPER_REVIEW.md")
pdf_file = Path("DEVELOPER_REVIEW.pdf")

with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "", 10)

# Helper function to clean text
def clean_text(text):
    # Remove markdown formatting
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    
    # Replace ALL unicode special characters with ASCII equivalents
    unicode_replacements = {
        '\u2014': '-', '\u2013': '-', '\u2012': '-',
        '\u2018': "'", '\u2019': "'", '\u201A': "'",
        '\u201C': '"', '\u201D': '"', '\u201E': '"',
        '\u2190': '<-', '\u2192': '->',  
        '\u2713': 'v', '\u2705': '[OK]', '\u2717': 'x', '\u2717': 'x',
        '\u00b1': '+/-', '\u00d7': 'x', '\u00f7': '/',
        '\u00b7': '*', '\u2022': '*',
        '\u2017': '_', '\u2191': '^', '\u2193': 'v',
        '\u2212': '-', '\u2215': '/',
        '\u00a9': '(C)', '\u00ae': '(R)', '\u2122': '(TM)',
    }
    
    for unicode_char, ascii_char in unicode_replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    # Remove any remaining non-ASCII characters
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    return html.escape(text)

lines = md_content.split('\n')

for line in lines:
    if not line.strip():
        pdf.ln(2)
        continue
    
    # Ensure we have space for new content
    if pdf.get_y() > pdf.h - 15:
        pdf.add_page()
    
    clean_line = clean_text(line)
    
    # Headers
    if line.startswith('# '):
        pdf.set_font("Helvetica", 'B', 16)
        pdf.set_text_color(0, 26, 102)
        pdf.cell(0, 10, clean_line[2:].strip()[:85], new_y='NEXT')
        pdf.set_text_color(0, 0, 0)
        pdf.ln(2)
        
    elif line.startswith('## '):
        pdf.set_font("Helvetica", 'B', 13)
        pdf.set_text_color(0, 26, 102)
        pdf.cell(0, 8, clean_line[3:].strip()[:85], new_y='NEXT')
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)
        
    elif line.startswith('### '):
        pdf.set_font("Helvetica", 'B', 11)
        pdf.set_text_color(128, 0, 32)
        pdf.cell(0, 7, clean_line[4:].strip()[:85], new_y='NEXT')
        pdf.set_text_color(0, 0, 0)
        pdf.ln(0.5)
        
    elif line.startswith('- '):
        pdf.set_font("Helvetica", "", 10)
        list_item = clean_line[2:].strip()[:80]
        pdf.cell(190, 5, '- ' + list_item, new_y='NEXT')
        pdf.ln(0.5)
        
    elif line.startswith('| '):
        # Skip complex table formatting
        continue
        
    else:
        # Regular paragraph text
        text_content = clean_line.strip()
        if len(text_content) > 2:
            pdf.set_font("Helvetica", "", 9)
            pdf.multi_cell(0, 5, text_content[:95], new_y='NEXT')
            pdf.ln(0.5)

# Footer
pdf.set_y(-15)
pdf.set_font("Helvetica", 'I', 8)
pdf.set_text_color(128, 128, 128)
pdf.cell(0, 5, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}', align='C')

# Save
pdf.output(str(pdf_file))

size_kb = pdf_file.stat().st_size / 1024
print(f"✓ PDF created successfully!")
print(f"  File: DEVELOPER_REVIEW.pdf")
print(f"  Size: {size_kb:.1f} KB")



