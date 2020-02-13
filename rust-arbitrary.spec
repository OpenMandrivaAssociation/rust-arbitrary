# Generated by rust2rpm 13
# * https://github.com/rust-fuzz/rust_arbitrary/issues/10
%if 0%{?__isa_bits} == 32
%bcond_with check
%else
%bcond_without check
%endif
%global debug_package %{nil}

%global crate arbitrary

Name:           rust-%{crate}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Arbitrary trait for generating structured data from unstructured data

# Upstream license specification: MIT/Apache-2.0
# * https://github.com/rust-fuzz/rust_arbitrary/issues/9
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/arbitrary
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Arbitrary trait for generating structured data from unstructured data.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:02:50 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
