%define	api	0.0.2
%define	major	0
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname %{name} %{api} -d

Summary:	Gesture Library for Clutter
Name:		clutter-gesture
Version:	0.0.2.1
Release:	3
Group:		System/Libraries
License:	LGPLv2+ and MIT
URL:		http://maemo.org/packages/view/clutter-gesture/
Source0:	http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch1:		clutter-gesture-0.0.2-build.patch

BuildRequires:	pkgconfig(clutter-x11-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)

%description
This library allows clutter applications to be aware of gestures 
and to easily attach some handlers to the gesture events. The library 
supports both single and multi touch.

%package -n	%{libname}
Summary:	Gesture Library for Clutter
Group:		System/Libraries

%description -n	%{libname}
This library allows clutter applications to be aware of gestures
and to easily attach some handlers to the gesture events. The library
supports both single and multi touch.

%package -n	%{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
Files for development with %{name}.

%prep
%setup -q
%apply_patches
autoreconf -vfi

# don't treat warnings as errors
sed -i -e 's,-Werror,,g' configure.ac

# The NEWS file contains the license so use it as a COPYING file. Upstream has been contacted to resolve the issue
cp NEWS COPYING

%build
%configure2_5x \
	--disable-static

%make LIBS=-lm CFLAGS+="-DGLIB_DISABLE_DEPRECATION_WARNINGS -DCLUTTER_DISABLE_DEPRECATION_WARNINGS" V=1

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING
%{_libdir}/libcluttergesture-%{api}.so.%{major}*
%{_libdir}/libengine.so.%{major}*

%files -n %{devname}
%{_libdir}/libcluttergesture-%{api}.so
%{_libdir}/libengine.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
