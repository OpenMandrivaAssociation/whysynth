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
