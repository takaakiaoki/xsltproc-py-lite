#!python
# xsltproc subset using python+lxml
# python xsltproc_py.py [-o output_xml_file] stylesheet input_xml_file

import sys
import lxml.etree as ET
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="subset implementation of xlstproc using python+lxml"
    )
    parser.add_argument("stylesheet", help="XSLT stylesheet file")
    parser.add_argument("xmlfile", help="Input XML file")
    parser.add_argument("-o", "--output", metavar="FILE", default="-",
                        help="Output file (use '-' or omit for stdout)")
    args = parser.parse_args()

    try:
        # read XSLT
        xslt_doc = ET.parse(args.stylesheet)
        transform = ET.XSLT(xslt_doc)

        # read input XML
        xml_doc = ET.parse(args.xmlfile)

        # transformation
        result = transform(xml_doc)

        # output to stdout
        if args.output == '-' :
            print(str(result))
        else:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(str(result))
    
    except ET.XSLTParseError as e:
        print(f'XSLT parse error: {e}', file=sys.stderr)
        sys.exit(2)
    except ET.XMLSyntaxError as e:
        print(f'XML syntax error: {e}', file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(4)

if __name__ == '__main__':
    main()
