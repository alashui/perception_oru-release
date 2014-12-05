Name:           ros-hydro-ndt-feature-reg
Version:        1.0.27
Release:        0%{?dist}
Summary:        ROS ndt_feature_reg package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ndt_feature_reg
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl-devel
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-geometry
Requires:       ros-hydro-laser-geometry
Requires:       ros-hydro-ndt-map
Requires:       ros-hydro-ndt-registration
Requires:       ros-hydro-ndt-visualisation
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-srvs
BuildRequires:  pcl-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-geometry
BuildRequires:  ros-hydro-laser-geometry
BuildRequires:  ros-hydro-ndt-map
BuildRequires:  ros-hydro-ndt-registration
BuildRequires:  ros-hydro-ndt-visualisation
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-srvs

%description
ndt_feature_reg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Dec 05 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.27-0
- Autogenerated by Bloom

* Wed Dec 03 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.26-0
- Autogenerated by Bloom

* Mon Dec 01 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.25-0
- Autogenerated by Bloom

* Tue Nov 25 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.23-0
- Autogenerated by Bloom

* Tue Nov 25 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.24-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.22-0
- Autogenerated by Bloom

