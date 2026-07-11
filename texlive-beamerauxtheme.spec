%global tl_name beamerauxtheme
%global tl_revision 56087

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02a
Release:	%{tl_revision}.1
Summary:	Supplementary outer and inner themes for beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerauxtheme
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerauxtheme.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerauxtheme.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a collection of inner and outer themes as
supplements to the default themes in the beamer distribution. These
themes can be used in combination with existing inner, outer, and color
themes.

