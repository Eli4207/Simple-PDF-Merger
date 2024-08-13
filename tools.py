from pypdf import PdfWriter


def merge_pdf(filename, pages, oname):
    merger = PdfWriter()
    for i in range(0, len(filename)):
        try:
            data = open(filename[i], "rb")
            if pages[i][0] == "a":
                merger.append(data)
            else:
                b_page = int(pages[i][0])-1
                e_page = int(pages[i][1])
                merger.append(fileobj=data, pages=(b_page, e_page))

        except:
            return False

    output = open(oname + ".pdf", "wb")
    merger.write(output)
    merger.close()
    output.close()
    return True
