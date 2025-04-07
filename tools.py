from pypdf import PdfWriter, PdfReader

comp_level = [40, 24, 15]

def merge_pdf(filename, pages, rpages, oname, comp):
    writer = PdfWriter()
    for i in range(0, len(filename)):
        try:
            reader = PdfReader(filename[i])
            if pages[i][0] == "a":
                for page in reader.pages:
                    if rpages[i] > 0:
                        page.rotate(rpages[i])
                    writer.add_page(page)
            else:
                b_page = int(pages[i][0]) - 1
                e_page = int(pages[i][1])
                for j in range(b_page, e_page):
                    if rpages[i] > 0:
                        reader.pages[j].rotate(rpages[i])
                    writer.add_page(reader.pages[j])
        except:
            return False

    if comp > 0:
        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality=comp_level[comp - 1])

    output = open(oname + ".pdf", "wb")
    writer.write(output)
    writer.close()
    output.close()
    return True