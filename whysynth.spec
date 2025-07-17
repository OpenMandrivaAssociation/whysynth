%global	_disable_ld_no_undefined 1

Summary:	Advanced synthesizer DSSI plugin
Name:	whysynth
Version:	20170701
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://smbolton.com/whysynth.html
Source0:	https://smbolton.com/whysynth/%{name}-%{version}.tar.bz2
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblo)

%description
WhySynth is a versatile softsynth which operates as a plugin for the DSSI Soft
Synth Interface. Some of its features are 4 oscillators, 2 filters, 3 LFOs, 5
envelope generators per voice, 10 oscillator modes (minBLEP, wavecycle,
asynchronous granular, three FM modes, waveshaper, noise, PADsynth and phase
distortion), 6 filter modes, flexible modulation and mixdown options,
plus effects.

%files
%license COPYING
%doc README.rst AUTHORS TODO
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}/WhySynth_gtk
%{_datadir}/%{name}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install
