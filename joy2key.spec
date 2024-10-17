Name:			joy2key
Version:		1.6.3
Release:		5

Summary:	Translate joystick events into keyboard events
License:	GPLv2
# keyboard emulator:
Group:		Emulators
URL:		https://sourceforge.net/projects/joy2key/
Source0:	http://downloads.sourceforge.net/joy2key/joy2key-%{version}.tar.bz2
# Uses xwininfo to find the window.
Requires:	xwininfo
BuildRequires:	pkgconfig(x11)

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.3-3mdv2011.0
+ Revision: 619833
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.6.3-2mdv2010.0
+ Revision: 438058
- rebuild

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 359227
- new version
- drop patches, applied upstream
- update URL

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.6.1-3mdv2009.0
+ Revision: 267308
- rebuild early 2009.0 package (before pixel changes)

* Sun May 18 2008 Anssi Hannula <anssi@mandriva.org> 1.6.1-2mdv2009.0
+ Revision: 208789
- requires xwininfo

* Sun May 18 2008 Anssi Hannula <anssi@mandriva.org> 1.6.1-1mdv2009.0
+ Revision: 208697
- initial Mandriva release

