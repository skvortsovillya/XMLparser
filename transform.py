from lxml import etree


def transform(xml_f):
    xslt_doc = etree.parse("transform.xsl")
    xslt_transformer = etree.XSLT(xslt_doc)

    source_doc = etree.parse(xml_f)
    output_doc = xslt_transformer(source_doc)

    html_f = xml_f.strip(".xml") + ".html"
    output_doc.write(html_f, pretty_print=True)


if __name__ == '__main__':
    xml_doc = "1.xml"
    transform(xml_doc)
