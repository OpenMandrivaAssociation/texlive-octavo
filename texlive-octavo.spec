Name:		texlive-octavo
Version:	15878
Release:	1
Summary:	Typeset books following classical design and layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/octavo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The octavo class is a modification of the standard LaTeX book
class. Its purpose is to typeset books following classical
design and layout principles, with the express intention of
encouraging the making of beautiful books by anyone with access
to a good printer and with an inclination towards venerable
crafts, e.g., bookbinding. The octavo class differs from the
book class by implementing many of the proposals and insights
of respected experts, especially Jan Tschichold and Hugh
Williamson. The documentation discusses methods to organise and
print out any text into signatures, which can then be gathered,
folded and sewn into a book.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/octavo/oct10.clo
%{_texmfdistdir}/tex/latex/octavo/oct11.clo
%{_texmfdistdir}/tex/latex/octavo/oct12.clo
%{_texmfdistdir}/tex/latex/octavo/octavo.cls
%doc %{_texmfdistdir}/doc/latex/octavo/README
%doc %{_texmfdistdir}/doc/latex/octavo/changes
%doc %{_texmfdistdir}/doc/latex/octavo/tub-octavo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/octavo/octavo.dtx
%doc %{_texmfdistdir}/source/latex/octavo/octavo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
