Name:			joy2key
Version:		1.6.1
# (Anssi) wrongly versioned tarball...
%define tarfilever	1.6
Release:		%mkrel 2

Summary:	Translate joystick events into keyboard events
License:	GPLv2
# keyboard emulator:
Group:		Emulators
URL:		http://interreality.org/~tetron/technology/joy2key/
Source0:	http://interreality.org/~tetron/technology/joy2key/joy2key-%{tarfilever}.tar.gz
# Debian patches:
Patch0:		x-libs-in-standard-search-path.patch
Patch1:		argtokey-implicit-declaration.patch
Patch2:		accept-0-as-threshold.patch
Patch3:		correct-string-freeing.patch
Patch4:		process-args-fix.patch

# Uses xwininfo to find the window.
Requires:	xwininfo
BuildRequires:	libx11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Joy2key will translate your joystick movements into the equivalent
keystrokes. Joy2key works both in X and at the console, both raw and
terminal modes.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README TODO joy2keyrc.sample
%{_bindir}/joy2key
%{_mandir}/man1/joy2key.1*

