%global tl_name sclang-prettifier
%global tl_revision 35087

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Prettyprinting SuperCollider source code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sclang-prettifier
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sclang-prettifier.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Built on top of the listings package, the package allows effortless
prettyprinting of SuperCollider source code in documents typeset with
LaTeX & friends.

