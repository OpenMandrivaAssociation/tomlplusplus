Name:           tomlplusplus
Version:        3.4.0
Release:        1
Summary:        Header-only TOML config file parser and serializer for C++17
License:        MIT
URL:            https://github.com/marzer/tomlplusplus
Source0:        https://github.com/marzer/tomlplusplus/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  pkgconfig(catch2)

%description
toml++ is a TOML config parser and serializer for c++.
 
- Header-only (optional!)
- Supports the latest [TOML] release ([v1.0.0]), plus optional support for some
unreleased TOML features
- Passes all tests in the [toml-test](https://github.com/BurntSushi/toml-test)
suite
- Supports serializing to JSON and YAML
- Proper UTF-8 handling (incl. BOM)
- C++17 (plus some C++20 features where available, e.g. experimental support for
[char8_t] strings)
- Doesn't require RTTI
- Works with or without exceptions
- Tested on Clang (6+), GCC (7+) and MSVC (VS2019)
- Tested on x64, x86 and ARM
 
%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
%prep
%autosetup -p1
 
# remove the third party libraries for testing
rm -r vendor/
 
%build
%meson \
    -Dbuild_examples=true \
    -Duse_vendored_libs=false \
    -Dbuild_tests=false

%meson_build

%install
%meson_install
 
%files
%license LICENSE
%doc README.md
%{_libdir}/libtomlplusplus.so.3*
 
%files devel
%{_includedir}/toml++/
%dir %{_libdir}/cmake/tomlplusplus
%{_libdir}/cmake/tomlplusplus/*.cmake
%{_libdir}/libtomlplusplus.so
%{_libdir}/pkgconfig/tomlplusplus.pc
