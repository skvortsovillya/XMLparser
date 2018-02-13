import abc
import xml.dom.minidom
import xml.sax


class Document:

    def __init__(self, strategy, doc, output, city=None, address=None, name=None, price=None, rate=None, kind=None,
                 bags=None):

        self._strategy = strategy
        self.output = output
        self.doc = doc
        self.city = city
        self.address = address
        self.name = name
        self.price = price
        self.rate = rate
        self.kind = kind
        self.bags = bags

    def context_interface(self):
        self._strategy.parser(self.doc, self.output, self.city, self.address, self.name, self.price, self.rate, self.kind,
                              self.bags)


class Analise(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parser(self, doc, output, city=None, address=None, name=None, price=None, rate=None, kind=None, bags=None):
        pass


class DOM(Analise):

    result = []

    def parser(self, doc, output, city=None, address=None, name=None, price=None, rate=None, kind=None, bags=None):

        for nodeCoffee in doc.getElementsByTagName("coffee"):
            cities = nodeCoffee.getElementsByTagName("city")
            addresses = nodeCoffee.getElementsByTagName("address")
            names = nodeCoffee.getElementsByTagName("name")
            prices = nodeCoffee.getElementsByTagName("price")
            rates = nodeCoffee.getElementsByTagName("rate")
            kinds = nodeCoffee.getElementsByTagName("kind")
            bags_all = nodeCoffee.getElementsByTagName("bags")

            node_city_text = cities[0].firstChild
            if city not in (node_city_text.data, None):
                continue
            node_address_text = addresses[0].firstChild
            if address not in (node_address_text.data, None):
                continue
            node_name_text = names[0].firstChild
            if name not in (node_name_text.data, None):
                continue
            node_price_text = prices[0].firstChild
            if price not in (node_price_text.data, None):
                continue
            node_rate_text = rates[0].firstChild
            if rate not in (node_rate_text.data, None):
                continue
            node_kind_text = kinds[0].firstChild
            if kind not in (node_kind_text.data, None):
                continue
            node_bags_text = bags_all[0].firstChild
            if bags not in (node_bags_text.data, None):
                continue
            self.result.append('Місто: ' + node_city_text.data + '\n')
            self.result.append('Адреса: ' + node_address_text.data + '\n')
            self.result.append("Ім'я: " + node_name_text.data + '\n')
            self.result.append('Ціна: ' + node_price_text.data + '\n')
            self.result.append('Рейтинг: ' + node_rate_text.data + '\n')
            self.result.append('Вид: ' + node_kind_text.data + '\n')
            self.result.append('Несправності автомату: ' + node_bags_text.data + '\n')

            self.result.append("------------------------------------------------------------------------\n")

        #print(self.result)
        for line in self.result:
            output.write(line)


class SAX(Analise):

    result1 = []

    def parser(self, doc, output, city=None, address=None, name=None, price=None, rate=None, kind=None, bags=None):
        class ABContentHandler(xml.sax.ContentHandler):
            result1 = []
            def __init__(self, out=output, cityx=city, addressx=address, namex=name, pricex=price, ratex=rate, kindx=kind,
                         bagsx=bags):
                xml.sax.ContentHandler.__init__(self)
                self.out = out

                self.root_count = 0

                self.result = []

                self.start_tag = ""
                self.end_tag = ""

                self.flag_print = False

                self.d_flag = False

                self.cityx = cityx
                self.addressx = addressx
                self.namex = namex
                self.pricesx = pricex
                self.ratex = ratex
                self.kindx = kindx
                self.bagsx = bagsx

            def startElement(self, name, attrs):
                self.start_tag = name

            def endElement(self, name):
                self.end_tag = name

            def characters(self, content):
                if not content.isspace():
                    if self.start_tag.strip(" ") == 'city' and self.cityx in [content.strip(" "), None]:
                        self.result.append('Місто: ' + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'city':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'address' and self.addressx in [content.strip(" "), None] and self.d_flag:
                        self.result.append('Адреса: ' + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'address':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'name' and self.namex in [content.strip(" "), None] and self.d_flag:
                        self.result.append("Ім'я: " + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'name':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'price' and self.pricesx in [content.strip(" "),
                                                                                 None] and self.d_flag:
                        self.result.append('Ціна: ' + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'price':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'rate' and self.ratex in [content.strip(" "), None] and self.d_flag:
                        self.result.append('Рейтинг: ' + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'rate':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'kind' and self.kindx in [content.strip(" "), None] and self.d_flag:
                        self.result.append('Вид: ' + content)
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'kind':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'bags' and self.bagsx in [content.strip(" "), None] and self.d_flag:
                        self.result.append('Несправності автомату: ' + content + '\n')
                        self.d_flag = True
                    elif self.start_tag.strip(" ") == 'bags':
                        self.d_flag = False

                    if self.start_tag.strip(" ") == 'bags' and content:
                        self.flag_print = True

                    if self.flag_print and self.d_flag and len(self.result) > 3:
                        for item in self.result:
                            self.out.write(item + '\n')
                            self.result1.append(item)

                        self.flag_print = False
                        self.result.clear()
                    elif self.flag_print:
                        self.result.clear()

            def get_result1(self):
                return self.result1

        xml.sax.parse(doc, ABContentHandler(output))



if __name__ == '__main__':
    xml_document = xml.dom.minidom.parse('1.xml')
    dom = DOM()
    sax = SAX()
    source = open('1.xml', encoding='utf-8')
    #output = open("output5.txt", 'w', encoding='utf-8')

    global city, address, name, price, rate, kind, bags
    print(city, address, name, price, rate, kind, bags)

    document = Document(sax, source, output, city=city, address=address, name=name, price=price,
                        rate=rate,
                        kind=kind, bags=bags)
    document.context_interface()

    out = open('output2.txt', 'w', encoding='utf8')

    document = Document(dom, xml_document, out, price=price_test)
    document.context_interface()

