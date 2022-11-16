Name:		texlive-sclang-prettifier
Version:	35087
Release:	1
Summary:	Prettyprinting SuperCollider source code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sclang-prettifier
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Built on top of the listings package, the package allows
effortless prettyprinting of SuperCollider source code in
documents typeset with LaTeX & friends.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sclang-prettifier
%{_texmfdistdir}/tex/latex/sclang-prettifier
%doc %{_texmfdistdir}/doc/latex/sclang-prettifier

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
