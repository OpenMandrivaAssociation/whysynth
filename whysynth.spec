Name:           whysynth
Summary:        Advanced synthesizer DSSI plugin
Version:        20120903
Release:        1

Source:         http://smbolton.com/%{name}/%{name}-%{version}.tar.bz2
URL:            http://smbolton.com/%{name}.html
License:        GPLv2
Group:          Sound
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  ladspa-devel
BuildRequires:  fftw-devel


%description
WhySynth is a versatile softsynth which operates as a plugin for the
DSSI Soft Synth Interface. Some of its features are 4 oscillators, 2
filters, 3 LFOs, and 5 envelope generators per voice, 10 oscillator
modes: minBLEP, wavecycle, asynchronous granular, three FM modes,
waveshaper, noise, PADsynth, and phase distortion, 6 filter modes,
flexible modulation and mixdown options, plus effects.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}/WhySynth_gtk
%{_datadir}/%{name}


%changelog
* Wed Sep 05 2012 Frank Kober <emuse@mandriva.org> 20120903-1
+ Revision: 816410
- new version 20120903

* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 20100922-2
+ Revision: 793823
- rebuild, spec cleanup

* Sat Sep 25 2010 Frank Kober <emuse@mandriva.org> 20100922-1mdv2011.0
+ Revision: 581022
- new version 20100922 (new waveform, knobs)

* Mon Dec 21 2009 Stéphane Téletchéa <steletch@mandriva.org> 20090608-2mdv2010.1
+ Revision: 480588
- Move autoconf command n the build section

* Fri Dec 18 2009 Frank Kober <emuse@mandriva.org> 20090608-1mdv2010.1
+ Revision: 480032
- Update rpm group tag
- import whysynth


* Mon Dec 18 2009 Frank Kober <emuse@mandriva.org> 20090608-1mdv2010.0
- import whysynth
