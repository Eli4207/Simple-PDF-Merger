from pypdf import PdfWriter, PdfReader


def merge_pdf(filename, pages, rpages, oname):
    writer = PdfWriter()
    for i in range(0, len(filename)):
        try:
            reader = PdfReader(filename[i])
            if pages[i][0] == "a":
                for page in reader.pages:
                    page.rotate(rpages[i])
                    writer.add_page(page)
            else:
                b_page = int(pages[i][0]) - 1
                e_page = int(pages[i][1])
                for j in range(b_page, e_page):
                    reader.pages[j].rotate(rpages[i])
                    writer.add_page(reader.pages[j])
        except:
            return False

    output = open(oname + ".pdf", "wb")
    writer.write(output)
    writer.close()
    output.close()
    return True
