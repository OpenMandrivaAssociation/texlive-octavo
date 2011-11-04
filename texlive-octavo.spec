# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/octavo
# catalog-date 2007-03-07 18:02:23 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-octavo
Version:	1.2
Release:	1
Summary:	Typeset books following classical design and layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/octavo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octavo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
