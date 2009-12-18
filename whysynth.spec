%define name    whysynth
%define version 20090608
%define release %mkrel 1 

Name:           %{name} 
Summary:        Advanced synthesizer DSSI plugin
Version:        %{version} 
Release:        %{release}

Source:         http://smbolton.com/%{name}/%{name}-%{version}.tar.bz2
URL:            http://smbolton.com/%{name}.html
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:  dssi-devel gtk2-devel liblo-devel alsa-lib-devel
BuildRequires:  ladspa-devel fftw-devel


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
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}.la
%{_libdir}/dssi/%{name}/WhySynth_gtk
%{_datadir}/%{name}
#%{_datadir}/%{name}/current_default_patches.WhySynth
#%{_datadir}/%{name}/more_K4_interpretations.WhySynth
#%{_datadir}/%{name}/version_20051005_patches.WhySynth
#%{_datadir}/%{name}/version_20051231_patches.WhySynth

