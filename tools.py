import pikepdf


def merge_pdf(filename, pages, rpages, oname):
    writer = pikepdf.Pdf.new()
    for i in range(0, len(filename)):
        try:
            reader = pikepdf.Pdf.open(filename[i])
            if pages[i][0] == "a":
                for page in reader.pages:
                    page.rotate(rpages[i], relative=True)
                    writer.pages.append(page)
            else:
                b_page = int(pages[i][0]) - 1
                e_page = int(pages[i][1])
                for j in range(b_page, e_page):
                    reader.pages[j].rotate(rpages[i], relative=True)
                    writer.pages.append(reader.pages[j])
        except:
            return False

    writer.save(oname + ".pdf")
    writer.close()
    return True
