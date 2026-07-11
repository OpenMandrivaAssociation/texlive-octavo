%global tl_name octavo
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Typeset books following classical design and layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/octavo
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The octavo class is a modification of the standard LaTeX book class. Its
purpose is to typeset books following classical design and layout
principles, with the express intention of encouraging the making of
beautiful books by anyone with access to a good printer and with an
inclination towards venerable crafts, e.g., bookbinding. The octavo
class differs from the book class by implementing many of the proposals
and insights of respected experts, especially Jan Tschichold and Hugh
Williamson. The documentation discusses methods to organise and print
out any text into signatures, which can then be gathered, folded and
sewn into a book.

