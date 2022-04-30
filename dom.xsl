<?xml version="1.0" encoding="utf-8" ?>
<!-- Created with Liquid Studio 2020 (https://www.liquid-technologies.com) -->
<xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" omit-xml-declaration="yes" />


    <xsl:template match="/">
        <html>
            <head>
                <title>Covid19</title>
            </head>
            <body>
                <h1>Covid19</h1>
                <table border='1'>
                    <tr>
                        <th>Date</th>
                        <th>Cases</th>
                        <th>Deaths</th>
                        <th>Country</th>
                        <th>Population</th>
                        <th>Continent</th>
                    </tr>
                    <xsl:for-each select="/records/record">
					<xsl:if test="countriesAndTerritories = 'Iran'">

                        <tr>
                            <td>
                                <xsl:value-of select='dateRep' />
                            </td>
                            <td>
                                <xsl:value-of select='cases' />
                            </td>
                            <td>
                                <xsl:value-of select='deaths' />
                            </td>
                            <td>
                                <xsl:value-of select='countriesAndTerritories' />
                            </td>
                            <td>
                                <xsl:value-of select='popData2018' />
                            </td>
                            <td>
                                <xsl:value-of select='continentExp' />
                            </td>
                        </tr>
					</xsl:if>						
                    </xsl:for-each>



                </table>

            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>