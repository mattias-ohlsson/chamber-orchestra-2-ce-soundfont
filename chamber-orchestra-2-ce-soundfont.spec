Name:           chamber-orchestra-2-ce-soundfont
Version:        1.1.0
Release:        1%{?dist}
Summary:        Versilian Studios Chamber Orchestra 2 Community Edition

License:        CC0
URL:            https://vis.versilstudios.com/vsco-community.html
Source0:        https://github.com/sgossner/VSCO-2-CE/archive/%{version}.tar.gz

BuildArch:      noarch

%description
VSCO 2 Community Edition is an open-source, open-ended subset of the main VSCO
2 library designed for young composers, hobbyist sample library developers,
and students around the world to create better sounding music for free and
learn more about the process of sample library development.

%prep
%autosetup -n VSCO-2-CE-%{version}

%build
rm .gitignore

%install
rm -rf $RPM_BUILD_ROOT
install --directory $RPM_BUILD_ROOT%{_datadir}/soundfonts/chamber-orchestra-2-ce/
cp -a ./. $RPM_BUILD_ROOT%{_datadir}/soundfonts/chamber-orchestra-2-ce/
rm $RPM_BUILD_ROOT%{_datadir}/soundfonts/chamber-orchestra-2-ce/LICENSE
rm $RPM_BUILD_ROOT%{_datadir}/soundfonts/chamber-orchestra-2-ce/README.md
rm $RPM_BUILD_ROOT%{_datadir}/soundfonts/chamber-orchestra-2-ce/*.txt

%files
%license LICENSE
%doc Readme.txt README.md "How To Install.txt"
%{_datadir}/soundfonts/chamber-orchestra-2-ce

%changelog
* Thu Apr  9 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.1.0-1
- Initial build
