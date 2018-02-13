<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>

    <xsl:template match="coffeeDataBase">
        <html>
            <body>
                <table border="1">
                    <tr bgcolor="#9acd32">
                      <th>Місто</th>
                      <th>Адреса</th>
                      <th>Напій</th>
                      <th>Ціна, грн</th>
                       <th>Рейтинг</th>
                      <th>Вид</th>
                      <th>Несправності автомату</th>
                    </tr>
                    <xsl:for-each select="coffee">
                        <tr>
                            <td><xsl:value-of select="city"/></td>
                            <td><xsl:value-of select="address"/></td>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td><xsl:value-of select="rate"/></td>
                            <td><xsl:value-of select="kind"/></td>
                            <td><xsl:value-of select="bags"/></td>
                        </tr>>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
