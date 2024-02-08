'''
This is a script that can take poster sized pdf files, and tile them into 
8.5 x 11 pages for printing on a home printer.
'''


import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def tile_pdf(input_pdf, output_pdf, input_width, input_length):
    # Constants for 8.5 by 11 inch page size
    # Using slightly smaller dimensions so that there is a margin when you print
    page_width = 8 * 72  # Convert inches to points
    page_height = 10.5 * 72

    # Calculate the number of rows and columns
    rows = int(input_length / 8)
    columns = int(input_width / 10.5)

    # Initialize a PdfFileWriter object for the output PDF
    writer = PdfFileWriter()

    # Open the input PDF file
    with open(input_pdf, 'rb') as input_file:
        reader = PdfFileReader(input_file)
        total_pages = reader.getNumPages()

        # Calculate the dimensions for cropping each page
        crop_width = reader.getPage(0).mediaBox.getWidth() / columns
        crop_height = reader.getPage(0).mediaBox.getHeight() / rows

        # Iterate through each page of the input PDF
        for page_num in range(total_pages):
            page = reader.getPage(page_num)

            # Iterate through each tile
            for row in range(rows):
                for col in range(columns):
                    # Calculate the cropping box
                    x0 = col * crop_width
                    y0 = (rows - row - 1) * crop_height  # Invert y-axis
                    x1 = x0 + crop_width
                    y1 = y0 + crop_height

                    # Create a new blank page with the appropriate dimensions
                    new_page = writer.addBlankPage(width=page_width, height=page_height)

                    # Scale and translate the content of the original page
                    new_page.mergeTranslatedPage(page, tx=-x0, ty=-y0)

        # Write the tiled PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    return rows * columns

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Tile a PDF into 8.5 by 11 inch pages.')
    parser.add_argument('--input_pdf', '-i', help='Input PDF file', required=True)
    parser.add_argument('--output_pdf', '-o', help='Output PDF file', required=True)
    parser.add_argument('--input_pdf_w', '-w', help='Input PDF width in inches.', required=True)
    parser.add_argument('--input_pdf_l', '-l', help='Input PDF length in inches.', required=True)

    args = parser.parse_args()

    # Tile the PDF
    print('Tiling your poster. Please wait.')
    num_pages = tile_pdf(args.input_pdf, args.output_pdf, int(args.input_pdf_w), int(args.input_pdf_l))
    print(f'Total number of 8.5 by 11 inch pages generated: {num_pages}')
