Name:			joy2key
Version:		1.6.3
Release:		%mkrel 1

Summary:	Translate joystick events into keyboard events
License:	GPLv2
# keyboard emulator:
Group:		Emulators
URL:		http://sourceforge.net/projects/joy2key/
Source0:	http://downloads.sourceforge.net/joy2key/joy2key-%{version}.tar.bz2
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

