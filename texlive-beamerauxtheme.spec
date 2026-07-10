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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a collection of inner and outer themes as
supplements to the default themes in the beamer distribution. These
themes can be used in combination with existing inner, outer, and color
themes.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerauxtheme
%dir %{_datadir}/texmf-dist/tex/latex/beamerauxtheme
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-content.ltx
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-inner-simplelines.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-inner-simplelines.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-sidebarwithminiframes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-sidebarwithminiframes.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-splitwithminiframes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-splitwithminiframes.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-twolines.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerauxtheme/example-outer-twolines.tex
%{_datadir}/texmf-dist/tex/latex/beamerauxtheme/beamerinnerthemesimplelines.sty
%{_datadir}/texmf-dist/tex/latex/beamerauxtheme/beamerouterthemesidebarwithminiframes.sty
%{_datadir}/texmf-dist/tex/latex/beamerauxtheme/beamerouterthemesplitwithminiframes.sty
%{_datadir}/texmf-dist/tex/latex/beamerauxtheme/beamerouterthemetwolines.sty
