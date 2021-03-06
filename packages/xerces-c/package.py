from spack import *

class XercesC(Package):
    """ Xerces-C++ is a validating XML parser written in a portable subset of C++.
    Xerces-C++ makes it easy to give your application the ability to read and
    write XML data. A shared library is provided for parsing, generating,
    manipulating, and validating XML documents using the DOM, SAX, and SAX2 APIs.
    """

    homepage = "https://xerces.apache.org/xerces-c"
    url      = "https://www.apache.org/dist/xerces/c/3/sources/xerces-c-3.1.2.tar.gz"
    version('3.1.4', '21bb097b711a513275379b59757cba4c')
      
    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix,
                  "--disable-network")
        make("clean")
        make()
        make("install")

