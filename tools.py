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
            elif len(pages[i]) == 2:
                b_page = int(pages[i][0]) - 1
                e_page = int(pages[i][1])
                for j in range(b_page, e_page):
                    if rpages[i] > 0:
                        reader.pages[j].rotate(rpages[i])
                    writer.add_page(reader.pages[j])
            elif len(pages[i]) == 1:
                be_page = int(pages[i][0]) - 1
                if rpages[i] > 0:
                    reader.pages[be_page].rotate(rpages[i])
                writer.add_page(reader.pages[be_page])

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

def check_pagenr(filename, uinput):
    reader = PdfReader(filename)
    for page in uinput:
        pagenr = int(page)
        if not pagenr in range(1, reader.get_num_pages() + 1):
            print(page)
            print(reader.get_num_pages())
            return False
    return True