# You shuold enable-network to finish the check
%bcond_without check

%global forgeurl  https://github.com/Qv2ray/shadowsocksr-uvw/
%global branch    master

%forgemeta

Name:             shadowsocksr-uvw
Version:          0
Release:          0.1%{?dist}
Summary:          A ShadowsocksR implementation in uvw

License:          GPLv3
URL:              %{forgeurl}
Source0:          %{forgesource}

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    cmake
BuildRequires:    libuv-devel
BuildRequires:    libsodium-devel
BuildRequires:    openssl-devel

Requires:         libuv >= 1.38.0
Requires:         libsodium
Requires:         openssl


%description
A minimal dependency shadowsocksr implementation.


%prep
%forgesetup


%build
%cmake -DSSR_UVW_WITH_QT=0 \
       -DUSE_SYSTEM_SODIUM=ON \
       -DUSE_SYSTEM_LIBUV=ON \
       -DSTATIC_LINK_LIBUV=OFF \
       -DSTATIC_LINK_SODIUM=OFF \
       -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%if %{with check}
%check
%ctest
%endif


%files
%license LICENSE COPYING
%doc README.md
%{_bindir}/ssr-local


%changelog
* Thu Oct  1 2020 sixg0000d <sixg0000d@gmail.com> - 0-0.1
- Initial shadowsocksr-uvw.
